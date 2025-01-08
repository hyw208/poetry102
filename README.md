
# TODO
1. activate/deactivate virtual env
2. to use poetry shell or not 
3. add tox, ruff, formating  
4. experiment with black flake8 isort mypy pylint


# References 
1. pyenv: 
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
7. deactivate
8. poetry config --list
9. poetry add requests (or requests==2.25.1 "beautifulsoup4<4.10")
10. poetry add pytest coverage --dev
11. poetry remove requests
12. poetry lock (or poetry lock --no-update if no updating deps to latest versions)
13. poetry show --latest --top-level (or poetry show --tree)
14. poetry export --output requirements.txt
15. poetry run which python
16. poetry run xyz2 (run script defined in toml, need to do 'poetry install' first)
