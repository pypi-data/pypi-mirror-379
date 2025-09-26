from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="alphabuilder_optimizer",
    version="0.0.1.3",
    description="Alpha optimizer library for quantitative finance research",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Geet Mukherjee",
    author_email="mukherjeegeet3@gmail.com",
    url="https://alphabuilder.xyz/",
    project_urls={
        "Optimizer": "https://alphabuilder.xyz/optimizer",
        "Changelog": "https://alphabuilder.xyz/changelog",
        "Documentation": "https://alphabuilder.xyz/docs",
    },
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Programming Language :: Python :: 3",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.8",
    install_requires=[
        "pandas>=1.3,<3.0",
        "numpy>=1.21,<2.0",  
        "requests>=2.28.0",  
    ],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
