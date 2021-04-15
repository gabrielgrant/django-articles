from setuptools import setup

setup(
    name='django-articles',
    version='0.1.6dev',
    author='Gabriel Grant',
    packages=['articles',],
    license='LGPL',
    long_description=open('README').read(),
    install_requires=[
        'pillow',
        'django-inline-edit',
        'django-ckeditor',
        'django-ckeditor-filemodel-manager',
        'django-html-field',
        'django-static-filtered-images',
    ],
    dependency_links = [
    	'http://github.com/gabrielgrant/django-inline-edit/tarball/master#egg=django-inline-edit',
    	'http://github.com/gabrielgrant/django-ckeditor/tarball/master#egg=django-ckeditor',
    	'http://github.com/gabrielgrant/django-ckeditor-filemodel-manager/tarball/master#egg=django-ckeditor-filemodel-manager',
        'http://github.com/gabrielgrant/django-html-field/tarball/master#egg=django-html-field',
        'http://github.com/gabrielgrant/django-static-filtered-images/tarball/master#egg=django-static-filtered-images',
    ]
)

