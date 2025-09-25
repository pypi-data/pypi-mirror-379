from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="bloxapi",  # Package name for pip install bloxapi
    version="0.1.7",
    author="jmkdev",
    author_email="jmkdev@gmail.com",
    description="Advanced roblox wrapper for the Roblox API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jmkdev/bloxapi",  # Replace with your repo URL
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.7",
    install_requires=[
        "discord.py>=2.0.0",
        "requests>=2.25.0",
        "pyautogui>=0.9.50",
        "python-dotenv>=0.19.0",
        "comtypes>=1.1.0",
        "pycaw>=20220416",
        "mss>=6.1.0",
        "pynput>=1.7.0",
        "pywin32>=227",
    ],
)
