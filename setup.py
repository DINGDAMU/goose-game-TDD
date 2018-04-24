import setuptools

setuptools.setup(
    name="asyncDownloader",
    version="0.0.1",
    url="https://github.com/DINGDAMU/asyncDownloader",

    author="DAMU DING",
    author_email="dingdamu@gmail.com",

    description="An opinionated, minimal cookiecutter template for Python packages",
    long_description=open('README.rst').read(),

    packages=setuptools.find_packages(),

    install_requires=[],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite="tests",
)
