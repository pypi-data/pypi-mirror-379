# from setuptools import setup, find_packages

# setup(
#     name="nimpy",  # your library name (must be unique on PyPI)
#     version="0.1.0",
#     description="A Python library containing nimpy.",
#     author="Nimpy",
#     packages=find_packages(),
#     python_requires=">=3.6",
# )














# setup.py
from setuptools import setup, find_packages

setup(
    name="nimpy-mannny",      
    version="0.1.0",
    description="advanced version of nimpy by mannny",
    author="nimpy production by mannny",
    packages=find_packages(),        # will now find nimpy/
    include_package_data=True,
    python_requires=">=3.8",
    install_requires=[
        "numpy",
        "pandas",
        "matplotlib",
        "scikit-learn",
        "tensorflow"
    ],
)
