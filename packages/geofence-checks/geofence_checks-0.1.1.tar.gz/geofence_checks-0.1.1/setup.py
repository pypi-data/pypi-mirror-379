from setuptools import setup, find_packages

setup(
    name="geofence_checks",
    version="0.1.1",
    description="A package for detecting geofence entry and exit events for trucks",
    author="chandra shekhar",
    author_email="chandra.shekhar@enmovil.in",
    packages=find_packages(),
    install_requires=[
        "pandas==1.4.1",
        "h3==3.7.6",
        "numpy==1.26.2",
        "shapely>=2.0.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)