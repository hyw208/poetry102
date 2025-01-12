# An empty python project for python dev & build & publish to pypi
1. Integrated with VS Code IDE & be able to run/debug code and tests
2. Project structure supports multiple python packages & modules 
3. Use pyenv & poetry for python installation/management
4. Use poetry for build and publish
5. Use python 3.12.7, pytest, coverage, flake8, mypy, black 


# To install and use 
1. <TBD>


# To develop
1. Install pyenv & poetry (with brew on mac)
2. In mac terminal, clone this poetry102 and open vscode, 'code poetry102'
3. Open vscode terminal and run cmd 'poetry env use 3.12.7' (** this create empty .venv under poetry102 folder **)
4. Run 'poetry install' to populate .venv with required dependencies, build and install code
5. To verify, run 'poetry run pip list' to see eg. pytest, coverage are installed properly
6. Now run src/poetry102/xyz.py with poetry script xyz, run 'poetry install' then 'poetry run xyz' 
7. Or run 'poetry install' and then 'poetry run python src/poetry102/xyz.py' (poetry is a bit flaky, retry 'poetry install' if needed)
8. When you see xyz as output, it's all set to start development
9. For more details on running and debugging with VS Code, see doc/102.md


# Installation and running
1. make test
2. cd test
3. python -m venv venv
4. source ./venv/bin/activate
5. pip install poetry102
6. uvicorn poetry102.main:app
   

# Repo
https://github.com/hyw208/poetry102


# TODO
1. https://www.pythoncheatsheet.org/blog/python-projects-with-poetry-and-vscode-part-1
2. https://www.pythoncheatsheet.org/blog/python-projects-with-poetry-and-vscode-part-2
3. add tox, ruff, formating  
4. experiment with black flake8 isort mypy pylint


# Installation for dev 
1. pyenv
2. poetry 


# References 
1. pyenv: https://opensource.com/article/20/4/pyenv 
2. poetry intro: https://realpython.com/dependency-management-python-poetry/
3. poetry doc: https://python-poetry.org/docs/cli/
4. poetry and pytest and coverage: https://dev.to/iamibi/add-coverage-report-with-pytest-and-gitlab-ci-3e9p
5. pytest conf: https://docs.pytest.org/en/stable/reference/reference.html#ini-options-ref
6. coverage conf: https://coverage.readthedocs.io/en/6.4.3/cmd.html#cmd
7. make: https://github.com/mapsa/makefile-examples (or use poetry shell)


# Commands
1. poetry new <folder> --src (or poetry new <folder>)
2. poetry env remove --all (delete virtual env)
3. poetry install (or 'poetry install --sync' to create virtual env & sync deps)
4. poetry env list
5. poetry env info --path
6. poetry env activate (and source the output) 
7. source "$(poetry env info --path)/bin/activate"
8. deactivate
9. poetry config --list
10. poetry add requests (or requests==2.25.1 "beautifulsoup4<4.10")
11. poetry add pytest coverage --dev
12. poetry add -D flake8 mypy
13. poetry remove requests
14. poetry lock (or poetry lock --no-update if no updating deps to latest versions)
15. poetry show --latest --top-level (or poetry show --tree)
16. poetry export --output requirements.txt
17. poetry run which python
18. poetry run xyz2 (run script defined in toml, need to do 'poetry install' first)
19. poetry run uvicorn --factory poetry102.main:app (xxxxxx not working all of a sudden)
20. poetry run fastapi src/poetry102/main.py
21. poetry publish -u __token__ -p <token>


