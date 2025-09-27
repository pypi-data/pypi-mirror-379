import setuptools

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='webhacking',
    version='2.0',
    author='vova2f',
    author_email='vovk4756@gmail.com',
    description='взломай сайт',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/vova2f/webhacking',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.12',
    install_requires=[
        'somepackage>=1.1.0',
        'ipaddress==1.0.23',
        'socket',
        'trio-websocket==0.12.2',
        'colorama==0.4.2',
        'requests==2.32.5',
        'threading',
        'websocket-client==1.8.0'
    ]
)