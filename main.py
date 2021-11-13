import youtube_dl #Debemos hacer la importacion de youtube_dl

def run(): #Creamos una función, con la que vamos a ejecutar el codigo
    
    menu = """
    Bienvenido! Aquí podras descargar musica y videos de Youtube, selecciona la opción: 

    1 - Descargar videos
    2 - Descargar musica

    Elige una opción: """

    opcion = int(input(menu))

    if opcion == 1:

        url_video = input('Ingresa la url del video: ')
        
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best', #elegimos el formato en este caso elegimos el mejor para descargar video
            'postprocessors': [{

                'key': 'FFmpegVideoConvertor', #le definimos a ffmpeg que queremos convertir solo el video

                'preferedformat': 'mp4',#definimos el formato de video

            }]
    }
        
        with youtube_dl.YoutubeDL(ydl_opts) as ydl: #clase con la que descargamos los videos de yt
             ydl.download([url_video])



    elif opcion == 2:

        url_musica = input('Ingresa la url del video: ')
        ydl_opts = {
            'format': 'bestaudio/best',#elegimos el formato en este caso elegimos el mejor para descargar audio
            'postprocessors': [{

                'key': 'FFmpegExtractAudio', #le definimos a ffmpeg que queremos extraer el audio del video

                'preferredcodec': 'mp3',#definimos el formato de video

                'preferredquality': '192',#elegimos la mejor calidad de audio establecida

            }]
    }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:#clase con la que descargamos los videos de yt y le extraeremos el audio 
            ydl.download([url_musica])

    else:
        print('Opción invalida⛔')

if __name__=='__main__':
    run()