from setuptools import setup, find_packages

setup(
    name='clean_folder',
    version='1.0',
    author='S.M.K.',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Utilities'
    ],
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'clean_folder = clean_folder.Sort:main']
    }
)
