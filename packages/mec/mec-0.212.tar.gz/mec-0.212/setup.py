from setuptools import setup, find_packages

setup(
	name="mec",
	version="0.212",
	authors=["Alfred Galichon"],
	author_email="ag133@nyu.edu",
	licence="",
	python_requires=">= 3",
	install_requires=["gurobipy"],
	packages=find_packages(),
	package_data = {'mec': ['datasets/**/*.txt','datasets/**/*.csv','datasets/**/*.asc','datasets/*/*/*.asc','datasets/*/*/*.txt','datasets/*/*/*.csv']},
	test_suite="mec.tests", 
	description="description of the package",	# can link markdown file here 
	include_package_data=True,
)