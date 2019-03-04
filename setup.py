from setuptools import setup, find_packages

setup(
    name='pyxhook',
    version='1.0.0',
    description='Packaged version of pyxhook',
    maintainer='g3rb3n',
    license='BSD-3-Clause',
    url='https://github.com/g3rb3n/pyxhook/',
    package_dir={'': 'src'},
    include_package_data=True,
    packages=find_packages('src'),
    entry_points={
    },
    install_requires=[
        'python-xlib'
    ]
)
