from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="python-roblox-cloud",
    version="0.1.1",     # ↑ увеличь версию, например 0.1.1
    description="Unofficial Roblox Cloud API wrapper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="G3tFun",
    author_email="",
    packages=find_packages(),
    install_requires=["requests"],
    python_requires=">=3.7",
)