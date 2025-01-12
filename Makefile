.PHONY: clean
clean: 
	rm .coverage || true
	rm coverage.xml || true
	rm -fr htmlcov || true
	rm -fr dist || true
	rm -fr .pytest_cache || true
	find . -name __pycache__ -exec rm -fr {} \; || true

.PHONY: install
install:
	poetry install

.PHONY: check
check: 
	poetry check

.PHONY: cov
cov: 
	poetry run coverage run

.PHONY: report
report: 
	poetry run coverage report

.PHONY: html
html: 
	poetry run coverage html

.PHONY: xml
xml: 
	poetry run coverage xml

.PHONY: build
build: 
	poetry build

.PHONY: publish
publish: 
	poetry publish

# Run python interactive
.PHONY: python
python: 
	poetry run python

# Echo activte command, need to then manually cope & paste
.PHONY: act
act: 
	poetry env activate

.PHONY: deact
deact: 
	deactivate