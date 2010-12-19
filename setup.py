from setuptools import setup

setup(
    name='django-articles',
    version='0.1dev',
    author='Gabriel Grant',
    packages=['articles',],
    license='LGPL',
    long_description=open('README').read(),
    install_requires=[
        'PIL',
    #    'django-html-field',
    ],
    dependency_links = [
    #    'http://github.com/gabrielgrant/django-html-field/tarball/master#egg=django-html-field',
    ]
)

