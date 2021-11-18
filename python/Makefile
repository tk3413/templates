utest:
	pytest --cov-report term-missing --cov=src.hello test/

etest:
	behave e2e/features

lint:
	black src/
	black e2e/
	black test/
	pylint src/
	pylint e2e/

install:
	pip3 install -r requirements.txt
