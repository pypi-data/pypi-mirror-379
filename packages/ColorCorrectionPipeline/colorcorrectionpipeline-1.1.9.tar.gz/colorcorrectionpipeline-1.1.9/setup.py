import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.readlines()

setuptools.setup(
    name="ColorCorrectionPipeline",
    version="1.1.9",
    author="Collins Wakholi, Devin A. Rippner",
    author_email="wcoln@yahoo.com, devinrippner@gmail.com",
    description="A Stepwise color‐correction pipeline with flat‐field, gamma, white‐balance, and color‐correction stages.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/collinswakholi/ColorCorrectionPackage",
    project_urls={
        "Bug Tracker": "https://github.com/collinswakholi/ColorCorrectionPackage/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords=["color", "image-processing", "flat-field", "gamma-correction", "white-balance", "color-correction"],
    packages=setuptools.find_packages(), # Automatically finds packages in 'src/'
    python_requires=">=3.8",
    install_requires=requirements,
    include_package_data=True
)