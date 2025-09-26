from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Optional

from .api_client import APIClient
from .command import Command, CommandFinished
from .credentials import Credentials, get_credentials
from .models import (
    CommandResponse,
    Sandbox as SandboxModel,
    SandboxAndRoutesResponse,
)


@dataclass
class Sandbox:
    client: APIClient
    sandbox: SandboxModel
    routes: list[dict[str, Any]]

    @property
    def sandbox_id(self) -> str:
        return self.sandbox.id

    @property
    def status(self) -> str:
        return self.sandbox.status

    @staticmethod
    async def create(
        *,
        source: Optional[dict[str, Any]] = None,
        ports: Optional[list[int]] = None,
        timeout: Optional[int] = None,
        resources: Optional[dict[str, Any]] = None,
        runtime: Optional[str] = None,
        token: Optional[str] = None,
        project_id: Optional[str] = None,
        team_id: Optional[str] = None,
    ) -> "Sandbox":
        creds: Credentials = get_credentials(
            token=token, project_id=project_id, team_id=team_id
        )
        client = APIClient(team_id=creds.team_id, token=creds.token)
        resp: SandboxAndRoutesResponse = await client.create_sandbox(
            project_id=creds.project_id,
            source=source,
            ports=ports,
            timeout=timeout,
            resources=resources,
            runtime=runtime,
        )
        return Sandbox(
            client=client,
            sandbox=resp.sandbox,
            routes=[r.model_dump() for r in resp.routes],
        )

    @staticmethod
    async def get(
        *,
        sandbox_id: str,
        token: Optional[str] = None,
        project_id: Optional[str] = None,
        team_id: Optional[str] = None,
    ) -> "Sandbox":
        creds: Credentials = get_credentials(
            token=token, project_id=project_id, team_id=team_id
        )
        client = APIClient(team_id=creds.team_id, token=creds.token)
        resp: SandboxAndRoutesResponse = await client.get_sandbox(sandbox_id=sandbox_id)
        return Sandbox(
            client=client,
            sandbox=resp.sandbox,
            routes=[r.model_dump() for r in resp.routes],
        )

    def domain(self, port: int) -> str:
        for r in self.routes:
            if r.get("port") == port:
                # Prefer URL when provided by the API; fall back to subdomain
                return r.get("url") or f"https://{r['subdomain']}.vercel.run"
        raise ValueError(f"No route for port {port}")

    async def get_command(self, cmd_id: str) -> Command:
        resp = await self.client.get_command(sandbox_id=self.sandbox.id, cmd_id=cmd_id)
        assert isinstance(resp, CommandResponse)
        return Command(client=self.client, sandbox_id=self.sandbox.id, cmd=resp.command)

    async def run_command(
        self,
        cmd: str,
        args: Optional[list[str]] = None,
        *,
        cwd: Optional[str] = None,
        env: Optional[dict[str, str]] = None,
        sudo: bool = False,
    ) -> CommandFinished:
        command_response = await self.client.run_command(
            sandbox_id=self.sandbox.id,
            command=cmd,
            args=args or [],
            cwd=cwd,
            env=env or {},
            sudo=sudo,
        )
        command = Command(
            client=self.client, sandbox_id=self.sandbox.id, cmd=command_response.command
        )
        # Wait for completion
        return await command.wait()

    async def run_command_detached(
        self,
        cmd: str,
        args: Optional[list[str]] = None,
        *,
        cwd: Optional[str] = None,
        env: Optional[dict[str, str]] = None,
        sudo: bool = False,
    ) -> Command:
        command_response = await self.client.run_command(
            sandbox_id=self.sandbox.id,
            command=cmd,
            args=args or [],
            cwd=cwd,
            env=env or {},
            sudo=sudo,
        )
        return Command(
            client=self.client, sandbox_id=self.sandbox.id, cmd=command_response.command
        )

    async def mk_dir(self, path: str, *, cwd: Optional[str] = None) -> None:
        await self.client.mk_dir(sandbox_id=self.sandbox.id, path=path, cwd=cwd)

    async def read_file(
        self, path: str, *, cwd: Optional[str] = None
    ) -> Optional[bytes]:
        return await self.client.read_file(
            sandbox_id=self.sandbox.id, path=path, cwd=cwd
        )

    async def write_files(self, files: list[dict[str, bytes]]) -> None:
        await self.client.write_files(
            sandbox_id=self.sandbox.id,
            cwd=self.sandbox.cwd,
            extract_dir="/",
            files=files,
        )

    async def stop(self) -> None:
        await self.client.stop_sandbox(sandbox_id=self.sandbox.id)

    # Async context manager to ensure cleanup
    async def __aenter__(self) -> "Sandbox":
        return self

    async def __aexit__(self, exc_type, exc, tb) -> None:
        try:
            await self.stop()
        except Exception:
            # Best-effort stop; ignore errors during teardown
            pass
        await self.client.aclose()
