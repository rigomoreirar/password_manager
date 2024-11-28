from setuptools import setup, find_packages

# Function to read the requirements.txt file
def parse_requirements(filename):
    with open(filename, 'r') as f:
        requirements = f.read().splitlines()
    # Remove comments and empty lines
    requirements = [req.strip() for req in requirements if req.strip() and not req.startswith('#')]
    return requirements

setup(
    name='password_manager',
    version='0.1',
    description='A password manager using Hexagonal Architecture and SOLID principles',
    author='Rigoberto Moreira',
    author_email='rigmoreirar@gmail.com',
    packages=find_packages(),
    install_requires=parse_requirements('requirements.txt'),
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
