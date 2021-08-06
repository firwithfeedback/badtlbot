from setuptools import setup

with open("README", 'r') as f:
    long_description = f.read()

setup(
   name='badtlbot',
   version='0.1.0',
   description='A bad translation bot for Discord using goslate.',
   license="GPL3",
   long_description=long_description,
   author='Ian Palabasan',
   author_email='firwithfeedback@gmail.com',
   url="https://firwithfeedback.github.io/",
   packages=['badtlbot'],
   install_requires=['goslate', 'discord.py'],
   scripts=[
            'scripts/badtlbot-instance',
            'scripts/badtlbot',
           ]
)
