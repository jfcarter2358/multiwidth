.PHONY: help lint test clean install install-dev docs

help:  ##        Show this help
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

install:  ##     Install poetry if needed and use it to install multiwidth
	pip install poetry
	poetry install --no-dev

install-dev:  ## Install poetry if needed and use it to install multiwidth and dev dependencies
	pip install poetry
	poetry install

lint:  ##        Format and lint multiwidth
	black multiwidth
	pylint multiwidth

test:  ##        Test multiwidth
	pytest --cov=multiwidth --cov-report=html --cov-fail-under=95 -W ignore::DeprecationWarning -vv

clean:  ##       Remove test and doc artifacts
	rm -rf .coverage || true
	rm -rf htmlcov || true
	rm -rf .pytest_cache || true
	rm -rf multiwidth/__pycache__ || true
	rm -rf tests/__pycache__ || true
	rm -rf docs/build || true

docs:  ##        Generate documentation for multiwidth
	cd docs && make html

release:  ##     Release the current version of multiwidth
	poetry build
	poetry publish -u "${PYPI_USERNAME}" -p "${PYPI_PASSWORD}"
