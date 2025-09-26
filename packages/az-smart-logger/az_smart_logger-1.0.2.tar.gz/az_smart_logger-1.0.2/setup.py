from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="smart-logger",
    version="0.1.0",
    author="Your Name",
    author_email="youremail@example.com",
    description="Smart Logger library for Python projects with FastAPI, Flask, and Django support",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/smart-logger",
    packages=find_packages(exclude=["tests", "examples"]),
    python_requires=">=3.8",
    install_requires=[
        "fastapi>=0.95.0",
        "uvicorn[standard]>=0.23.0",
        "SQLAlchemy>=2.0",
        "Jinja2>=3.1",
        "typer>=0.9",
        "pydantic>=2.0"
    ],
    entry_points={
        "console_scripts": [
            "smart-logger = smart_logger.cli.commands:main",
        ],
    },
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Framework :: FastAPI",
        "Framework :: Flask",
        "Framework :: Django",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
