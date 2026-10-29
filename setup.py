"""Include the catalog and its runtime assets in installed distributions."""
from pathlib import Path
import shutil
from setuptools import setup
from setuptools.command.build_py import build_py

ROOT = Path(__file__).resolve().parent
ASSETS = ("catalog.json", "source-catalog.json", "source-omex-catalog.json",
          "LICENSE", "NOTICE", "SOURCE_NOTICE.md", "models", "sources",
          "scripts/model_summaries.json")


class BuildLibrary(build_py):
    def run(self):
        super().run()
        destination = Path(self.build_lib) / "qspquest_models" / "_library"
        for name in ASSETS:
            source = ROOT / name
            paths = sorted(source.rglob("*")) if source.is_dir() else [source]
            for path in paths:
                if path.is_symlink():
                    raise ValueError("Library assets must be regular files")
                if path.is_file() and path.name != ".DS_Store" and "__pycache__" not in path.parts:
                    target = destination / path.relative_to(ROOT)
                    target.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copyfile(path, target)


setup(cmdclass={"build_py": BuildLibrary})
