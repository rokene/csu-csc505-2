.DEFAULT_GOAL := help

CURRENT_DIR := $(CURDIR)

MODULE1=$(CURRENT_DIR)/module-1
MODULE1_ENTRY=$(MODULE1)/app.py

MODULE2=$(CURRENT_DIR)/module-2
MODULE2_ENTRY=$(MODULE2)/app.py
MODULE2_DIAGRAM_FILEPATH=$(MODULE2)/diagram.uxf

.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*' $(MAKEFILE_LIST) | sort

.PHONY: m1
m1: ## executes module 1
	@echo "executing module 1 ..."
	@$(MODULE1_ENTRY)
	@echo "completed module 1."

.PHONY: m2
m2: ## executes module 2
	@echo "executing module 2 ..."
	@$(MODULE2_ENTRY) $(MODULE2_DIAGRAM_FILEPATH)
	@echo "completed module 2."
