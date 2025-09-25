from setuptools import setup, find_packages

setup(
    name="emojify-asid",
    version="0.1.0",
    description="A smart text emojifier",
    author="Your Name",
    packages=find_packages(),
    install_requires=[
        # "spacy>=3.0.0",
    ],
    entry_points={
        "console_scripts": [
            "emojify=emojify.core:emojify_text"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
)