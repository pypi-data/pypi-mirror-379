from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="oytel-esim-sdk",
    version="1.0.0",
    author="Oytel Mobile",
    author_email="developers@oytel.co.uk",
    description="Official Oytel eSIM API SDK for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/oytel/esim-sdk-python",
    project_urls={
        "Documentation": "https://oytel.co.uk/developers",
        "Developer Dashboard": "https://oytel.co.uk/developers/dashboard",
        "Bug Tracker": "https://github.com/oytel/esim-sdk-python/issues",
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Communications",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    packages=find_packages(),
    python_requires=">=3.7",
    install_requires=[
        "requests>=2.25.0",
        "typing-extensions>=4.0.0; python_version<'3.8'",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov",
            "black",
            "flake8",
            "mypy",
            "responses",
        ],
    },
    keywords="esim oytel mobile connectivity api sdk",
)
