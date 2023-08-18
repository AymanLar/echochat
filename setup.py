from setuptools import setup, find_packages

VERSION ='0.1.0'

with open("README.md", encoding="UTF-8") as file:
    readme = file.read()

with open("requirements.txt", "r", encoding="utf-8") as file:
    requirements = [line.strip() for line in file]

setup(
    name='EchoChat',
    description="EchoChat CLI tool that simulates conversations with historical figures",
    version=VERSION,
    packages=find_packages(),
    install_requires=requirements,  # Add any dependencies here
    entry_points={
        "console_scripts": [
        "echochat = echochat.cli:echochat",
        ]
    },
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Ayman Lar"
)