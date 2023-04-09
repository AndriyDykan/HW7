import setuptools


setuptools.setup(
    name='SORT_SCRIPT',
    version='0.0.1',
    packages=setuptools.find_namespace_packages(),
    url='',
    license='"MIT"',
    author='MIRAN',
    author_email='andriy.dykanan@gmail.com',
    description='sort script for dir',
    entry_points={'console_scripts':['clean-folder = src.main:main']}
)
