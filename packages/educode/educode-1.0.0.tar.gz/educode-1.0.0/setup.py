# setup.py
"""Setup script pour publier EduCode sur PyPI"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="educode",
    version="1.0.0", 
    author="Mohamed Ndiaye",
    author_email="mintok2000@gmail.com",
    description="Système interactif de 100 exercices pour apprendre Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Moesthetics-code/educode",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Education",
        "Intended Audience :: Developers", 
        "Topic :: Education",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    keywords="education, python, exercises, learning, programming, tutorial, practice",
    python_requires=">=3.6",
    install_requires=[
        # Aucune dépendance externe - pur Python stdlib
    ],
    entry_points={
        "console_scripts": [
            "educode=educode.__main__:main",
        ],
    },
    project_urls={
        "Bug Reports": "https://github.com/Moesthetics-code/educode/issues",
        "Source": "https://github.com/Moesthetics-code/educode",
        "Documentation": "https://educode.readthedocs.io/",
    },
)
