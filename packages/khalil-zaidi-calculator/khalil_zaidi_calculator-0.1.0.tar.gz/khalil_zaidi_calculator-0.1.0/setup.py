from setuptools import setup, find_packages

setup(
    name="khalil-zaidi-calculator",
    version="0.1.0",
    author="خليل الزايدي",
    author_email="your_email@example.com",
    description="Advanced calculator with extra math operations",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/khalil-zaidi-calculator",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
