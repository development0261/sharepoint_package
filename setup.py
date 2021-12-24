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
  #dependency_links=['https://files.pythonhosted.org/packages/94/19/5a42fbf4680afba462c89f68f979ef76f2c99d3014edeca46064977333e9/apsw_wheels-3.36.0.post1-cp39-cp39-win32.whl'],
  install_requires=['setuptools','pandas','pandasql==0.7.3','Office365-REST-Python-Client','apsw','apsw-wheels','shillelagh==1.0.5']
  
)
