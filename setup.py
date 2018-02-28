from setuptools import setup
import os


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='pymortgage',
    version='0.1.1',
    author="Dmytro Makovey",
    author_email="dmakovey@yahoo.com",
    description=("Python Mortgage utilities"),
    license="GPL3",
    keywords="mortgage library",
    url="https://github.com/droopy4096/pymortgage",
    packages=['mortgage', ],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Utilities",
        "License :: OSI Approved :: GPL3 License",
    ],
)
