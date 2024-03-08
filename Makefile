POETRY_VERSION :=$(shell poetry --version)

include makefiles/poetry.mk
include makefiles/quality.mk
include makefiles/workers.mk
