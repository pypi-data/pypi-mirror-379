from setuptools import setup, find_packages

setup(
    name="pynexitec",
    version="0.1.2",
    description="A mini terminal game package with Tic-Tac-Toe",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Aayush B",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/pynexitec",  # optional
    packages=find_packages(),
    python_requires=">=3.7",
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
