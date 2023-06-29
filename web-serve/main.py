import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/')
def get_list():
    return [2,3,4,5,6,7,8,9,0]

@app.get('/main', response_class=HTMLResponse)
def get_main():
    return """
        <h1>Hola papirrin</h1>
        <p>No eres una pagina, eres lo que tu quieras ser querida</p>
        <img src="quico.jpg" width="300" height="200">

    """

def run():
    store.get_categories()

if __name__ == '__main__':
    run()
