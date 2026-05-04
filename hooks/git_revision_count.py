"""MkDocs hook to inject git revision count per page."""

import subprocess
from pathlib import Path


def on_page_context(context, page, config, nav):
    """Add git_revision_count to page meta for template use."""
    docs_dir = Path(config["docs_dir"])
    file_path = docs_dir / page.file.src_path

    if not file_path.exists():
        return context

    try:
        result = subprocess.run(
            ["git", "log", "--oneline", "--follow", "--", str(file_path)],
            capture_output=True,
            text=True,
            cwd=str(docs_dir),
            timeout=10,
        )
        if result.returncode == 0:
            count = len(result.stdout.strip().splitlines())
            context["git_revision_count"] = max(count, 1)
        else:
            context["git_revision_count"] = 1
    except Exception:
        context["git_revision_count"] = 1

    return context
