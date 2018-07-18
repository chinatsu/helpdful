# helpdful
pdf generating thing!

## Installation

For development purposes, it is recommended to use a virtual environment
to keep the project isolated.

1. `git clone` this repository, and enter its directory
2. Run `python -m venv .` to initiate a virtual environment
3. Activate the virtual environment,
  * `Scripts\activate.bat` for Windows, cmd.exe
  * `Scripts\activate.ps1` for Windows, PowerShell
  * `source bin/activate` for Bash/Zsh
  * `. bin/activate.fish` for Fish
  * `source bin/activate.csh` for Csh/Tcsh
4. Run `pip install -e .` to install the module and its dependencies
5. Run `python -m helpdful` to spin up a simple web server which will
serve you a PDF at localhost:3000!

### The alternate way

If you have Docker installed, you can simply clone this repository and
run `docker build -t helpdful .` and `docker run -itp 3000:3000 helpdful`
to easily run the web server as described above.

### Recommendations

It is recommended to use [Black](https://github.com/ambv/black) for code
formatting before pushing changes. Simply run `pip install black` and then
run `black helpdful` to have it format your changes.
