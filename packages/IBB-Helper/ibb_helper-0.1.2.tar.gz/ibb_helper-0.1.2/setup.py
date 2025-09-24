from setuptools import setup, find_packages

setup(
    name='IBB_Helper', 
    version='0.1.2',
    packages=find_packages(), 
    install_requires=[],
    author='IBB',
    author_email='stud193984@stud.uni-stuttgart.de',
    description='helper functions',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.tik.uni-stuttgart.de/st193984/IBB_helper.git',
    license="custom",
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: Other/Proprietary License',
        'Operating System :: OS Independent',
    ],
)