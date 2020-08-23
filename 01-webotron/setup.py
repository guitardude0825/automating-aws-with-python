from setuptools import setup

setup (
    name='webotron-80',
    version='0.1',
    author='Tom Coyle',
    author_email='tcoyle0825@gmail.com',
    description='Webotron 80 is a tool to deploy static websites to AWS',
    license='GPLv3+',
    pacakages=['webotron'],
    url='https://github.com/guitardude0825/automating-aws-with-python',
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        webotron=webotron.webotron:cli
    '''
)
