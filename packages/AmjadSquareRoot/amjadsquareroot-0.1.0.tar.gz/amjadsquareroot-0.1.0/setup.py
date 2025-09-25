from setuptools import setup, find_packages

setup(
    name="AmjadSquareRoot",
    version="0.1.0",
    description="Calculate the square root of a number",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Amjad Sameer Alnamer",
    author_email="aalnmr392@gmail.com",
    packages=find_packages(),
    python_requires=">=3.7",
    license="MIT",
    entry_points={
        "console_scripts": [
            "amjadsqrt=square_root_lib_amjad.__main__:main"
        ]
    },
)
