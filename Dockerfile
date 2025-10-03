# 🐳 Dockerfile pour CS2 Teams Calendar
FROM python:3.11-slim

# Métadonnées
LABEL maintainer="CS2 Calendar Team"
LABEL description="Générateur automatique de calendrier pour les équipes CS2"
LABEL version="2.0.0"

# Variables d'environnement
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PIP_NO_CACHE_DIR=1
ENV PIP_DISABLE_PIP_VERSION_CHECK=1

# Répertoire de travail
WORKDIR /app

# Installation des dépendances système
RUN apt-get update && apt-get install -y \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copie des fichiers de dépendances
COPY requirements.txt .

# Installation des dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Copie du code source
COPY . .

# Permissions d'exécution
RUN chmod +x generate_calendar.py

# Volume pour le fichier config.json
VOLUME ["/app/config.json"]

# Volume pour le fichier de sortie
VOLUME ["/app/output"]

# Point d'entrée
ENTRYPOINT ["python", "generate_calendar.py"]

# Commande par défaut (peut être surchargée)
CMD []
