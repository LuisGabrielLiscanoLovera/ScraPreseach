from random import randint as rd
from json import load as js
try:   
    from numpy  import asarray as np
except Exception as e:
    import subprocess,sys   
    print ("**** instalando lib Numpy ****")
    subprocess.call([sys.executable, "-m", "pip", "install", "numpy" ])
    from numpy  import asarray as np

def megaFaker():
    try:       
        with open('1000.json', 'r') as milSemillas:
            milSemillas=js(milSemillas)
    except Exception as e:
        print (str(e)+"< Archivo no existe!")
        exit()   
    
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
            "fecha de lanzamiento de ",
            "reparto  en ",
            "secuelas de  ",
            "resumen  ",
            "protagonista en ",
            "elenco de ",
            "descargar de ",
            "animacion de ",
            "calidad  de " ,
            "cinematic de ",
            "musica de " ,
            "esenario en ", 
            "Historia en"  ,
            "catetgoria de la" ,
            "errores de la " ,
            "trama de" ,
            "arte de " ,
            "libro de " ,
            "escritor de " ,
            "gion de" ,
            "etapas de ",
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
      
    rSemilla     = np(milSemillas)[rd(0,999)][rCategoria]
    rPalabras    = str(palabras[rd(0,(len(palabras))-1)])   
    
    
    #################### Documentacion info solo informativo#######################
    global rn
    doc="""
        --------------------Thankas for play!-----------        
                            Al azar python3
                            
        Tiempo segunso           =  [{}] 
        Tiempo minutos           =  [{}]
        Tema                     =  [{}]
        Categoria                =  [{}]         
        Accion a concatenar      =  [{}]       
        cantidad de palabras     =  [{}]
        ------------------------------------------------
    """.format(rn(),(str(rn()/60)),rCategoria,rSemilla,rPalabras,(len(milSemillas)))    
    print (doc)
    ##########################################################    
    
    return(str(rPalabras+rSemilla))

rn=lambda:int(rd(50,350)*2+9)+(rd(0,100)/3+100)    
print (megaFaker())
