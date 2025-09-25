from setuptools import setup, find_packages

setup(
    name="DateTimeLib",
    version="0.1.0",
    description="Library to get current date and time",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Adel Amin Alashmouri",
    author_email="ashmouri12ty@gmail.com",
    packages=find_packages(),
    python_requires=">=3.7",
    license="MIT",
    entry_points={
        "console_scripts": [
            "datetimelib=datetime_lib.__main__:main"
        ]
    },
)
