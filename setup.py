from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()


setup(
    name="br-lottery-simulation",
    version="0.0.10",
    author="richard_oliveira",
    author_email="doomsdayst9@gmail.com",
    description="brazilian lottery game simulation",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rd-oliveira/br-lottery-simulation",
    packages=find_packages(),
    python_requires=">=3.10",
)
