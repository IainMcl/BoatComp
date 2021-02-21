# python setup.py build
# python setup.py install
# pip install -e .
# pip install -e .[dev]

from setuptools import setup


class Person():
    def __init__(self, fname: str, sname: str, email: str, role: list[str]):
        self.name = f"{fname} {sname}"
        self.email = email
        self.role = role


aut = Person("Iain", "McLaughaln",
             "SailingExercises@gmail.com", ["aut", "men"])

with open("README.rst", "r") as fh:
    long_description = fh.read()

with open("requirements.txt") as f:
    required = f.read().splitlines()

with open("requirements-dev.txt") as f:
    required_dev = f.read().splitlines()

with open("requirements-docs.txt") as f:
    required_doc = f.read().splitlines()

setup(
    name="boatcomp",
    version="0.0.1",
    description="Boat computer for yacht racing.",
    author=aut.name,
    author_email=aut.email,
    maintainer=aut.name,
    maintainer_email=aut.email,
    url="https://github.com/IainMcl/BoatComp",
    packages=[
        "api",
        "database",
        "models",
    ],
    py_modules=[
        "settings",
    ],
    package_dir={"": "src"},
    license="Apache",
    classifiers=[
        "Programming Language :: Python 3",
        "Programming Language :: Python 3.9",
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=required,
    extras_require={
        "dev": required_dev,
        "doc": required_doc,
    },
    keywords=[
        "python",
        "sailing",
        "racing",
        "tactics",
        "tactic",
        "timer"
    ]
)
