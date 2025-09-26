from setuptools import setup, find_packages

setup(
    name="dekho-cli",
    version="1.0.2",
    packages=find_packages(),
    install_requires=["requests"],
    entry_points={
        "console_scripts": [
            "dekho-cli = dekho_cli.main:main"
        ]
    },
    author="dev1abhi",
    author_email="opguddu21@gmail.com",
    description="CLI tool to fetch and play sports channels via mpv.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    license="MIT",
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
