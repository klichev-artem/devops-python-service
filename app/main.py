from fastapi import FastAPI
import os

app = FastAPI(title="devops python service")

APP_ENV = os.getenv("APP_ENV", "local")
APP_VERSION = os.getenv("APP_VERSION", "0.1.0")

@app.get("/")
def read_root():
    return {
            "message": "hello from python service",
            "environment": APP_ENV
            }

@app.get
def health_check():
    return {
            "status": "ok",
            "environment": APP_ENV
            }

@app.get("/version")
def get_version():
    return {
        "app": "devops-python-service",
        "version": APP_VERSION,
    }
