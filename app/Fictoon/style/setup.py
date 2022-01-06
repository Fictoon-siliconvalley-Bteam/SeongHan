import setuptools

setuptools.setup(
    name='style',
    version='0.1',
    description='Neural style transfer in PyTorch.',
    # TODO: add long description
    long_description='Neural style transfer in PyTorch.',
    url='https://github.com/crowsonkb/style-transfer-pytorch',
    author='Katherine Crowson',
    author_email='crowsonkb@gmail.com',
    license='MIT',
    packages=['style_transfer1'],
    entry_points={
        'console_scripts': ['style_transfer1=style_transfer1.cli:main'],
    },
    package_data={'style_transfer1': ['*.icc', 'web_static/*']},
    install_requires=['aiohttp>=3.7.2',
                      'dataclasses>=0.8;python_version<"3.7"',
                      'numpy>=1.19.2',
                      'Pillow>=8.0.0',
                      'tifffile>=2020.9.3',
                      'torch>=1.7.1',
                      'torchvision>=0.8.2',
                      'tqdm>=4.46.0'],
    python_requires=">=3.6",
    # TODO: Add classifiers
    classifiers=[],
)
