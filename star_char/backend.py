import urllib.request as request
import json

def parse(url):
    """
    this functions is used to parse any url given to it
    returns data in json format
    """
    with request.urlopen(url) as films: 
        source = films.read()
        data = json.loads(source)
    return data

def film_names(): 
    """
    Fetch the json file and performs subsetting of data
    returns only the id, filname, and release date
    """

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
    """
    this function calls the films api and extracts the url for each character in the film
    """
    data = parse("https://swapi.dev/api/films/")
    film_links=[]
    for i in data['results']:
        for key,value in i.items():
            if key == "characters":
                film_links.extend(value)
    return film_links

def char_names():
    """
    this function fetches the name and url of each character from people API
    """
    data = parse('https://swapi.dev/api/people/')
    counter = 0  # USED TO GIVE UNIQUE ID
    links = []   
    keys = ['name','url']
    for i in data['results']:     # PERFORMING SUBSETTING LOGIC
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
    """
    this functions perfomrs the condition check
    if and only if the the character's url was in any of the seleted films url, 
    then only chracters data was saved. 

    this funtion returns the subseted chracter's api data with people worked in the 
    films from films API
    """

    f_links = film_links()
    character = char_names()
    for i in character:
        if i['url'] in f_links:   # PERFORMING THE CONDITION CHECK
            del i['url']  
    return character

if __name__ == "__main__":
    characters = join()
    films = film_names()

    print(films)
    


    


