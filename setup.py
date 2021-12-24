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
  install_requires=['setuptools','pandas','pandasql==0.7.3','Office365-REST-Python-Client','shillelagh==1.0.5'],
  dependency_links=['https://files.pythonhosted.org/packages/01/82/6abf2c0940aba29c9b5740f67cfa4f7a987f0f1977d54cc14e0b700e1b53/apsw_wheels-3.36.0.post1-cp38-cp38-win_amd64.whl']
)
