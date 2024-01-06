from setuptools import setup, find_packages

setup(
    name='template_selenium_python',
    version='0.1.0',
    description='sirva este proyecto como un template para futuros proyectos',
    author='Rommel',
    author_email='rommel.ayala@gmail.com',
    url='https://www.linkedin.com/in/rommelayala/',
    packages=find_packages(exclude=['tests*']),
    install_requires=[
        # Lista de dependencias requeridas
        'dependencia1>=1.0',
        'dependencia2>=2.0,<3.0',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
