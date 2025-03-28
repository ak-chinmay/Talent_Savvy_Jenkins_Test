# setup.py
from setuptools import setup, find_packages

setup(
    name="simple_calculator",
    version="0.1",
    packages=find_packages(),
    install_requires=[],
    author="ak.chinmay@gmail.com",
    author_email="your_email@example.com",
    description="A simple calculator package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourgithub/simple_calculator",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)