install:
	poetry install

make lint:
	poetry run flake8 scraping accounts_app