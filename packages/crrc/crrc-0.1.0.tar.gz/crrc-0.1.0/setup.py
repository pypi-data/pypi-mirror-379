from setuptools import setup, find_packages

setup(
    name="crrc",          # ✅ PyPI package name
    version="0.1.0",      # bump this when you update
    packages=find_packages(),  # auto-detects crrc/ folder
    install_requires=[],  # no auto-installed dependencies
    description="",       # keep blank (no PyPI description)
    author="Your Name",
    author_email="you@example.com",
    url="",               # optional (GitHub link if you host it)
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
