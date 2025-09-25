
from setuptools import setup, find_packages

setup(
    name="MinNumberLib",
    version="0.1.0",
    description="Find the smallest number from a list",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Mohammed Abdo Aljamal",
    author_email="aljmal7722@gmail.com",
    packages=find_packages(),
    python_requires=">=3.7",
    license="MIT",
    entry_points={"console_scripts": ["minnumberlib=min_number_lib.__main__:main"]},
)
