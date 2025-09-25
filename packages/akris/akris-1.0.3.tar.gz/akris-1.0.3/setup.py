from setuptools import setup, find_packages

setup(
    name="akris",
    version="1.0.3",
    description="A pest implementation",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Adam Thorsen",
    author_email="awt@fastmail.fm",
    url="http://alethepedia.com/akris",
    license="VPL",
    packages=find_packages(),
    install_requires=["cffi", "setuptools"],
    setup_requires=["cffi"],
    cffi_modules=["akris/c_serpent/serpent_build.py:ffibuilder"],
    extras_require={
        "dev": [
            "black",
            "pytest",
            "pylint",
            "pyinstaller",
            "staticx",
            "markdown2"
        ]
    },
    package_data={"akris": ["migrations/*.py", "VERSION", "c_serpent/*.h", "c_serpent/*.c", "c_serpent/lib/*.c", "c_serpent/lib/*.h"]},
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "akris=akris.main:main",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: Other/Proprietary License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
    ],
    keywords="p2p pest chat",
    python_requires=">=3.6",
    zip_safe=False,
)
