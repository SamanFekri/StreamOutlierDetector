import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='pyood',
    packages=['pyood'],
    version='0.2.1',
    scripts=['pyood/OutlierDetector.py'] ,
    author="Saman Fekri",
    author_email="samanf74@gmail.com",
    description="Detect outliers of sequence in stream.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SamanFekri/StreamOutlierDetector",
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
        'Operating System :: OS Independent',
    ],
 )