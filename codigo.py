import yt_dlp
import os

def descargar_videos_tiktok(username, directorio_salida):
    # Asegurarse de que el directorio de salida existe
    os.makedirs(directorio_salida, exist_ok=True)

    # Configurar las opciones de yt-dlp
    ydl_opts = {
        'outtmpl': os.path.join(directorio_salida, '%(id)s.%(ext)s'),
        'format': 'best',
        'no_warnings': True,
        'ignoreerrors': True,
    }

    # URL del perfil de TikTok
    profile_url = f'https://www.tiktok.com/@{username}'

    # Descargar los videos
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([profile_url])
            print(f"Descarga completada para el usuario {username}")
        except Exception as e:
            print(f"Error al descargar videos de {username}: {str(e)}")

if __name__ == '__main__':
    # Solicitar el nombre de usuario de TikTok
    username = input("Ingresa el nombre de usuario de TikTok: ")
    
    # Definir el directorio de salida
    directorio_salida = f'./videos_{username}'
    
    # Llamar a la función para descargar los videos
    descargar_videos_tiktok(username, directorio_salida)
