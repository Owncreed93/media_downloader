

# Tool
https://github.com/yt-dlp/yt-dlp


# Git
git remote add origin https://github.com/Owncreed93/media_challenge
git pull https://github.com/Owncreed93/media_challenge main
git config pull.rebase true
git pull https://github.com/Owncreed93/media_challenge main

# Extra packages to install
ffmpeg libavdevice60 libdc1394-25 libjack-jackd2-0 libopenal-data libopenal1 libsdl2-2.0-0 libsndio7.0

## 📂 Project's structure
```
/youtube_downloader
│   │   ├── downloads           # Provitional storage
│   │   │   ├── audios          # For audio
│   │   │   ├── videos          # For videos
│   │   ├── tests               # Test automatizados
│   │   ├── utils               # Validación de requisitos para acceder a la funcionalidad
│   │   ├── youtube_downloader  # Funcionalidad de descarga de la plataforma
│   │   └── main.py             # Punto de entrada del sistema
│   │   └── uvicorn_conf.py     # Configuracion de uvicorn y arranque del sistema
│   │   └── uvicorn_conf.py     # Configuracion de uvicorn
│   ├── .env.example          # Variables de entorno de ejemplo
│   ├── package.json          # Dependencias y configuraciones de node
│   ├── package-lock.json     # Versiones instaladas en la ultima version probada
│   ├── coverage              # Testing para funcionalidad
├── .dockerignore         # Archivos a ignorar por los contenedores
├── docker-compose.yml    # Configuración de Docker Compose
├── README.md             # Presentación del proyecto
└── .gitignore            # Archivos a ignorar por el git
```

# Poetry
## Activate shell
poetry shell

## Deactivate shell
exit

## Add packages

- Production:
    poetry add <package>=<version>
- Dev:
    poetry add --group dev <package>

## Install plugin to generate requirements
```bash
poetry add poetry-plugin-export
```

## requeriment.txt generation with Poetry
```bash
poetry export -f requirements.txt > requirements.txt
```

## Start Service
```bash
poetry run python uvicorn_conf.py
```