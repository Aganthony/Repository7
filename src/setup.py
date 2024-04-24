from setuptools import setup # type: ignore

setup(
    name="barky",
    version="0.1.1",
    packages=["djbarky"],
)
from setuptools import setup, find_packages # type: ignore

setup(
    name="pms",
    version="0.1.0",
    packages=find_packages(),
    # If you have specific subpackages and you want to list them manually, you can do so:
    # packages=["pms", "pms_app"],
    # include_package_data=True to include files specified by MANIFEST.in
    include_package_data=True,
    # Additional metadata about your package
    description="Patient Monitoring System",
    author="Your Name",
    author_email="your.email@example.com",
    # More detailed description
    long_description=open('README.md').read(),
    # If the readme is in another format like .rst
    # long_description_content_type='text/x-rst',
    # The project's main homepage.
    url="https://github.com/yourusername/pms",
    # If there are any package dependencies, list them here
    install_requires=[
        # 'dependency==version',
    ],
    # To provide executable scripts, use entry points
    entry_points={
        'console_scripts': [
            # 'script_name = module:function',
        ],
    },
    # Additional classifiers that describe the project
    classifiers=[
        "Programming Language :: Python",
        "Framework :: Django",
        "Operating System :: OS Independent",
    ],
)
