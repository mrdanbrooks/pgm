from setuptools import setup


with open("README.md", "r") as f:
    long_description = f.read()

setup(name='pgm',
      version="0.0.2",
      description="Process Group Management",
      long_description=long_description,
      url="https://github.com/mrdanbrooks/pgm",
      author="Dan Brooks",
      license="Apache v2.0",

      # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Environment :: Console',
          'Intended Audience :: System Administrators',
          'License :: OSI Approved :: Apache Software License',
          'Programming Language :: Python :: 2.7',
      ],
      keywords='pgm, tmux',

      scripts=['pgm'],

      )



