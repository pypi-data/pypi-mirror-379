from setuptools import setup, find_packages

setup(
    name="samplesheetutils",
    version="1.3.4",
    author="nbtm-sh",
    author_email="n.glades@unsw.edu.au",
    packages=find_packages(),
    description="Collection of utilities for creating and transforming samplesheets and samples",
    install_requires=["pyyaml==6.0.1"],
    
    entry_points={
        'console_scripts': [
            'create-samplesheet=samplesheetutils.binaries.create_samplesheet:create_samplesheet',
            'sample-name=samplesheetutils.binaries.sample_name:sample_name',
            'truncate-msa=samplesheetutils.binaries.truncate_msa:truncate_msa'
        ]
    }
)
