from setuptools import setup, find_packages 

setup(
    name="WordCountLibRS",
    version="0.1.0",
    description="Count words in a text",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Roiuda Sharaf Abutaleb",
    author_email="abutaleb09n@gmail.com",
    packages=find_packages(),
    python_requires=">=3.7",
    license="MIT",
    entry_points={"console_scripts": ["wordcountrs=word_count_lib.__main__:main"]},
) 
