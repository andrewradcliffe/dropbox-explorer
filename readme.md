# Python Command-line Dropbox File Explorer

Uses the Dropbox SDK to navigate and download files from Dropbox

## Dependencies

[Python Dropbox SDK](https://github.com/dropbox/dropbox-sdk-python)
[python-dotenv](https://pypi.org/project/python-dotenv/)

## Installation

To install this program, make sure you first have a [Python](https://www.python.org/) distribution installed.

The steps to install are as follows:
1. First initialise a virtual environment:
```bash
python -m venv venv
```
2. Once that has been initialised, you can now install the pip packages:
```bash
pip install -r requirements.txt
```
3. (Optional) set up a local `.env` file with the following variables
```
DROPBOX_TOKEN = "{dropbox API key}"
DOWNLOAD_PATH = "{path to downloads folder (or other)}"
```

The last step is optional as you have the option to set these variables the first time you run the program, it will automatically create and save the variables in a `.env` file.

You should now be set up to use the Dropbox Explorer!

## Running the program

First, you will need to activate the virtual environment:

Note: If running through VSCode and you have the Python extension installed, you will not need to activate the environment. VSCode does it for you!

For Windows:
```bash
./venv/Scripts/Activate.ps1
```
Note: Make sure you run this program through Powershell, not Command Prompt

For MacOS / Linux:
```bash
source venv/bin/activate
```

To run the program, you should run the following command:
```bash
python -m main
```
