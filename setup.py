import setuptools

setuptools.setup(
    name='pycrib',
    version='0.0.1',
    url='https://github.com/dolyasergey/pycrib',
    author='Sergio Dolia',
    author_email='sergei.s.dolia@gmail.com',
    description='Python cribbage',
    long_description=open('README.md').read(),
    packages=setuptools.find_packages(),
    package_dir={'': '/Users/dolyasergey/py/cribbage/pycrib'},
    install_requires=[],
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
)