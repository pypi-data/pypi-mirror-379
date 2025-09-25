from setuptools import setup, find_packages

setup(
    name="keyauth_renee",
    version="0.2.0",
    description="FastAPI-compatible API key validator client",
    author="Renee",
    license="MIT",
    packages=find_packages(),
    install_requires=["requests"],
    include_package_data=True,
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Caseymaill/keyauth_renee",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Framework :: FastAPI",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)