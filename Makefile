.DEFAULT_GOAL := help

CURRENT_DIR := $(CURDIR)

MODULE1=$(CURRENT_DIR)/module-1
MODULE1_ENTRY=$(MODULE1)/app.py

MODULE2=$(CURRENT_DIR)/module-2
MODULE2_ENTRY=$(MODULE2)/app.py
MODULE2_DIAGRAM_FILEPATH=$(MODULE2)/diagram.uxf

MODULE3=$(CURRENT_DIR)/module-3
MODULE3_ENTRY=$(MODULE3)/app.py

MODULE4=$(CURRENT_DIR)/module-4
MODULE4_ENTRY=$(MODULE4)/app.py

MODULE5=$(CURRENT_DIR)/module-5
MODULE5_ENTRY=$(MODULE5)/app.py

MODULE6=$(CURRENT_DIR)/module-6
MODULE6_ENTRY=$(MODULE6)/app.py

FINAL=$(CURRENT_DIR)/final-project
FINAL_ENTRY=$(FINAL)/app.py

.PHONY: help
help:
	@grep -E '^[a-zA-Z0-9_-]+:.*?## .*' $(MAKEFILE_LIST) | sort

.PHONY: m1
m1: ## executes module 1
	@echo "executing module 1 ..."
	@cd $(MODULE1); ./app.py
	@echo "completed module 1."

.PHONY: m2
m2: ## executes module 2
	@echo "executing module 2 ..."
	@$(MODULE2_ENTRY) $(MODULE2_DIAGRAM_FILEPATH)
	@echo "completed module 2."

.PHONY: m3
m3: ## executes module 3
	@echo "executing module 3 ..."
	@cd $(MODULE3); ./app.py
	@echo "completed module 3."

.PHONY: m4
m4: ## executes module 4
	@echo "executing module 4 ..."
	@cd $(MODULE4); ./app.py
	@echo "completed module 4."

.PHONY: m5
m5: ## executes module 5
	@echo "executing module 5 ..."
	@cd $(MODULE5); ./app.py
	@echo "completed module 5."

.PHONY: m6
m6: ## executes module 6
	@echo "executing module 6 ..."
	@cd $(MODULE6); ./app.py
	@echo "completed module 6."

.PHONY: final
final: ## executes final project
	@echo "executing final project ..."
	@cd $(FINAL); ./app.py
	@echo "completed final project."