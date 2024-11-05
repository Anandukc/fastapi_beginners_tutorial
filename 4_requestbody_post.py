from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

@app.get('/')
def index():
    return {'data':{'name':'Anandu'}}

@app.get('/about')
def about_page():
    return{'data':{'about':'page'}}

#post

class Blog(BaseModel):
    title : str
    body : str
   

@app.post('/about')
def create_blog(blog:Blog):
    return{"data":f'new message in created with {blog.title}'}