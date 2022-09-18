import setuptools

with open("./brasilapy/README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="brasilapy", 
    packages=setuptools.find_packages(),                    # This is the name of the package
    version="0.0.5",                        # The initial release version
    author="Filipe Soares",                     # Full name of the author
    description="Brasil API client.",
    license='MIT',
    long_description=long_description,      # Long description read from the the readme file
    long_description_content_type="text/markdown",
    url='https://github.com/lipe14-ops/brasilapy',
    author_email='filipe.ns1001@gmail.com',   # List of all python modules to be installed
    keywords=['api', 'requests', 'brasilapy', 'web', 'client' ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],                                      # Information to filter the project on PyPi website
    python_requires='>=3.9',                # Minimum version requirement of the package   # Directory of the source code of the package
    install_requires=[]                     # Install other dependencies if any
)