import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="es8_roomManage",
    version="1.2.2",
    author="Ekkagra Singh",
    author_email="ekkagra@gmail.com",
    description="A small example package",
    include_package_data=True,
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["pandas"],
)
