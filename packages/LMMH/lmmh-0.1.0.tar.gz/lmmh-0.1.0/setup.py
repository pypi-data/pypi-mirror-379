from setuptools import setup, find_packages

setup(
    name="LMMH",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "LMMH-setup=LMMH.app:main",  # optional: run as CLI command
        ],
    },
    author="LaithALhaware",
    author_email="www.landr41@gmail.com",
    description="👽 LMMH Library - Text Model Training setup dashboard",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/LaithALhaware/LMMH-AI",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)

