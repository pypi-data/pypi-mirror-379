from setuptools import setup, find_packages
from setuptools.command.install import install
from os import path
import sys
import os

VERSION = "1.7.11.294"  # may include build metadata

# Strip build metadata for PyPI (keep only MAJOR.MINOR.PATCH)
PUBLISHED_VERSION = ".".join(VERSION.split(".")[:3])

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()


class VerifyVersionCommand(install):
    """Custom command to verify that the git tag matches our version"""

    description = "verify that the git tag matches our version"

    def run(self):
        tag = os.getenv("CIRCLE_TAG")

        # If no tag is set (local or non-tagged CircleCI build), skip
        if not tag:
            print("No CIRCLE_TAG set — skipping version check.")
            return

        # Enforce tag/version match when tag is present
        if tag != VERSION:
            info = f"Git tag: {tag} does not match the version of this app: {VERSION}"
            sys.exit(info)

        print(f"✔ Git tag {tag} matches version {VERSION}")


setup(
    name="Django_local_lib_pycon2025",
    version=VERSION,
    description="Local Django library packaged as a reusable app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/joseph-njogu/Django_local_lib",
    author="Joseph",
    author_email="josephnjogu487@gmail.com",
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Build Tools",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Internet",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3 :: Only",
    ],
    keywords="django local library",
    python_requires=">=3.6",
    install_requires=[
        "Django>=4.0",
    ],
    cmdclass={
        "verify": VerifyVersionCommand,
    },
    entry_points={
        "console_scripts": [
            # This generates a CLI command `locallib`
            # which points to your __main__.py:main()
            "locallib = cli:main",
        ],
    },
    packages=find_packages(),
    include_package_data=True,
)
