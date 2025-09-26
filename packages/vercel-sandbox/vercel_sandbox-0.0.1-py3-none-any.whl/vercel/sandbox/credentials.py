from __future__ import annotations

import os
from dataclasses import dataclass
import base64
import json
from typing import Optional


@dataclass
class Credentials:
    token: str
    project_id: str
    team_id: str


def get_credentials(
    *,
    token: Optional[str] = None,
    project_id: Optional[str] = None,
    team_id: Optional[str] = None,
) -> Credentials:
    if token and project_id and team_id:
        return Credentials(token=token, project_id=project_id, team_id=team_id)

    oidc = os.getenv("VERCEL_OIDC_TOKEN")
    if oidc:
        project = os.getenv("VERCEL_PROJECT_ID")
        team = os.getenv("VERCEL_TEAM_ID")
        if not (project and team):
            # Try to decode JWT payload to extract project_id and owner_id
            try:
                payload_b64 = oidc.split(".")[1]
                padded = payload_b64 + "=" * (-len(payload_b64) % 4)
                raw = base64.urlsafe_b64decode(padded)
                payload = json.loads(raw.decode("utf-8"))
                project = payload.get("project_id")
                team = payload.get("owner_id")
            except Exception:
                pass
        if project and team:
            return Credentials(token=oidc, project_id=project, team_id=team)
        raise RuntimeError(
            "VERCEL_OIDC_TOKEN present but could not determine VERCEL_PROJECT_ID and VERCEL_TEAM_ID"
        )

    token = token or os.getenv("VERCEL_TOKEN")
    project_id = project_id or os.getenv("VERCEL_PROJECT_ID")
    team_id = team_id or os.getenv("VERCEL_TEAM_ID")

    if token and project_id and team_id:
        return Credentials(token=token, project_id=project_id, team_id=team_id)

    raise RuntimeError(
        "Missing credentials. Provide VERCEL_OIDC_TOKEN with VERCEL_PROJECT_ID and VERCEL_TEAM_ID, "
        "or VERCEL_TOKEN, VERCEL_PROJECT_ID, VERCEL_TEAM_ID."
    )
