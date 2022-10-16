import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()


def _requires_from_file(filename):
    return open(filename, encoding="utf8").read().splitlines()


def _get_version(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
    version = None
    for line in lines:
        if "__version__" in line:
            version = line.split()[2]
            break
    return version.replace('"', '')


extras_require = {
    "async": [
        "aiohttp>=3.8.1"
    ]
}

setuptools.setup(
    name="google-custom-search",
    version=_get_version("google_custom_search/__init__.py"),
    author="mc-fdc-dev",
    author_email="masato190411@gmail.com",
    description="This is for google custom search api.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mc-fdc-dev/google-custom-search",
    install_requires=_requires_from_file('requirements.txt'),
    extras_require=extras_require,
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
