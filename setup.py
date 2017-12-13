'''Metadata about dist'''
from distutils.core import setup

setup(
    # Set up function's arg names
    name='nester',
    version='1.3.0',
    py_modules=['nester'], # Associate module's metadata w/setup func's args
    author='Arthur Ngondo',
    author_email='ngondoarthur@gmail.com',
    description='A simple printer of nested lists'
)
