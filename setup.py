from setuptools import setup

with open('README') as f:
    long_description = ''.join(f.readlines())

setup(
    name='traco',
    version='0.1',
    description="Correction of translocation defects in crystals",
    long_description=long_description,
    author="Petr Kolenko",
    author_email='kolenpe1@cvut.cz',
    license='GNU LESSER GENERAL PUBLIC LICENSE Version 3',
    url='https://github.com/kolenpe1/traco',
    py_modules=['traco'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: GNU lGPL v3',
        'Operating System :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development',
    ],
    zip_safe=False,
)
