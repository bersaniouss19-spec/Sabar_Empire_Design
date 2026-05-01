import spacy
from flask import Flask, request, jsonify
from flask_cors import CORS

print("SABAR DIGITAL - Initialisation du moteur DEEP_SEA...")
try:
    nlp = spacy.load("fr_core_news_md")
    print("Moteur chargé avec succès. IA Prête.")
except Exception as e:
    print(f"Erreur de chargement : {e}")

app = Flask(__name__)
CORS(app)

@app.route('/audit', methods=['POST'])
def audit():
    data = request.json
    texte = data.get('texte', '')
    doc = nlp(texte)
    entites = [ent.text for ent in doc.ents]
    mots_cles = [token.text for token in doc if not token.is_stop and not token.is_punct]
    score = min(100, (len(mots_cles) * 5) + 50)
    
    return jsonify({
        "status": "ANALYSE MONDIALE COMPLÈTE",
        "expert": "Sabar Digital",
        "jeton": "SBR-8892-X-2026",
        "score_optimisation": f"{score}%",
        "concepts_cles": entites[:5],
        "mots_cles_strategiques": mots_cles[:10]
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
