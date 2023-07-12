from setuptools import setup, find_packages

setup(
    name='sat-solver',
    version='0.1',
    description='A SAT Solver',
    long_description=open('README.md').read(),
    url='https://gitlab.fit.fraunhofer.de/zeyd.boukhers/sat-solver',  # replace 'github_link' with the actual link to your GitHub repository
    author='Zeyd Boukhers',  # replace 'your_name' with your actual name
    author_email='zeyd.boukhers@fit.fraunhofer.de',  # replace 'your_email' with your actual email
    license='apache 2.0',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='sat solver logic cnf',
    packages=find_packages(exclude=['tests']),
    install_requires=[
        # list the packages that your library depends on.
        # For example: 'numpy', 'pysat', etc.
    ],
    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },
)
