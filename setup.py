from setuptools import setup

setup(
   name='scorekivy',
   version='1.0',
   description='A useful module',
   author='Man Foo',
   author_email='foomail@foo.com',
   packages=['scorekivy'],  #same as name
   install_requires=['bar', 'greek'], #external packages as dependencies
)
