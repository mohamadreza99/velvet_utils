from pathlib import Path
import shutil


def empty_dir(p:Path):
    shutil.rmtree(p)
    p.mkdir(parents=True, exist_ok=True)