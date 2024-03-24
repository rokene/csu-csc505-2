.DEFAULT_GOAL := help

MODULE1=module-1/app.py

.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*' $(MAKEFILE_LIST) | sort

.PHONY: m1
m1: ## executes module 1
	@echo "executing module 1 ..."
	@$(MODULE1)
	@echo "completed module 1."
