from setuptools import setup, find_packages

setup(
    name="rusty-tags",
    version="0.1.0",
    packages=find_packages(),
    python_requires=">=3.10",
    author="Nikola Dendic",
    description="High-performance HTML generation library",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ndendic/rusty-tags",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
)
