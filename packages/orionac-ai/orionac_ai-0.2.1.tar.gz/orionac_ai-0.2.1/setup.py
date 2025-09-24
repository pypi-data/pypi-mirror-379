from setuptools import setup, find_packages

setup(
    name="orionac-ai",
    version="0.2.1",
    author="Zakaria",
    author_email="rishi@orionac.in",
    description="Python client for Orionac AI API",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/RishiR123/orionac-ai",
    packages=find_packages(),
    python_requires=">=3.10",
    install_requires=[
        "requests>=2.28"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
