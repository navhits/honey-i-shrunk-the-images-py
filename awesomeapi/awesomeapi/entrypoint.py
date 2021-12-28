"""
This file is used as entrypoint for pyinstaller to pack the files.
It will be excluded from the package when installed separately.
"""
import uvicorn

from awesomeapi.main import app

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8081)
