from setuptools import setup, find_packages

setup(
    name="qrs32lib",                # Package name on PyPI
    version="0.1.0",                 # Start with 0.1.0
    author="Abhinandan Bhatt",
    author_email="your_email@example.com",
    description="Quantum Resonance Search 32-qubit model library",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/qrs32_project",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.12",
    install_requires=[
        "torch>=2.8.0",
        "numpy>=1.26"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
