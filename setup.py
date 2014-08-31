from setuptools import setup

setup(
    name='horoscope',
    version='0.1.1',
    description='Fetches and parses data from Ganeshaspeaks.',
    author='Tapasweni Pathak',
    author_email='tapaswenipathak@gmail.com',
    url='https://github.com/tapasweni-pathak/pyhoroscope',
    packages=['horoscope'],
    install_requires=[
        "beautifulsoup4 == 4.3.2",
    ]
    )
