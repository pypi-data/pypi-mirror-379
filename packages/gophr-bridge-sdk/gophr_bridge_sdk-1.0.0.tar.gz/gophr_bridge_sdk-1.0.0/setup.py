from setuptools import setup, find_packages

# Read README for long description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="gophr-bridge-sdk",
    version="1.0.0",
    author="Gophr Inc.",
    author_email="engineering@gophr.com",
    description="A simple SDK for interacting with the Gophr Bridge API (Gophr customers only)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://bitbucket.org/gophrapp/gophr-bridge-py",
    project_urls={
        "Bug Tracker": "https://bitbucket.org/gophrapp/gophr-bridge-py/issues",
        "Repository": "https://bitbucket.org/gophrapp/gophr-bridge-py.git",
        "Documentation": "https://bitbucket.org/gophrapp/gophr-bridge-py#readme",
        "Sales": "https://gophr.com",
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: Other/Proprietary License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10", 
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Internet :: WWW/HTTP :: HTTP Servers",
        "Topic :: Office/Business",
    ],
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        "requests>=2.25.0",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0.0",
            "pytest-cov>=2.0.0",
            "pytest-mock>=3.0.0",
            "responses>=0.18.0",
            "black>=22.0.0",
            "flake8>=4.0.0",
            "mypy>=0.910",
            "python-dotenv>=0.19.0",
        ],
    },
    keywords="gophr delivery logistics api bridge shipping courier",
    include_package_data=True,

)
