from setuptools import find_packages, setup

with open("./README.md", "r",encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="trgenpy", 
    version="1.0.0",
    description="## A Python library for Trgen Device",
    packages=find_packages(),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/b00leant/trgenpy",
    author="Stefano Latini",
    author_email="stefanoelatini@hotmail.it",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
    ],
    install_requires=["bson >= 0.5.10"],
    extras_require={
        "dev": ["pytest>=7.0", "twine>=4.0.2"],
    },
    python_requires=">=3.10",
)