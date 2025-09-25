from setuptools import setup, find_packages

setup(
    name='my_maths',
    version='0.0.1',
    description='PYPI tutorial package creation written by TeddyNote',
    author='junhyungkim',
    author_email='wnsgud4553@naver.com',
    packages=find_packages(where='src'),
    python_requires='>=3.6',
    package_dir={'': 'src'},
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
