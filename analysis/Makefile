#!/usr/bin/make

include .env

# app configuration
APP_NAME := "analysis"

# grep the version from the pyproject.toml
VERSION := "$(shell poetry version -s)"

# This will output the short help text for each task
# thanks to https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
.PHONY: help \
		format lint \
		schemas clean-schemas api-schemas py-schemas \
		test build \
		version

help: ## This help.
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)
.DEFAULT_GOAL := help



# Formatting and linting
FORMAT_TARGET ?= pp_* shared sys_* tests
format: ## Run formatters on FORMAT_TARGET (defaults to the current directory)
	poetry run black ${FORMAT_TARGET}
	poetry run isort ${FORMAT_TARGET}

lint: ## Run linters
	poetry run pre-commit run --all-files --show-diff-on-failure



# API schema download & python type generation
SCHEMAS := ablaufschritt abstimmung behoerdenmandat departement geschaeft geschaeftsart gremiumdetail gremiumstyp gremiumsuebersicht kontakt partei pendentbei referendum sitzung wahlkreis wohnkreis
SCHEMAS_DIR_API := provider_schemas/grzh/
SCHEMAS_DIR_PY := app/providers/grzh/schemas_gen/
SCHEMAS_MODULE_PY := app.providers.grzh.schemas_gen
schemas: api-schemas py-schemas  ## Download & Generate API schemas

clean-schemas: ## Clean API schemas
	rm -rf "${SCHEMAS_DIR_API}" "${SCHEMAS_DIR_PY}"

api-schemas: $(addprefix $(SCHEMAS_DIR_API), $(addsuffix .xsd, $(SCHEMAS))) ## Download API schemas

$(SCHEMAS_DIR_API)%.xsd:
	@mkdir -p "${SCHEMAS_DIR_API}"
	curl -fsSLo $@ "https://www.gemeinderat-zuerich.ch/api/$*/schema/"

py-schemas: $(addprefix $(SCHEMAS_DIR_PY), $(addsuffix .py, $(SCHEMAS))) ## Generate python types for API schemas

$(SCHEMAS_DIR_PY)%.py: $(SCHEMAS_DIR_API)%.xsd
	@mkdir -p "${SCHEMAS_DIR_PY}"
	poetry run xsdata generate -o pydantic -p "${SCHEMAS_MODULE_PY}" "${SCHEMAS_DIR_API}$*.xsd"



# Run & test
test: ## Run tests
	poetry run pytest tests

build: ## Build python wheel
	poetry build


# Bookkeeping
version: ## Output the current version
	@echo ${VERSION}
