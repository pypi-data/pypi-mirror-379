from setuptools import setup, find_packages

setup(name='primrea',
      version='0.1.0',
      description='Access to PRIMRE knowledge hub metadata and content.',
      author='Dominick DeCanio',
      author_email='dominick.c.decanio@pnnl.gov',
     license='BSD 3',
      packages=find_packages(),
      install_requires=['requests', 'pandas'])

print("Thank you for downloading primrea!")