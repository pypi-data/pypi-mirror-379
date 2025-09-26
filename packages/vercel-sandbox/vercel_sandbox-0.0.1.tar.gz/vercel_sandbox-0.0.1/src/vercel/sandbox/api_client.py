from __future__ import annotations

from typing import Any, AsyncGenerator, Optional

from .base_client import BaseClient
from .models import (
    CommandFinishedResponse,
    CommandResponse,
    LogLine,
    SandboxAndRoutesResponse,
    SandboxResponse,
)


USER_AGENT = "vercel/sandbox-python/0.1.0"


class APIClient(BaseClient):
    def __init__(
        self, *, host: str = "https://api.vercel.com", team_id: str, token: str
    ):
        super().__init__(host=host, token=token)
        self._team_id = team_id

    async def request(self, method: str, path: str, **kwargs):
        headers = kwargs.pop("headers", {})
        headers = {
            "user-agent": USER_AGENT,
            **headers,
        }
        query = kwargs.pop("query", {})
        query = {"teamId": self._team_id, **(query or {})}
        return await super().request(
            method, path, headers=headers, query=query, **kwargs
        )

    async def request_json(self, method: str, path: str, **kwargs):
        r = await self.request(method, path, **kwargs)
        return r.json()

    async def create_sandbox(
        self,
        *,
        project_id: str,
        ports: Optional[list[int]] = None,
        source: Optional[dict[str, Any]] = None,
        timeout: Optional[int] = None,
        resources: Optional[dict[str, Any]] = None,
        runtime: Optional[str] = None,
    ) -> SandboxAndRoutesResponse:
        # Build body with only provided values to avoid sending nulls
        body: dict[str, Any] = {"projectId": project_id}
        if ports:
            body["ports"] = ports
        if source is not None:
            body["source"] = source
        if timeout is not None:
            body["timeout"] = timeout
        if resources is not None:
            body["resources"] = resources
        if runtime is not None:
            body["runtime"] = runtime

        data = await self.request_json("POST", "/v1/sandboxes", json_body=body)
        return SandboxAndRoutesResponse.model_validate(data)

    async def get_sandbox(self, *, sandbox_id: str) -> SandboxAndRoutesResponse:
        data = await self.request_json("GET", f"/v1/sandboxes/{sandbox_id}")
        return SandboxAndRoutesResponse.model_validate(data)

    async def run_command(
        self,
        *,
        sandbox_id: str,
        command: str,
        args: list[str],
        cwd: Optional[str] = None,
        env: Optional[dict[str, str]] = None,
        sudo: bool = False,
    ) -> CommandResponse:
        body: dict[str, Any] = {
            "command": command,
            "args": args,
            "env": env or {},
            "sudo": sudo,
        }
        if cwd is not None:
            body["cwd"] = cwd
        data = await self.request_json(
            "POST",
            f"/v1/sandboxes/{sandbox_id}/cmd",
            json_body=body,
        )
        return CommandResponse.model_validate(data)

    async def get_command(
        self, *, sandbox_id: str, cmd_id: str, wait: bool = False
    ) -> CommandResponse | CommandFinishedResponse:
        data = await self.request_json(
            "GET",
            f"/v1/sandboxes/{sandbox_id}/cmd/{cmd_id}",
            query={"wait": "true"} if wait else None,
        )
        if wait:
            return CommandFinishedResponse.model_validate(data)
        return CommandResponse.model_validate(data)

    async def get_logs(
        self, *, sandbox_id: str, cmd_id: str
    ) -> AsyncGenerator[LogLine, None]:
        async with self._client.stream(
            "GET",
            f"/v1/sandboxes/{sandbox_id}/cmd/{cmd_id}/logs",
            params={"teamId": self._team_id},
            headers={
                "user-agent": USER_AGENT,
                "authorization": f"Bearer {self._token}",
                "accept": "text/event-stream",
            },
        ) as resp:
            resp.raise_for_status()
            async for line in resp.aiter_lines():
                if not line:
                    continue
                try:
                    yield LogLine.model_validate_json(line)
                except Exception:
                    continue

    async def stop_sandbox(self, *, sandbox_id: str) -> SandboxResponse:
        data = await self.request_json("POST", f"/v1/sandboxes/{sandbox_id}/stop")
        return SandboxResponse.model_validate(data)

    async def mk_dir(
        self, *, sandbox_id: str, path: str, cwd: Optional[str] = None
    ) -> None:
        body: dict[str, Any] = {"path": path}
        if cwd is not None:
            body["cwd"] = cwd
        await self.request_json(
            "POST",
            f"/v1/sandboxes/{sandbox_id}/fs/mkdir",
            json_body=body,
        )

    async def read_file(
        self, *, sandbox_id: str, path: str, cwd: Optional[str] = None
    ) -> Optional[bytes]:
        body: dict[str, Any] = {"path": path}
        if cwd is not None:
            body["cwd"] = cwd
        resp = await self.request(
            "POST",
            f"/v1/sandboxes/{sandbox_id}/fs/read",
            json_body=body,
        )
        if resp.status_code == 404 or resp.content is None:
            return None
        return resp.content

    async def write_files(
        self,
        *,
        sandbox_id: str,
        files: list[dict[str, bytes]],
        extract_dir: str,
        cwd: str,
    ) -> None:
        import io
        import posixpath
        import tarfile

        def normalize_path(file_path: str) -> str:
            # Mirror TS normalizePath: basePath is absolute path. If relative, resolve against cwd.
            base_path = (
                posixpath.normpath(file_path)
                if posixpath.isabs(file_path)
                else posixpath.normpath(posixpath.join(cwd, file_path))
            )
            # Return path relative to extract_dir
            return posixpath.relpath(base_path, extract_dir)

        buffer = io.BytesIO()
        with tarfile.open(fileobj=buffer, mode="w:gz") as tar:
            for f in files:
                data = f["content"]
                rel = normalize_path(f["path"])  # e.g., vercel/sandbox/foo.txt
                info = tarfile.TarInfo(name=rel)
                info.size = len(data)
                tar.addfile(info, io.BytesIO(data))

        payload = buffer.getvalue()
        r = await self._client.request(
            "POST",
            f"/v1/sandboxes/{sandbox_id}/fs/write",
            params={"teamId": self._team_id},
            headers={
                "content-type": "application/gzip",
                "x-cwd": extract_dir,
                "user-agent": USER_AGENT,
                "authorization": f"Bearer {self._token}",
            },
            content=payload,
        )
        r.raise_for_status()

    async def kill_command(
        self, *, sandbox_id: str, command_id: str, signal: int = 15
    ) -> None:
        r = await self._client.request(
            "POST",
            f"/v1/sandboxes/{sandbox_id}/cmd/{command_id}/kill",
            params={"teamId": self._team_id},
            headers={"user-agent": USER_AGENT},
            json={"signal": signal},
        )
        r.raise_for_status()
