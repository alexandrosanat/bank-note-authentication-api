import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def index():
    return {'message': 'Hello world!'}


@app.get('/welcome')
def get_name(name: str):
    return {'Welcome to this page {}'.format(name)}


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)

