from setuptools import setup, find_packages

setup(
    name="PassMan",
    version="1.2",
    packages=find_packages(),
    scripts=['passman'],
    data_files=[
        ('share/applications', ['com.programmabel.PassMan.desktop']),
        ('share/passman/', ['window.glade'])
    ],
    install_requires=[
        'PyGObject',
    ],

    author="Abel Binoop",
    author_email="abelbinoop@live.co.uk",
    description="A different kind of password manager.",
    license="GPL3",
    keywords="password manager python",
)
