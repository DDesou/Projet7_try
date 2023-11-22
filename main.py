from fastapi import FastAPI
import uvicorn


app = FastAPI()

@app.get('/')
def home():
    return 'Hello, my API works!!'



if __name__ == '__main__':
    uvicorn.run('myapp:app', host='0.0.0.0', port=8000)

