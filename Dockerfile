# 1. Image de base optimisée pour Python
FROM python:3.10-slim

# 2. Installation des outils de compilation nécessaires pour SpaCy
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# 3. Définition du répertoire de travail
WORKDIR /app

# 4. Installation des dépendances Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 5. Téléchargement du modèle de langue SpaCy (Le cerveau NLP)
RUN python -m spacy download fr_core_news_md

# 6. Copie de tout l'arsenal (Interface, Brain, Moteurs)
COPY . .

# 7. Ouverture du port de communication pour Streamlit
EXPOSE 8501

# 8. Commande de lancement du Quartier Général
CMD ["streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]
