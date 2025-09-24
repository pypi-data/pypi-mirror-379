from setuptools import setup

setup(
    name='ess_cloud_utils',
    packages=['ess_cloud_utils'],
    version='0.31',
    description='Set of utils to support cloud deployments',
    author='Mykola Zelenku and Kamil Szewc',
    author_email='',
    license='Apache2',
    install_requires=['requests', 'py-eureka-client'],
    keywords=['ESS'],
    classifiers=[],
    python_requires='>=3.8',
)
