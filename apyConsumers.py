from numpy  import asarray as np;from random import randint as rd;from json import load as js
def rN():return (rd(150,350)*2+9)
def megaFaker():
    with open('1000.json', 'r') as handle:
        milSemillas=js(handle)
    palabras=["como ","cuando ","donde queda ","como encontrar ","que hacer en ","obtener "]
    categoria=["animal","carmodle","moviesTitle","NameOfCompany","Drug","uni","apps"]
    rCategoria   = (str(categoria[rd(0,6)]))
    rSemilla     = (np(milSemillas)[rd(1,100)][rCategoria])
    rPalabras    = (str(palabras[rd(0,5)]))
    return(str(rPalabras+rSemilla))
print(rN())
print(megaFaker())
"""import json,urllib.request
librosApi="http://api.nytimes.com/svc/books/v2/lists/overview.json?published_date=2013-01-01&api-key=76363c9e70bc401bac1e6ad88b13bd1d"
ErgastApi="http://ergast.com/api/f1/2004/1/results.json"
data = urllib.request.urlopen(librosApi).read()
output = json.loads(data)
dataG = urllib.request.urlopen(ErgastApi).read()
ErgastJson = json.loads(dataG)
palabrasR=["como","cuando","donde","hacer"]
books=[]
Ergast=[]
for i in range(len(output)):
    for x in range(21):
        books.append(output['results']['lists'][x]['books'][i]['title'])
        books.append(output['results']['lists'][x]['books'][i]['description'])
        books.append(output['results']['lists'][x]['books'][i]['sunday_review_link'])
        books.append(output['results']['lists'][x]['books'][i]['buy_links'][0]['name'])
        books.append(output['results']['lists'][x]['books'][i]['buy_links'][0]['url'])                     
for i in range(len(ErgastJson)):
    for z in range(19):                
        Ergast.append("nombre => "       + ErgastJson['MRData']['RaceTable']['Races'][0]['Results'][z]['Driver']['givenName'])
        Ergast.append("apellido => "     + ErgastJson['MRData']['RaceTable']['Races'][0]['Results'][z]['Driver']['familyName'])
        Ergast.append("fe_nacimiento => "+ ErgastJson['MRData']['RaceTable']['Races'][0]['Results'][z]['Driver']['dateOfBirth'])
libros=json.dumps(books, indent=4, sort_keys=True)
pilotosRacer=json.dumps(Ergast, indent=4, sort_keys=True)
print(libros,pilotosRacer,palabrasR)
#print(libros, end='', flush=True)
"""
