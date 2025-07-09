import os
from pathlib import Path
from typing import Union, List

def dir_ensure(paths: Union[str, List[str]]) -> List[Path]:
    """
    Ensure that one or more directories exist. Create them if they do not.

    Parameters:
    - paths: A single path or a list of paths (str or Path)

    Returns:
    - List of Path objects that were checked/created.
    """
    if isinstance(paths, (str, Path)):
        paths = [paths]
    elif not isinstance(paths, (list, tuple)):
        raise TypeError("`paths` must be a string, Path, or list of strings/Paths.")

    created_paths = []

    for p in paths:
        path = Path(p).expanduser().resolve()
        try:
            if not path.exists():
                path.mkdir(parents=True, exist_ok=True)
                print(f"📁 Directory created: {path}")
            else:
                print(f"✅ Directory already exists: {path}")
            created_paths.append(path)
        except Exception as e:
            print(f"⚠️ Failed to create directory: {path} — {e}")

    return created_paths

