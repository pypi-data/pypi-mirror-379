from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="pyredis_manager",
    version="0.1.2",
    author="jack-cizon",
    author_email="jack20021213cn@gmail.com",
    description="A lightweight Redis client manager with sync/async support",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jackcizon/pyredis_manager",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        "redis>=5.0.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
)
