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
  install_requires=['setuptools','pandas','pandasql==0.7.3','Office365-REST-Python-Client','shillelagh==1.0.5','https://files.pythonhosted.org/packages/2b/cc/fa84b748d2bba79b894d29aff9764746e6af4b8f22bea68b634a58336688/apsw-3.36.0.post1-cp38-cp38-manylinux1_x86_64.whl']
)
