from setuptools import setup

setup(
    name='django-articles',
    version='0.1.5dev',
    author='Gabriel Grant',
    packages=['articles',],
    license='LGPL',
    long_description=open('README').read(),
    install_requires=[
        'PIL',
        'django-inline-edit',
        'django-ckeditor',
    #    'django-html-field',
    ],
    dependency_links = [
    	'http://github.com/gabrielgrant/django-inline-edit/tarball/master#egg=django-inline-edit'
    	'http://github.com/gabrielgrant/django-ckeditor/tarball/master#egg=django-ckeditor'
    #    'http://github.com/gabrielgrant/django-html-field/tarball/master#egg=django-html-field',
    ]
)

