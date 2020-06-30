from setuptools import find_packages, setup

from src.meta import NAME, DESCRIPTION, VERSION, REPO_URL, DOCS_URL, AUTHOR, LICENSE

with open("README.md", "r") as fs:
    LONGE_DESCRIPTION = fs.read()

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONGE_DESCRIPTION,
    long_description_content_type="text/markdown",
    project_urls={"Documentation": DOCS_URL, "Source": REPO_URL},
    author=AUTHOR,
    author_email="decostakelvin@gmail.com",
    license=LICENSE,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        "Development Status :: 5 - Production/Stable",
        "Topic :: Artistic Software",
        "Topic :: Terminals",
        "Topic :: Utilities",
    ],
    packages=list(map(lambda x: x.replace("src", NAME), find_packages("."))),
    package_dir={NAME: "src"},
    package_data={"": ["data/*.txt"]},
    python_requires=">=3.8",
)
