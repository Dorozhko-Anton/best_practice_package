
import setuptools 
import adossproject

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='adossproject',
    version=adossproject.__version__,
    # url='',
    license='MIT',
    author='Anton Dorozhko',
    tests_require=['pytest'],
    install_requires=['numpy'],
    author_email='dorozhko.a@gmail.com',
    description='packaging package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers = [
        'Programming Language :: Python',
        ],
    extras_require={
        'testing': ['pytest'],
    },
    # scripts = [''],
    python_requires='>=3.5'
)