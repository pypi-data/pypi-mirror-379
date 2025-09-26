from setuptools import setup, find_packages

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='kakaomail',
    version='1.0.1',
    description='send simple text using kakao mail',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    author='Kyunghonn',
    author_email='aloecandy@gmail.com',
    url='https://github.com/aloecandy/kakaomail',
    keywords=['kakao', 'mail','korean'],
    install_requires=[
        'email>=6.0.0a1',
        'python-dotenv'
    ],
    packages=find_packages(exclude=['tests'])
)