import setuptools

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='hulomhack',
    version='2.1',
    author='vova',
    author_email='vovk4756@gmail.com',
    description='лол взломай сайт',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/vova2f/hulom',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
        'somepackage>=1.1.0',
        'ipaddress==1.0.23',
        'colorama==0.4.6,',
        'requests==2.32.5',
        'threading'
    ]
)