

# Tool
https://github.com/yt-dlp/yt-dlp

# Output template
https://github.com/yt-dlp/yt-dlp#output-template

# Extra packages to install
```bash
ffmpeg libavdevice60 libdc1394-25 libjack-jackd2-0 libopenal-data libopenal1 libsdl2-2.0-0 libsndio7.0
```
## 📂 Project's structure
```
/youtube_downloader
├── api                                    # API Code
│   ├── controllers                        # API controllers
|   │   ├── download.py                    # Executes functionality to download
│   ├── query                              # API DB connection
│   │   ├── db_connection.py               # Get connection the database
│   │   ├── donwload.py                    # Donwload query structure
│   ├── routes                             # API Routes
│   │   ├── download.py                    # download routes
│   │   ├── main.py                        # main route configuration
│   ├── main.py                            # Main router
├── db                                     # Database configuration
│   ├── models                             # Models configuration
│   │   ├── download.py                    # download DB model
│   ├── base.py                            # Connection to the database
│   ├── session.py                         # Session database
├── downloads                              # Provitional storage
│   ├── audios                             # For audio
│   ├── videos                             # For videos
├── migrations                             # Handles database's structure updates
│   ├── env.py                             # Alembic database environment configuration
│── tests                                  # Automated test
│── utils                                  # Functionality that helps data treatment
│── youtube_downloader                     # Donwload functionality
│   ├── downloader.py                      # Functionality downloader
│── alembic.ini                            # Alembic tool configuration 
│── main.py                                # System's entry point
│── uvicorn_conf.py                        # Configuracion de uvicorn y arranque del sistema
├── .env.example                           # Variables de entorno de ejemplo
├── .dockerignore                          # Archivos a ignorar por los contenedores
├── docker-compose.yml                     # Configuración de Docker Compose
├── README.md                              # Presentación del proyecto
└── .gitignore                             #  Archivos a ignorar por el git

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

## Detect migrations
```bash
poetry run alembic revision --autogenerate -m "Basic functional system"
```
or

```bash
alembic revision --autogenerate -m "<your message>"
```

## Apply Migration
```bash
poetry run alembic alembic upgrade head
```
