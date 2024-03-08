install/poetry:
	poetry install

setup/poetry:
ifdef POETRY_VERSION
	@echo "Found poetry version $(POETRY_VERSION)"
else
	@echo "Poetry not found, starting to install poetry"
	pip install pip -U
	pip install setuptools
	pip install poetry
	@echo "Installed poetry version" $(shell poetry --version)
endif
