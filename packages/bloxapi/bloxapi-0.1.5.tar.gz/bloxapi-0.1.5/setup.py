from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="bloxapi",  # Package name for pip install bloxapi
    version="0.1.5",
    author="Your Name",  # Replace with your name
    author_email="your.email@example.com",  # Replace with your email
    description="Roblox Discord Bot Controller",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/bloxapi",  # Replace with your repo URL
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
    ],
)
