from setuptools import setup, find_packages

setup(
    name='purplepy',
    version='0.1.1',
    description='tokens processes',
    author='Your Name',
    packages=find_packages(),
    install_requires=[
        'psutil',
        'pywin32',
        'requests'
    ],
    entry_points={
        'console_scripts': [
            'purplepy=purplepy.main:cli'
        ]
    },
    python_requires='>=3.7',
)
