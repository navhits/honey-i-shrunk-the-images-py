""" 
This file is used as entrypoint for pyinstaller to pack the files.
It will be excluded from the package when installed separately. 
"""

from awesomecli.cli import app

if __name__ == "__main__":
    app()
