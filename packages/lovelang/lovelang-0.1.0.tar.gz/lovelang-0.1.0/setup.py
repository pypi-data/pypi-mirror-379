from setuptools import setup

setup(
    name="lovelang",
    version="0.1.0",
    py_modules=["lovelang"],
    entry_points={
        "console_scripts": [
            "lovelang=lovelang:main",
        ],
    },
    install_requires=[],
    python_requires=">=3.8",
    description=" LoveLang - A Hinglish-based programming language",
    author="Gourahari",
    author_email="",
    url="https://github.com/CodeGoura/lovelang",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
