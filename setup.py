# python setup.py bdist_wheel
# python setup.py sdist
# pip install -e .
# pip install -e .[dev]

from setuptools import setup


class Person():
    def __init__(self, fname: str, sname: str, email: str, role):
        self.name = f"{fname} {sname}"
        self.email = email
        self.role = role


aut = Person("Iain", "McLaughaln",
             "SailingExercises@gmail.com", ["aut", "men"])

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="boatcomp",
    version="0.0.1",
    description="Boat computer for yacht racing.",
    author=aut.name,
    author_email=aut.email,
    maintainer=aut.name,
    maintainer_email=aut.email,
    url="https://github.com/IainMcl/BoatComp",
    py_modules=[
        "db_setup",
    ],
    package_dir={"": "src"},
    license="Apache",
    classifiers=[
        "Programming Language :: Python 3",
        "Programming Language :: Python 3.8",
        "Programming Language :: Python 3.7",
        "Programming Language :: Python 3.6",
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        "python-decouple>=3.4"
    ],
    extras_require={
        "dev": [
            "pytest>=6.2",
            "tox",
        ],
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
