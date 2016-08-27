from setuptools import setup
setup(
    name='HostHelper',
    version='1.0',
    packages=['main', 'main/config', 'main/edit', 'main/host'],
    package_dir={'': 'src'},
    entry_points={
        'console_scripts': ['hh=main:main']
    }
)