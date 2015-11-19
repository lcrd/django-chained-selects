from setuptools import setup, find_packages

setup(
    name='django-chained-select',
    version='0.1.3',
    description="A django app to link two select fields together",
    author='Moreno Cunha',
    author_email='moreno.pinheiro@gmail.com',
    url="https://github.com/morenopc/django-chained-selects",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities'],
)
