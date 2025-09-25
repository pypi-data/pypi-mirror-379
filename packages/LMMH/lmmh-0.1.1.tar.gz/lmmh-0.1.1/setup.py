from setuptools import setup, find_packages

setup(
    name="LMMH",
    version="0.1.1",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "LMMH-setup=LMMH.app:main",  # optional: run as CLI command
        ],
    },
    author="Laith Madhat M. AL-Haware",
    author_email="www.landr41@gmail.com",
    description="👽 LMMH - Comprehensive Library of AI",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/LaithALhaware",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)

