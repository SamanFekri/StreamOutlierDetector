import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='outlierDetectorOnline',
     version='0.1',
     scripts=['OutlierDetector'] ,
     author="Saman Fekri",
     author_email="samanf74@gmail.com",
     description="Detect outliers of sequence in stream.",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/SamanFekri/StreamOutlierDetector",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
         "Operating System :: OS Independent",
     ],

 )