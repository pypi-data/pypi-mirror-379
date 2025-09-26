from setuptools import setup, find_packages

setup(
    name="CharFrequencyLib",
    version="0.1.0",
    description="Calculate character frequency in text",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Ashjan Walid Alakhaly",
    author_email="alakhaly58@gmail.com",
    packages=find_packages(),
    python_requires=">=3.7",
    license="MIT",
    entry_points={"console_scripts": ["charfrequencylib=char_frequency_lib.__main__:main"]},
)
