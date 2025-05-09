import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="metaimg",
    version="0.0.1",
    author="Sidharth S",
    author_email="sidharth.tradis@gmail.com",
    description="A package to read metadata of images and create clean copies",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Sidharth-S/metaimg",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)