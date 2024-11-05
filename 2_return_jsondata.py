from fastapi import FastAPI

app=FastAPI()

@app.get('/')
def index():
    return {'data':{'name':'Anandu'}}

@app.get('/about')
def about_page():
    return{'data':{'about':'page'}}