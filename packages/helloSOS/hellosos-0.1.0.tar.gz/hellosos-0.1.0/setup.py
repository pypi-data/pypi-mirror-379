from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="helloSOS",
    version="0.1.0",
    author="Manny",
    author_email="contact@Manny.com",
    description="Kya be kya karlega jaan ke",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Manny",
    packages=find_packages(),  
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        "numpy",
        "pandas",
        "matplotlib",
    ],
)
