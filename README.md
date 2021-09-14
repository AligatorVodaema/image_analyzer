Web service for image analysis.
Reports which pixels are more in the picture, white or black.

Requirements: Python3.9

You can pull docker container with this project:
$ docker pull aligatorvodaema/analyzer_app

Installation from git:
1. create venv, activate.
2. $ cd analyzer_app/
3. $ pip install -r requirements.txt

Run: $ uvicorn view:APP --reload --host=0.0.0.0 --port=8000

All requests/reponses logs are saved to a folder "logs".
For tests run:
$ pytest --tb=line -v -m pixel_counting

Usage:
1. go to localhost:8000
2. download png or jpg image
3. click send
