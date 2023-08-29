import subprocess

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


if __name__ == '__main__':
    subprocess.run(["uvicorn", "challenge_11_restful_api:app", "--reload", "--port", "8080"])
