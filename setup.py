from setuptools import setup, find_packages

setup(
    name='mystify',
    version='1.0',
    packages=find_packages(where='src'),
    package_dir={'':'src'}
    install_requires=[
        # Specify minimum version
    ],
    test_require=[
        'unittest',
    ],
    test_suite='tests',
    entry_points={
        'console scripts': [
          # If you have any console scripts, specify them here  
        ],
    },
    url='https://github.com/ghinaalamsyahh/mystify',
    license='MIT',
    author='Ghina H. Alamsyah',
    author_email='ghinaalamsyah70@gmail.com',
    description='Robustly (and easily) solve hard optimization problems',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OST Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.12',
)