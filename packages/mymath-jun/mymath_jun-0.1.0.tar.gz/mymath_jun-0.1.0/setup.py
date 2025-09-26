from setuptools import setup, find_packages

setup(
        name = 'mymath_jun',
        version = '0.1.0',
        description = 'A simple example package',
        author = 'junhyungkim',
        author_email = 'wnsgud4553@naver.com',
        packages=find_packages(where='src'), # src 폴더 내 패키지 검색
        package_dir = {'':'src'},
        python_requires = '>=3.7'
        )
