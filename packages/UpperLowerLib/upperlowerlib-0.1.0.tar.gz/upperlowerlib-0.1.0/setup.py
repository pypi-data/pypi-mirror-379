from setuptools import setup, find_packages 

setup(
    name="UpperLowerLib",
    version="0.1.0",
    description="Convert text to upper or lower case",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Amal Ahmed Mohammed Al-Sharif",
    author_email="alsharif5433@gmail.com",
    packages=find_packages(),
    python_requires=">=3.7",
    license="MIT",
    entry_points={"console_scripts": ["upperlowerlib=upper_lower_lib.__main__:main"]},
) 
