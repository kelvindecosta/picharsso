from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name="image-to-text-art",
    version="1.0",
    description="A command line utility to convert an image to text art.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kelvindecosta/image-to-text-art",
    author="Kelvin DeCosta",
    author_email="decostakelvin@gmail.com",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    packages=find_packages("src"),
    package_dir={"" : "src"},
    package_data={
        "" : ["*.json"]
    },
    install_requires=[
        "opencv-python",
        "sty"
    ],
    entry_points={
        "console_scripts": [
            "img2txt = image_to_text_art.__main__:main",
        ]
    },
)