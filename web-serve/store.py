import requests

def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    print(r.status_code)
    print(r.text)
    categorias = r.json()
    llave = input('Type(name, image, id, creationAt, updateAt): ')
    for categoria in categorias:
        print(categoria[f'{llave}'])
