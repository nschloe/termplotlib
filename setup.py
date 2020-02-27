import os

from setuptools import find_packages, setup

# https://packaging.python.org/single_source_version/
base_dir = os.path.abspath(os.path.dirname(__file__))
about = {}
with open(os.path.join(base_dir, "termplotlib", "__about__.py"), "rb") as f:
    exec(f.read(), about)


setup(
    name="termplotlib",
    version=about["__version__"],
    packages=find_packages(),
    url="https://github.com/nschloe/termplotlib",
    author=about["__author__"],
    author_email=about["__email__"],
    install_requires=[],
    description="Plotting on the command line",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    license=about["__license__"],
    python_requires=">=3.5",
    classifiers=[
        about["__license__"],
        about["__status__"],
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Topic :: System :: Shells",
        "Topic :: Multimedia :: Graphics",
    ],
)
