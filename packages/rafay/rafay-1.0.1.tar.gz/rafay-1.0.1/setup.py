from setuptools import setup, find_packages

setup(
    name="rafay",
    version="1.0.1",
    author="Muhammad Rafay Shaikh",
    author_email="datascience.youexcel@gmail.com",
    description="simple package",
    pakages=find_packages(),
    python_requires=">=3.6",
    entry_point={
        "console_scripts" : [
            "rafay=rafay.rafay:main"
        ],
    },
)