from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="diag-pythoncode",
    version="1.0.0",
    author="DiagProxy Framework",
    description="基于DiagProxy架构的ECU诊断刷写框架",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/diag-pythoncode",
    project_urls={
        "Repository": "https://github.com/yourusername/diag-pythoncode",
    },
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Hardware",
    ],
    python_requires=">=3.7",
    keywords="diagnostic ecu uds automotive flash",
    package_data={
        "diag_pythoncode": ["data/*"],
    },
)