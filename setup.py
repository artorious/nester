from distutils.core import setup

# Metadata about dist

setup(
    # Set up function's arg names
    name        = 'nester', 
    version     = '1.1.0',
    py_modules  = ['nester'], # Associate module's metadata with setup func's args
    author      = 'Arthur Ngondo',
    author_email = 'ngondoarthur@gmail.com',
    description = 'A simple printer of nested lists'  

)