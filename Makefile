.DEFAULT_GOAL := help

PROJECT_NAME := DS - Snippets
PROJECT_ALIAS := bacon
IMAGE_NAME := ds-snippets

.PHONY: help build test clean

help:
	@echo "------------------------------------------------------------------------"
	@echo "${PROJECT_NAME}"
	@echo "------------------------------------------------------------------------"
	@grep -E '^[a-zA-Z_/%\-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

build: clean ## Build unit test container
	@docker build -t ${PROJECT_ALIAS}/${IMAGE_NAME} .

test: build ## Run unit tests
	@docker run --rm ${PROJECT_ALIAS}/${IMAGE_NAME} /bin/bash -c "py.test --verbose --cov=src/ src/*/*.py"

clean: ## Remove images and containers
	@./resources/scripts/rm-image.sh ${PROJECT_ALIAS}/${IMAGE_NAME}
	@./resources/scripts/rm-container.sh ${IMAGE_NAME}
