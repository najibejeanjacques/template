install:
	@echo "Installing ...."
	poetry install
	poetry run pre-commit install

activate:
	@echo "Activate virtual environment"
	poetry shell

initialize_git:
	@echo "Initialize git"
	git init

setup: initialize_git install