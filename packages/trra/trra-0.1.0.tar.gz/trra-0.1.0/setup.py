from setuptools import setup, find_packages

setup(
    name="trra",          # ✅ new unique PyPI name
    version="0.1.0",      # bump if you already uploaded before
    packages=find_packages(),
    install_requires=[],  # keep empty so it's fast
    description="",       # no description
    author="Your Name",
    author_email="you@example.com",
    url="",               # optional
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
