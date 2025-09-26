from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="image_processing_ar_2025",
    version="0.0.1",
    author="Antonio_Richard",
    author_email="antoniorichardhc@gmail.com",
    description="Processador de imagens",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/antonioorichard/image-processing/tree/beta",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)
