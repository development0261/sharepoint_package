from setuptools import setup, find_packages
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='pushpaksharepoint',
  version='0.0.6',
  description='To fetch sharepoint data',
  long_description="This is just a demon file made by someone",
  url='https://ritscm.regeneron.com/projects/DCCE/repos/apache-superset-connector/browse',  
  author='Pushpak Pandya',
  author_email='pushpak.pandya@regeneron.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='sharepoint', 
  packages=find_packages(),  
  install_requires=['setuptools','pandas','pandasql==0.7.3','shillelagh==1.0.5','apsw-wheels','Office365-REST-Python-Client']
)
