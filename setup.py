from setuptools import setup

setup(name='kleague',
      version='0.0.1',
      packages=['kleague'],
      entry_points={
          'console_scripts': [
              'kleague = kleague.__main__:main'
          ]
      },
      )
