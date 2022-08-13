.PHONY: documentation

documentation:
	python -c "import shutil;shutil.rmtree('documentation')"
	python -m pdoc --html game --output-dir documentation

run:
	python main.py

setup: requirements.txt
	pip install --upgrade pip
	pip install -r requirements.txt

run_tests:
	python -m unittest discover .

generate_world:
	python ./scripts/generate_world.py

generate_test_world:
	python ./scripts/generate_test_world.py