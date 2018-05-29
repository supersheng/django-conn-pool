import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django-conn-pool",
    version="1.11.1",
    author="kerol",
    author_email="ikerol@163.com",
    description="Connection Pooling with Django and SQLAlchemy",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kerol/django-conn-pool",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    install_requires=[
        'Django<2.0.0',
        'SQLAlchemy>=1.2.7',
    ]
)
