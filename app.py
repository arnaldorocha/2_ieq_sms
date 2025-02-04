import os
from flask import Flask, render_template, url_for

app = Flask(__name__, static_url_path='/static', static_folder='static')

PHOTO_DIR = "static/images"  # Caminho base das imagens
VIDEO_DIR = "static/videos"  # Caminho base dos vídeos

# Função para obter arquivos de mídia (imagens e vídeos)
def get_album_media(album_name):
    media_folder = os.path.join(PHOTO_DIR, album_name)  # Caminho do álbum de imagens
    video_folder = os.path.join(VIDEO_DIR, album_name)  # Caminho do álbum de vídeos
    
    if not os.path.exists(media_folder) and not os.path.exists(video_folder):
        return None  # Se as pastas não existirem, retorna None
    
    media_files = []
    
    # Filtrando imagens
    if os.path.exists(media_folder):
        image_files = [f for f in os.listdir(media_folder) if f.endswith(('jpg', 'jpeg', 'png', 'gif'))]
        image_urls = [url_for('static', filename=f'images/{album_name}/{img}') for img in image_files]
        media_files.extend(image_urls)
    
    # Filtrando vídeos
    if os.path.exists(video_folder):
        video_files = [f for f in os.listdir(video_folder) if f.endswith(('mp4', 'avi', 'mov', 'mkv'))]
        video_urls = [url_for('static', filename=f'videos/{album_name}/{vid}') for vid in video_files]
        media_files.extend(video_urls)

    if not media_files:
        return None  # Se não houver mídia, retorna None

    return media_files


# Rota para a página inicial
@app.route("/")
def home():
    return render_template("index.html")

# Rota para a página "Pastores"
@app.route("/lideres")
def lideres():
    return render_template("lideres.html")


@app.route('/albuns')
def albuns():
    images_path = os.path.join('static', 'images', 'gpkids')
    videos_path = os.path.join('static', 'videos', 'gpkids')

    images = os.listdir(images_path) if os.path.exists(images_path) else []
    videos = os.listdir(videos_path) if os.path.exists(videos_path) else []

    medias = images + videos  # Junta imagens e vídeos
    return render_template('albuns.html', medias=medias)

# Rota para a página "Quem Somos"
@app.route("/quem_somos")
def quem_somos():
    return render_template("quem_somos.html")

# Rota para a página "História"
@app.route("/historia")
def historia():
    return render_template("historia.html")

# Outras rotas
@app.route("/batismo")
def batismo():
    return render_template("batismo.html")

@app.route("/cura")
def cura():
    return render_template("cura.html")

@app.route("/jesus_salva")
def jesus_salva():
    return render_template("jesus_salva.html")

@app.route("/volta_do_rei")
def volta_do_rei():
    return render_template("volta_do_rei.html")

@app.route('/gpkids')
def gpkids_album():
    album_name = 'gpkids'  # Exemplo de álbum
    media_files = get_album_media(album_name)
    
    if media_files:
        return render_template('album/gpkids.html', medias=media_files)
    else:
        return "Nenhuma mídia encontrada."
    
@app.route('/adolecentes')
def adolecentes_album():
    album_name = 'adolecentes'  # Exemplo de álbum
    media_files = get_album_media(album_name)
    
    if media_files:
        return render_template('album/adolecentes.html', medias=media_files)
    else:
        return "Nenhuma mídia encontrada."

@app.route('/jovens')
def jovens_album():
    album_name = 'jovens'  # Exemplo de álbum
    media_files = get_album_media(album_name)
    
    if media_files:
        return render_template('album/jovens.html', medias=media_files)
    else:
        return "Nenhuma mídia encontrada."
    
@app.route('/mulheres')
def mulheres_album():
    album_name = 'mulheres'  # Exemplo de álbum
    media_files = get_album_media(album_name)
    
    if media_files:
        return render_template('album/mulheres.html', medias=media_files)
    else:
        return "Nenhuma mídia encontrada."
    
@app.route('/homens')
def homens_album():
    album_name = 'homens'  # Exemplo de álbum
    media_files = get_album_media(album_name)
    
    if media_files:
        return render_template('album/homens.html', medias=media_files)
    else:
        return "Nenhuma mídia encontrada."
    

@app.route('/louvor')
def louvor_album():
    album_name = 'louvor'  # Exemplo de álbum
    media_files = get_album_media(album_name)
    
    if media_files:
        return render_template('album/louvor.html', medias=media_files)
    else:
        return "Nenhuma mídia encontrada."
    
@app.route('/teatro')
def teatro_album():
    album_name = 'teatro'  # Exemplo de álbum
    media_files = get_album_media(album_name)
    
    if media_files:
        return render_template('album/teatro.html', medias=media_files)
    else:
        return "Nenhuma mídia encontrada."
    

@app.route('/missoes')
def missoes_album():
    album_name = 'missoes'  # Exemplo de álbum
    media_files = get_album_media(album_name)
    
    if media_files:
        return render_template('album/missoes.html', medias=media_files)
    else:
        return "Nenhuma mídia encontrada."
    
@app.route('/midias')
def midias_album():
    album_name = 'midias'  # Exemplo de álbum
    media_files = get_album_media(album_name)
    
    if media_files:
        return render_template('album/midias.html', medias=media_files)
    else:
        return "Nenhuma mídia encontrada."
    
@app.route('/cultos')
def cultos_album():
    album_name = 'cultos'  # Exemplo de álbum
    media_files = get_album_media(album_name)
    
    if media_files:
        return render_template('album/cultos.html', medias=media_files)
    else:
        return "Nenhuma mídia encontrada."
    
@app.route('/dance')
def dance_album():
    album_name = 'dance'  # Exemplo de álbum
    media_files = get_album_media(album_name)
    
    if media_files:
        return render_template('album/dance.html', medias=media_files)
    else:
        return "Nenhuma mídia encontrada."
  

@app.route('/membros')
def membros_album():
    album_name = 'membros'  # Exemplo de álbum
    media_files = get_album_media(album_name)
    
    if media_files:
        return render_template('album/membros.html', medias=media_files)
    else:
        return "Nenhuma mídia encontrada."
  

@app.route('/eventos')
def eventos_album():
    album_name = 'eventos'  # Exemplo de álbum
    media_files = get_album_media(album_name)
    
    if media_files:
        return render_template('album/eventos.html', medias=media_files)
    else:
        return "Nenhuma mídia encontrada."
  

@app.route('/ceia')
def ceia_album():
    album_name = 'ceia'  # Exemplo de álbum
    media_files = get_album_media(album_name)
    
    if media_files:
        return render_template('album/ceia.html', medias=media_files)
    else:
        return "Nenhuma mídia encontrada."
  
@app.route('/batismos')
def batismos_album():
    album_name = 'batismos'  # Exemplo de álbum
    media_files = get_album_media(album_name)
    
    if media_files:
        return render_template('album/batismos.html', medias=media_files)
    else:
        return "Nenhuma mídia encontrada."
  

@app.route('/construcoes')
def construcoes_album():
    album_name = 'construcoes'  # Exemplo de álbum
    media_files = get_album_media(album_name)
    
    if media_files:
        return render_template('album/construcoes.html', medias=media_files)
    else:
        return "Nenhuma mídia encontrada."
  
@app.route('/recordacoes')
def recordacoes_album():
    album_name = 'recordacoes'  # Exemplo de álbum
    media_files = get_album_media(album_name)
    
    if media_files:
        return render_template('album/recordacoes.html', medias=media_files)
    else:
        return "Nenhuma mídia encontrada."
  

@app.route('/apresentacoes')
def apresentacoes_album():
    album_name = 'apresentacoes'  # Exemplo de álbum
    media_files = get_album_media(album_name)
    
    if media_files:
        return render_template('album/apresentacoes.html', medias=media_files)
    else:
        return "Nenhuma mídia encontrada."
  

if __name__ == "__main__":
    app.run(debug=True)
