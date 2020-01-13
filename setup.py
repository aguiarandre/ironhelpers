from setuptools import setup

setup(
    author="IronHack",
    author_email="andre.aguiar@ironhack.com",
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
    description="IronHack library for Python",
    install_requires=["termcolor"],
    keywords="IronHack",
    name="ironhack",
    package_dir={"": "src"},
    packages=["ironhelpers"],
    url="https://github.com/aguiarandre/ironhelpers",
    version="0.0.1"
)
