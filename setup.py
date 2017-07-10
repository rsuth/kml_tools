from setuptools import setup

setup(name='kml_tools',
    version='0.2',
    description='tools for creating kml tour files for google earth',
    url='',
    author='Rick Sutherland',
    author_email='suthe.rick@gmail.com',
    license='MIT',
    packages=['kml_tools'],
    install_requires=['lxml','pykml'],
    zip_safe=False)
