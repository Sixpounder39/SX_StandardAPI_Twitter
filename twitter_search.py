#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-

# ESTE PROGRAMA BUSCA LOS TWITTERS DEL TIMELINE DE UN USUARIO por medio de la API standar (gratuita)
# Recurso: https://twittersearch.readthedocs.io/en/latest/TwitterSearch.html
# Recurso: https://developer.twitter.com/en/pricing.html
# Stream premium y enterprise: https://github.com/gnip/support/tree/master/Premium%20Stream%20Connection

from TwitterSearch import *
import json
import datetime

fecha = datetime.datetime.now().strftime("%Y%m%d-%H:%M:%S")
print(fecha)

usuario=str(input("Ingresa el nombre de usuario Twitter que quieres monitorear: "))
file_name = "%s" % usuario + "_%s.json" % fecha # nombre del archivo de salida de los datos recabados
file = open(file_name, "w")
result = [] # Genero una lista que albergara los resultados

try:
    tso = TwitterUserOrder(usuario) # Obtengo el usuario desde el input
    #tso = TwitterUserOrder('nombre de usuario twitter') # En caso de requerir la búsqueda de un usuario especifico
    #tso = TwitterSearchOrder() # 1) En caso de requerir búsqueda por...
    #tso.set_keywords(['#Hashtag1', '#Hashtag2']) # 2) ... Hashtags.
    
    ts = TwitterSearch( # creando objeto de twittersearch *** Ingresa los token de twitter correspondientes
        consumer_key = "",
        consumer_secret = "",
        access_token = "",
        access_token_secret = ""

    )

    
    for tweet in ts.search_tweets_iterable(tso):
        result.append({
            'Usuario': tweet['user']['screen_name'],
            'Tweet': tweet['text']
        })
    with open(file_name, 'w+', encoding='utf-8') as f: #Para permitir caracteres UTF-8
        json.dump(result, f, ensure_ascii=False) # Para no mostrar caracteres Ascci


except TwitterSearchException as e: # Muestra la causa del error en caso de existir
    print(e) # Imprime el error en caso de existir
file.close() # Cierra el archivo Json donde escribe los datos recabados

print("Se ha generado el JSON con el contenido solicitado")
