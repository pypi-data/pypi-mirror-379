from setuptools import setup, find_packages

setup(
    name='myutils-canary',
    version='0.2',
    author='Alejandro González',
    author_email='alejandro.dev@example.com',
    description='Funciones matemáticas simples para proyectos Python',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/AlejandroGlezSan/myutils-canary',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)
