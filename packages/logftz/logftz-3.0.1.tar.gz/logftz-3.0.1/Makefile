.PHONY: upload

upload:
	rm -f dist/*.tar.gz
	python setup.py sdist build
	twine upload dist/*
