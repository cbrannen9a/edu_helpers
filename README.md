## Configuration for Python scripts

#### 1. Setting Up Python Virtual environments

Create a virtual environment first, this is best practice for Python development
to do this in cmd prompt navigate to the path if not already there for example C:\Workspaces\Python and type virtualenv env 

This command creates a virtual environment in a folder named env (you can call this what you like)

Once completed type the path to the activate script in the virtual environment this is located in env\scripts folder for example C:\Workspaces\Python\env\Scripts\activate.bat

This starts the environment for use in the terminal you'll see it's name infront of the prompt ie (env)

Issues: if you can't get the virtual environment command to work try running as admin typing virtualenv --version this should work then try to run setup as admin or alternatively use pip uninstall virtualenv and then pip install virtualenv and this should then resolve this issue

#### 2. Installing required packages to run scripts

In the virtual environment type: pip install -r requirements.txt 

This will add the required packages needed to run the scripts

#### 3. Optional setup for python in VSCode

(Optional) If using VScode to run scripts some additonal setup helps configure for running/debugging in virtualenvs.

If you have just made the virtualenv use the command Reload Window (Ctrl+Shift+P then search for Reload Window) this will mean that the environment is selectable in the setup

You can do this from the selector at bottom of screen or using the Python: Select Interpreter command and the virtual env should list. 

Once selected some prompts may appear regarding pylint, this is useful but not necessary just highlights good practises with python code

