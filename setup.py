from setuptools import setup

setup(
    name='git-squash',
    version='0.0.1',
    description='Git utility for squashing all commits in a feature branch.',
    author='Zameer Manji',
    license='MIT',
    py_modules=["git_squash"],
    install_requires=[
        "GitPython",
    ],
    entry_points={
        'console_scripts': [
            'git-squash=git_squash:main'
        ],
    }
)
