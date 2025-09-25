from setuptools import setup, find_packages

setup(
    name="HamoodSquareRoot",
    version="0.1.0",
    description="Calculate the square root of a number",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Hamood Ali Albukhaiti",
    author_email="hamoodalbukhity2000@gmail.com",
    packages=find_packages(),
    python_requires=">=3.7",
    license="MIT",
    entry_points={
        "console_scripts": [
            "hamoodsqrt=square_root_lib.__main__:main"
        ]
    },
)
