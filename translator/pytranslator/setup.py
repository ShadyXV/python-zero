import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="karkipytranslator",
    version="0.1.0",
    author="Aashish Karki",
    author_email="aashish.y2z@gmail.com",
    description="A language translator package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/karkipy/pytranslator",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
