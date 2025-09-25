from setuptools import setup, find_packages

setup(
    name="RangeNumbersSumLibrary",
    version="0.1.0",
    description="Calculate sum of numbers in a range from a to b",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Suhail Nabil Alansi",
    author_email="suhail09t12@gmail.com",
    packages=find_packages(),
    python_requires=">=3.7",
    license="MIT",
    entry_points={"console_scripts": ["rangesumnumbers=range_numbers_sum_lib.__main__:main"]},
)
