from fastapi import FastAPI
app=FastAPI()

@app.get('/')
def index():
    return {'data':'hello world'}

#dynamic route

@app.get('/show/{id}')
def about(id):
    return {'data': {id}}

#http://127.0.0.1:8000/show/100

@app.get('/blog/{comment}')
def about(comment: int):
    return {'data': comment}