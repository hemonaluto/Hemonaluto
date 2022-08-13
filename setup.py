import pathlib
import os
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

def package_files(directory):
    paths = []
    for (path, directories, filenames) in os.walk(directory):
        for filename in filenames:
            paths.append(os.path.join('..', path, filename))
    return paths

extra_files = package_files('game/data')

setup(
    install_requires=["parameterized==0.8.1"],
    name = "hemonaluto",
    version = "0.0.1",
    author = "Gabriel Schafflützel",
    author_email = "schaffluetzel.gabriel@gmail.com",
    description = ("A text adventure game!"),
    license = "GNU General Public License v3.0",
    keywords = "text-based adventure game",
    url = "https://github.com/hemonaluto/Hemonaluto",
    long_description=README,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    include_package_data=True,
    package_data={"": extra_files},
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Topic :: Games/Entertainment",
        "Environment :: Console",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
    python_requires=">=3.8",
    entry_points={"console_scripts": ["hemonaluto=game.runner:run", ], },
)
