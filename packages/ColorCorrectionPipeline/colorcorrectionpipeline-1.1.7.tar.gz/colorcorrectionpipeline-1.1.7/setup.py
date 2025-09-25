import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Define requirements directly to avoid build issues
requirements = [
    "opencv-python",
    "opencv-contrib-python", 
    "scikit-learn",
    "scipy",
    "numpy",
    "torch",
    "ultralytics",
    "scikit-image",
    "plotly",
    "matplotlib",
    "pandas",
    "statsmodels",
    "seaborn",
    "colour-science",
    "colour-checker-detection"
]

setuptools.setup(
    name="ColorCorrectionPipeline",
    version="1.1.7",
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