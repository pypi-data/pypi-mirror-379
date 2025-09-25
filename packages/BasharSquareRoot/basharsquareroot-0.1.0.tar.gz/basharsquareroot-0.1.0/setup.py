from setuptools import setup, find_packages

setup(
    name="BasharSquareRoot",
    version="0.1.0",
    description="Calculate the square root of a number",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Bashar Mohammed",
    author_email="bsharmshrh00@gmail.com",
    packages=find_packages(),
    python_requires=">=3.7",
    license="MIT",
    entry_points={
        "console_scripts": [
            "basharsqrt=square_root_lib_bashar.__main__:main"
        ]
    },
)
