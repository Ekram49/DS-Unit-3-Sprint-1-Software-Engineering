from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="Ekram49_another_try", # the name that you will install via pip
    version="2.0",
    author="Ekram Ahmed",
    author_email="ekramullahzaki@gmail.com",
    description="abbreviation to full name",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    #license="MIT",
    url="https://github.com/Ekram49/DS-Unit-3-Sprint-1-Software-Engineering",
    #keywords="",
    packages=find_packages()
)