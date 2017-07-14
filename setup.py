from setuptools import setup

setup(name='myFlaskApp',
      version='1.0',
      description='myFlaskApp',
      author='Noah Huntington',
      author_email='noah@beyondmapping.com',
      url='http://www.python.org/sigs/distutils-sig/',
      install_requires=[
            'blinker==1.4',
            'click==6.7',
            'Flask==0.12.2',
            'Flask-Mail==0.9.1',
            'itsdangerous==0.24',
            'Jinja2==2.9.6',
            'MarkupSafe==1.0',
            'Werkzeug==0.12.2'
            ],
      )