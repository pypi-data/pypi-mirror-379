# setup.py
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="ecosistema-turbopdf",
    version="0.1.0",
    author="Ecosistema UNP",
    author_email="ecosistema.notificacion@unp.gov.co",
    description="Librería para generar PDFs en Django usando componentes HTML.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://example.com/no-publicado-ainda",  # Temporal
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'pdf_generator': ['templates/sistema/*.html'],
    },
    install_requires=[
        "Django>=4.0",
        "pdfkit>=0.6.1",
    ],
    python_requires='>=3.8',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    keywords="django pdf html template wkhtmltopdf",
)