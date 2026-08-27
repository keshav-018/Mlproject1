from setuptools import setup, find_packages
from typing import List


def get_requirements(filepath: str) -> List[str]:
    """Return a list of requirements parsed from a requirements file.

    Skips empty lines, comment lines (starting with '#'), and local editable
    installs (lines starting with '-e').
    """
    requirements: List[str] = []
    with open(filepath) as file_obj:
        for line in file_obj:
            line = line.strip()
            if not line:
                continue
            if line.startswith('#'):
                continue
            if line.startswith('-e'):
                # skip editable/local installs
                continue
            requirements.append(line)

    return requirements




setup(
name='mlproject1',
version='0.0.1',
author='Keshav gupta',
author_email='keshav10017@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)