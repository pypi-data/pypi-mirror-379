from setuptools import setup, find_packages

setup(
    name='ouverture_firefox',
    version='1.0.0',
    packages=find_packages(),
    description='Un package d ouverture de firefox qu une seule fois',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='emmanuel julien',
    author_email='julienemmanuel01@gmail.com',
    url='https://github.com/emmanuel-julien/ouverture_firefox',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[],
)
