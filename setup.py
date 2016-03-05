from setuptools import setup, find_packages
import aldryn_quote

CLASSIFIERS = [
    "Development Status :: 4 - Beta",
    "Framework :: Django",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 2.7",
    "Topic :: Software Development",
    "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
]

setup(
    author="Philipp Havrilla",
    author_email="philipp.havrilla@bluewin.ch",
    name='aldryn-quote',
    version=aldryn_quote.__version__,
    description='Easy to use quote plugin for Aldryn Cloud and django CMS.',
    long_description=open('README.md').read(),
    url='https://github.com/philipp-x/aldryn-quote',
    packages=find_packages(),
    include_package_data = True,
    zip_safe = False,
    license='MIT License',
    platforms=['OS Independent'],
    classifiers=CLASSIFIERS,
    install_requires=[
        'Django>=1.7',
    ],
)
