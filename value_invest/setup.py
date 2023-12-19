from setuptools import find_packages, setup

setup(
    name='value_invest',
    packages=find_packages(include=['value_invest']),
    version='0.1.0',
    description='Useful functions in value investing',
    author='Brad Rohbock',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests'
)