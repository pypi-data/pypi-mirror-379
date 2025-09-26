from setuptools import setup, find_packages

setup(
    name="AgeCalculatorLib",
    version="0.1.0",
    description="Calculate age from birth date",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Asmaa Senan",
    author_email="asmaasenan3@gmail.com",
    packages=find_packages(),
    python_requires=">=3.7",
    license="MIT",
    entry_points={"console_scripts": ["agecalculatorlib=age_calculator_lib.__main__:main"]},
)
