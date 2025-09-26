from setuptools import setup, find_packages

def readme():
  with open('README.md', 'r') as f:
    return f.read()

setup(
  name='geodynamic',
  version='0.0.31',
  author='ivaleo',
  author_email='ivaleotion@gmail.com',
  description='Geometric tools for parsing GeoGebra construction, proccess with manim animation and export to SVG',
  long_description=readme(),
  long_description_content_type='text/markdown',
  url='https://pypi.org/project/geodynamic/',
  packages=find_packages(),
  entry_points = {
      'console_scripts': ['geodynamic=geodynamic.__main__:main'],
  },
  install_requires=[
      'requests>=2.25.1',
      'numpy>=1.26.0',
      'manim>=0.19.0',
      'pycairo>=1.0.0',
      ],
  classifiers=[
    'Programming Language :: Python :: 3.11',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent'
  ],
  keywords='geometry dynamic geogebra manim animation svg python',
  #project_urls={
  #  'Documentation': 'https://gitlab.mathem.ru/'
  #},
  python_requires='>=3.11'
)

print(find_packages())
