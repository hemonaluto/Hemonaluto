run:
	python ./game/hemonaluto.py

setup: requirements.txt
	pip install --upgrade pip
	pip install -r requirements.txt

run_tests:
	python -m unittest discover .

generate_world:
	python ./scripts/generate_world.py

generate_test_world:
	python ./scripts/generate_test_world.py