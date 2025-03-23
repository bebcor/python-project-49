#!/usr/bin/env python3

.PHONY: install brain-games                                                                                                                                                                                                                 
    
install:
	poetry install
    
brain-games:
	poetry run brain-games
	
build:
	poetry build
	
publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

make lint:
	poetry run flake8 brain_games

brain-even:
	poetry run brain-even
	
brain-gcd:
	poetry run brain-gcd

brain-progression:
	poetry run brain-progression

brain-prime:
	poetry run brain-prime

brain-calc:
	poetry run brain-calc
