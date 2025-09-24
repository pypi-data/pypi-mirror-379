from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="LibGram",
    version="1.1.1",
    author="GramLib Team",
    author_email="gramlib@telegram.com",
    description="Simple and powerful data management library with decorators",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    keywords="database, async, decorators, simple, json, gram",
    url="https://github.com/yourusername/gramlib",
    project_urls={
        "Bug Reports": "https://github.com/yourusername/gramlib/issues",
        "Source": "https://github.com/yourusername/gramlib",
    },
)
