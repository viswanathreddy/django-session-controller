import os
from setuptools import setup, find_packages

ROOT = os.path.abspath(os.path.dirname(__file__))

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-session-controller',
    version='1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['django'],
    description='Django middleware that controls sessions.',
    long_description=open(os.path.join(ROOT, 'README.md')).read(),
    url='https://github.com/viswanathreddy/django-session-controller',
    author='Viswanath,Naveen,Sibashish',
    author_email='visu.sanepalle@gmail.com,naveen.varshney29@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.x',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    zip_safe=False,
)
