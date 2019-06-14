from setuptools import setup, find_packages

setup(
    name="PassMan",
    version="1.0",
    packages=find_packages(),
    scripts=['passman'],
    include_package_data=True,

    author="Abel Binoop",
    author_email="abelbinoop@live.co.uk",
    description="A different kind of password manager.",
    license="GPL3",
    keywords="password manager python",
)
