from setuptools import setup, find_packages

setup(
    name="akris-desktop",
    version="1.0.1",
    description="A gui client for akris",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Adam Thorsen",
    author_email="awt@fastmail.fm",
    url="http://v.alethepedia.com/akris_desktop",
    license="VPL",
    packages=find_packages(),
    install_requires=["Pillow", "akris"],
    extras_require={
        "dev": [
            "black",
            "pytest",
            "pytest-mock",
            "autopep8",
            "pyinstaller",
            "markdown2",
            "staticx",
            "pylint",
        ]
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
    ],
    keywords="p2p pest forum",
    python_requires=">=3.11",
    entry_points={
        "console_scripts": [
            "akris-desktop=akris_desktop.main:main",
        ],
    },
)
