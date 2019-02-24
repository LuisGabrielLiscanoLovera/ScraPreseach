from numpy  import asarray as np;from random import randint as rd;from json import load as js

def megaFaker():
    with open('1000.json', 'r') as milSemillas:
        milSemillas=js(milSemillas)   
    categoria =[
            "animal",
            "carmodle",
            "moviesTitle",
            "NameOfCompany",
            "uni",
            "apps"
            ]
    rCategoria  = (str(categoria[rd(0,(len(categoria))-1)]))   
    #####################Entrenar IA mejor dese txt#############
    if(rCategoria=="animal"):
        palabras=[
            "donde encontar ",
            "habita ",
            "comida ",
            "peloigro de extinción ",
            "venenoso ",
            "composicion osea ",
            ]
    
    elif(rCategoria=="carmodle"):
        palabras=[
            "que es  ",
            "a que sabe ",
            "donde queda ",
            "como encontrar ",
            "ver "]     
    
    elif(rCategoria=="moviesTitle"):
        palabras=[
            "fecha de lanzamiento ",
            "reparto  ",
            "secuelas ",
            "resumen  ",
            "protagonista ",
            "elenco ",
            "descargar ",
            "animacion ",
            "calidad ",
            "cinematic ",
            "musica " ,
            "esenario ", 
            "Historia "  ,
            "catetgoria " ,
            "errores de la " ,
            "trama " ,
            "arte " ,
            "libro " ,
            "escritor " ,
            "gion" ,
            "etapas ",
            ]     
    
    elif(rCategoria=="NameOfCompany"):
        palabras=[
            "fecha de creacion ",
            "competencia de la ",
            "estrategia de la ",
            "vision  de la ",
            "mision de la ",
            "capacidad de trabajadores ",
            "beneficios de la ",
             ]      
    
    elif(rCategoria=="uni"):
        palabras=[
            "requisitos para entara en ",
            "carrera ",
            "donde queda la ",
            "como encontrar la ",
            "que hacer en la ",
            "obtener beca en la "
            ]     
    
    if(rCategoria=="apps"):
        palabras=[
            "Version ",
            "git ",
            "licencia ",
            "como encontrar ",
            "que hacer en la ",
            "animacion ",
            "keys ",
            "free ",
            "gratis ",
            "obtener ",
            "descargar "
            ]        
    ###################################################

    rSemilla     = (np(milSemillas)[rd(1,100)][rCategoria])
    rPalabras    = (str(palabras[rd(0,(len(palabras))-1)]))    
    return(str(rPalabras+rSemilla))

###################usar un lamdam!#####################
def rN():return (rd(50,350)*2+9)
#######################################################
print("Tiempo ramdom: ")
print(rN()+(rN()/2-100))
print("buscador random: ")
print(megaFaker())
