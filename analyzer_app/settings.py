from fastapi import FastAPI, Body, Form
from jinja2 import FileSystemLoader, Environment


APP = FastAPI()



FILE_LOADER = FileSystemLoader('templates')
ENV_TEMPLATES = Environment(loader=FILE_LOADER)

