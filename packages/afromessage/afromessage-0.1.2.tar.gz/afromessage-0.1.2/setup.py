from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="afromessage",
    version="0.1.2",  # Updated version to reflect changes
    author="Yonas Fikadie",
    author_email="yonasfikadie8989@gmail.com",  
    description="Python SDK for AfroMessage API to send SMS and OTP",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yonas8989/afromessage-python-sdk",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "requests>=2.25.0",
        "pydantic>=2.0",  
    ],
    entry_points={
        'console_scripts': [
            'afromessage-demo=usage.test_real:main',  
        ],
    },
)
