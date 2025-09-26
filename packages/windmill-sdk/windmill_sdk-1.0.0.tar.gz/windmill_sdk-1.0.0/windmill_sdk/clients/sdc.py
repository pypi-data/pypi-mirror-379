import asyncio
from urllib.parse import urljoin

import httpx
from typing import List
from ..models import Service, User


class SDCClient:
    def __init__(self, base_url: str, username: str, password: str, timeout: int = 10):
        self.base_url = base_url.rstrip("/")
        self.username = username
        self.password = password
        self.timeout = timeout
        self.token: str | None = None
        self.client = httpx.AsyncClient(
            base_url=self.base_url, timeout=timeout, follow_redirects=True
        )

    def _build_url(self, path: str) -> str:
        return urljoin(self.base_url + "/", path.lstrip("/"))

    async def _authenticate(self) -> str:
        response = await self.client.post(
            "/api/auth", json={"username": self.username, "password": self.password}
        )
        response.raise_for_status()
        token = response.json()["token"]
        self.token = token
        self.client.headers.update({"Authorization": f"Bearer {token}"})
        return token

    async def _request_with_retry(
        self, method: str, url: str, **kwargs
    ) -> httpx.Response:
        response: httpx.Response
        if not self.token:
            await self._authenticate()

        try:
            response = await self.client.request(method, self._build_url(url), **kwargs)

            if response.status_code == 401:
                # Token scaduto ➜ rigenerazione e retry
                await self._authenticate()
                response = await self.client.request(
                    method, self._build_url(url), **kwargs
                )

            elif response.status_code == 429:
                # Troppi tentativi ➜ rispetto del Retry-After
                retry_after = int(response.headers.get("Retry-After", "1"))
                await asyncio.sleep(retry_after)
                response = await self.client.request(
                    method, self._build_url(url), **kwargs
                )

            elif 500 <= response.status_code < 600:
                # Errore server ➜ 1 retry dopo 10 secondi
                await asyncio.sleep(10)
                response = await self.client.request(
                    method, self._build_url(url), **kwargs
                )

            response.raise_for_status()
            return response

        except httpx.HTTPError as e:
            print(
                f"[SDCClient] Errore durante la richiesta a {self.client.base_url}{self._build_url(url)}: {str(e)}"
            )
            raise

    async def list_services(self) -> List[Service]:
        response = await self._request_with_retry("GET", "/api/services")
        data = response.json()

        if not isinstance(data, list):
            raise ValueError("Risposta inattesa: attesa una lista di servizi")

        return [Service.model_validate(item) for item in data]

    async def get_service_by_identifier(self, identifier: str) -> Service:

        response = await self._request_with_retry(
            "GET", "/api/services", params={"identifier": identifier}
        )
        data = response.json()

        if not isinstance(data, list) or not data:
            raise ValueError(f"Nessun servizio trovato con identifier='{identifier}'")

        return Service.model_validate(data[0])

    async def list_users_by_role(self, role: str = "user") -> List[User]:
        if role not in ("admin", "user", "operator"):
            raise ValueError(
                f"Ruolo '{role}' non valido: i valori ammessi sono admin,user,operator'"
            )

        response = await self._request_with_retry(
            "GET", "/api/users", params={"roles": role}
        )
        data = response.json()

        if not isinstance(data, list):
            raise ValueError("Risposta inattesa: attesa una lista di utenti")

        users: List[User] = []
        for raw in data:
            mapped = {
                "first_name": raw.get("nome"),
                "last_name": raw.get("cognome"),
                "username": raw.get("username"),
                "email": raw.get("email"),
                "role": raw.get("role"),
                "tenant_url": self.base_url,
            }

            # Valida contro il modello Pydantic
            users.append(User.model_validate(mapped))

        return users

    async def close(self):
        await self.client.aclose()
