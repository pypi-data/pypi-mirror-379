from __future__ import annotations

import json
from pathlib import Path

from imagemcp import ProjectPaths
from imagemcp.cli import main as cli_main
from imagemcp.storage import load_manifest


def test_cli_generate_and_select(tmp_path, capsys):
    project_root = tmp_path
    target_root = "assets"
    exit_code = cli_main(
        [
            "--project-root",
            str(project_root),
            "gen",
            "--slot",
            "hero",
            "--target-root",
            target_root,
            "--prompt",
            "Warm hero section illustration",
            "--generator",
            "mock",
            "--n",
            "2",
            "--json",
        ]
    )
    assert exit_code == 0
    first_output = json.loads(capsys.readouterr().out)
    session_id = first_output["sessionId"]
    assert first_output["galleryUrl"].startswith("http://")

    config_path = project_root / ".imagemcp" / "config.json"
    assert config_path.exists()
    config_data = json.loads(config_path.read_text("utf-8"))
    assert config_data["targetRoot"] == target_root

    target_path = project_root / target_root / "hero.png"
    assert target_path.exists()

    session_dir = project_root / target_root / ".sessions" / f"hero_{session_id}"
    manifest_path = session_dir / "session.json"
    assert manifest_path.exists()

    manifest_data = json.loads(manifest_path.read_text("utf-8"))
    assert manifest_data["selectedIndex"] == 0
    assert len(manifest_data["history"]) == 1

    capsys.readouterr()  # Clear buffers
    exit_code = cli_main(
        [
            "--project-root",
            str(project_root),
            "select",
            "--target-root",
            target_root,
            "--slot",
            "hero",
            "--session",
            session_id,
            "--index",
            "1",
            "--json",
        ]
    )
    assert exit_code == 0
    second_output = json.loads(capsys.readouterr().out)
    assert second_output["selectedIndex"] == 1

    paths = ProjectPaths.create(Path(project_root), Path(target_root))
    manager_manifest = load_manifest(paths.manifest_path(session_dir))
    assert manager_manifest.selected_index == 1
    assert len(manager_manifest.history) == 2
