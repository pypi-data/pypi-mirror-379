from setuptools import setup, find_packages

setup(
    name="SquareRootLib",
    version="0.1.0",
    description="Calculate the square root of a number",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Your Name",
    author_email="you@example.com",
    packages=find_packages(),
    python_requires=">=3.7",
    license="MIT",
    entry_points={"console_scripts": ["squarerootlib=square_root_lib.__main__:main"]},
)