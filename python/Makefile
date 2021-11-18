utest:
	pytest --cov-report term-missing --cov=src.hello test/

etest:
	behave e2e/features

lint:
	black src/
	black e2e/
	black test/
	pylint src/

install:
	pip3 install -r requirements.txt
