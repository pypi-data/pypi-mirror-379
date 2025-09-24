from setuptools import setup, find_packages

with open("README_someip.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="someip-catch",
    version="1.0.0",
    author="SOME/IP Catch Framework",
    description="SOME/IP协议捕获和分析工具包",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/someip-catch",
    project_urls={
        "Repository": "https://github.com/yourusername/someip-catch",
    },
    packages=find_packages(include=['someip_catch', 'someip_catch.*']),
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
        "Topic :: System :: Networking",
        "Topic :: System :: Hardware",
    ],
    python_requires=">=3.7",
    keywords="someip automotive network protocol catch analysis",
    package_data={
        "someip_catch": ["data/*"],
    },
)