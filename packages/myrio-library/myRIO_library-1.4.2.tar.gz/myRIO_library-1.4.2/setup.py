from setuptools import setup, find_packages

# read the contents of your README file
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="myRIO_library",
    version="1.4.2",
    author="Aitzol Ezeiza Ramos",
    author_email="aitzol.ezeiza@ehu.eus",
    description="A library to control the myRIO board from National Instruments",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages("src"),
    package_dir={"": "src"},
    include_package_data=True,
    package_data={
        "myRIO_base": ["data/*"],
        "myRIO_base": ["examples/*"],
        "myRIO_API": ["examples/*"],
        "myRIO_API_client": ["examples/*"],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Other OS",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.5",
)
