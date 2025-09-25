from setuptools import setup, find_packages

setup(
    name="superweather",
    version="0.4",
    packages=find_packages(),  
    install_requires=[
        "requests",
        "pyttsx3",
    ],
    entry_points={
        "console_scripts": [
            "superweather=superweather.superweather:terminal_mode",
        ],
    },
    author="Mohammad Shabakhti",
    author_email="smmshabakhti@gmail.com",
    url="https://github.com/shabakhti",
    description="A package to fetch and display air quality data.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
