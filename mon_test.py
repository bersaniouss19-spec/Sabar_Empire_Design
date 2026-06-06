import requests

try:
    response = requests.get("https://www.google.com")
    print(f"Succès ! Code de statut : {response.status_code}")
except Exception as e:
    print(f"Erreur : {e}")
