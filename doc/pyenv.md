
# PyEnv Simple
1. pyenv is used to manage python installation and versions
2. for mac, install with terminal cmd 'brew install pyenv'
3. cmds: 
   1. to install, 'pyenv install 3.12.7'
   2. view versions installed, 'pyenv versions'
   3. set global version, 'pyenv global 3.12.7'
   4. set local version, cd into a project, run 'pyenv local 3.12.7' ** .python-version file will be created
   5. run 'python -m venv .venv', this will create a .venv with python 3.12.7 
   6. view local version in a project folder, run 'pyenv local' 

# Reference 
1. https://github.com/pyenv/pyenv
2. https://jordanthomasg.medium.com/python-development-on-macos-with-pyenv-2509c694a808
3. 