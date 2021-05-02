ENVIRONMENT_PREFIX=$(shell pwd)
ENVIRONMENT_NAME=.vesqlite
VENV_NAME=${ENVIRONMENT_PREFIX}/${ENVIRONMENT_NAME}
VENV_BIN=${VENV_NAME}/bin

# Virtualenv for project
dev: requirements.txt
	echo "Creating virtual environment..."
	${VENV_BIN}/pip-sync requirements.txt

requirements.txt: venv
	${VENV_BIN}/pip-compile requirements.in --output-file requirements.txt

venv: requirements.in
	echo "Compiling requirements..."
	python3 -m venv ${ENVIRONMENT_NAME}
	${VENV_BIN}/pip3 install --upgrade 'pip'
	${VENV_BIN}/pip3 install pip-tools 'numpy' 'scipy' 'setuptools>=41.0.0' 'ipykernel'
	# python3 -m ipykernel install --user --name=${ENVIRONMENT_NAME}

coverage:
	coverage erase
	run --include=eurocities/* -m pytest -ra
	coverage report -m

lint:
	black eurocities
	flake8 eurocities
	pylint eurocities
	mypy eurocities

test:
	pytest -ra