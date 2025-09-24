from setuptools import find_packages, setup

# Read the contents of README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


# Read the version from the package
def get_version():
    import re

    version_dict = {}
    with open("jhlogger/__init__.py", "r") as fp:
        content = fp.read()

    # Use regex to extract version variables, handling multi-line assignments
    patterns = {
        "__version__": r'__version__\s*=\s*["\']([^"\']+)["\']',
        "__author__": r'__author__\s*=\s*["\']([^"\']+)["\']',
        "__email__": r'__email__\s*=\s*["\']([^"\']+)["\']',
        "__description__": r'__description__\s*=\s*["\']([^"\']+)["\']',
    }

    for key, pattern in patterns.items():
        match = re.search(pattern, content, re.MULTILINE | re.DOTALL)
        if match:
            version_dict[key] = match.group(1)

    return version_dict


version_info = get_version()

setup(
    name="jhlogger",
    version=version_info["__version__"],
    author=version_info["__author__"],
    author_email=version_info["__email__"],
    description=version_info["__description__"],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Jacaranda-Health/jhlogger",
    project_urls={
        "Bug Tracker": ("https://github.com/Jacaranda-Health/jhlogger/issues"),
        "Documentation": ("https://github.com/Jacaranda-Health/jhlogger/blob/main/README.md"),
        "Source Code": "https://github.com/Jacaranda-Health/jhlogger",
    },
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Logging",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "structlog>=23.0.0",
        "watchtower>=3.0.0",
        "sentry-sdk>=1.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "black>=22.0.0",
            "flake8>=5.0.0",
            "mypy>=1.0.0",
            "pre-commit>=2.20.0",
        ],
        "docs": [
            "sphinx>=5.0.0",
            "sphinx-rtd-theme>=1.0.0",
        ],
    },
    keywords=[
        "logging",
        "json",
        "structured",
        "cloudwatch",
        "sentry",
        "configurable",
        "traceback",
        "debug",
        "monitoring",
    ],
    include_package_data=True,
    zip_safe=False,
)
