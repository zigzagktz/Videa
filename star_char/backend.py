import urllib.request as request
import json

def parse(url):
    with request.urlopen(url) as films: 
        source = films.read()
        data = json.loads(source)
    return data

def film_names():
    counter = 0
    data = parse("https://swapi.dev/api/films/")
    keys = ['title','release_date']
    lst = []
    for i in data['results']:
        c = {}
        for key,value in i.items():
            if key in keys:
                c['id'] = counter
                c[key] = value
            else:
                continue
        counter += 1
        lst.append(c)
    return lst

def film_links():
    data = parse("https://swapi.dev/api/films/")
    film_links=[]
    for i in data['results']:
        for key,value in i.items():
            if key == "characters":
                film_links.extend(value)
    return film_links

def char_names():
    data = parse('https://swapi.dev/api/people/')
    counter = 0
    links = []
    keys = ['name','url']
    for i in data['results']:
        d = {}
        for key, value in i.items():
            if key in keys:
                d['id'] = counter
                d[key] = value
            else:
                continue
        counter +=1
        links.append(d)
    return links

def join():
    f_links = film_links()
    character = char_names()
    for i in character:
        if i['url'] in f_links:
            del i['url']  
    return character

if __name__ == "__main__":
    characters = join()
    films = film_names()

    print(films)
    


    


