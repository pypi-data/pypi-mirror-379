from setuptools import setup, find_packages

setup(
    name="sea-cli",
    version="0.1.1",
    author="Ezekiel Edward Netty-Oppong & Per Badasu",
    author_email="cyril.davif@gmail.com",
    description="A command-line utility for Structured Entropy Analysis (SEA)",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/cyril-pierro/sea-cli",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Topic :: Scientific/Engineering",
    ],
    python_requires=">=3.6",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "numpy", "scipy", "scikit-learn", "matplotlib", "click", "pyyaml"
    ],
    entry_points={
        "console_scripts": [
            "sea=sea_cli.cli:main",
        ],
    },
)
