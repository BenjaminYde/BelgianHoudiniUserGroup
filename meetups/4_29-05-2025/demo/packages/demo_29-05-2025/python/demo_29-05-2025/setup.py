from pathlib import Path
import setuptools

current_folder: Path = Path(__file__).parent
name: str = current_folder.name
version: str = "0.1.0"

setuptools.setup(
    name=name,
    version=version,
    packages=setuptools.find_packages(exclude=["tests"])
)