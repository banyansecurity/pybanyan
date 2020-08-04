.PHONY: clean virtualenv test docker dist dist-upload

clean:
	find . -name '*.py[co]' -delete

virtualenv:
	virtualenv --prompt '|> banyan <| ' env
	env/bin/pip install -r requirements-dev.txt
	env/bin/python setup.py develop
	@echo
	@echo "VirtualENV Setup Complete. Now run: source env/bin/activate"
	@echo

test:
	python -m pytest \
		-v \
		--cov=banyan \
		--cov-report=term \
		--cov-report=html:coverage-report \
		tests/

docker: clean
	docker build -t banyan:latest .

tag:
	git tag -f `python -c 'from banyan.core.version import get_version; print(get_version())'`

dist: clean
	rm -rf dist/*
	python setup.py sdist
	python setup.py bdist_wheel

test-upload: dist tag
	twine upload -r testpypi dist/*

dist-upload: dist tag
	twine upload dist/*
