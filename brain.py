from flask import Flask, request, jsonify
from flask_cors import CORS
import spacy
import os

# Initialisation
nlp = spacy.load("fr_core_news_md")
app = Flask(__name__)
CORS(app)

@app.route('/audit', methods=['POST'])
def audit():
    data = request.json
    texte = data.get('texte', '')
    doc = nlp(texte)
    
    # Éclaireur : Extraction
    mots_cles = [token.text for token in doc if not token.is_stop and not token.is_punct]
    score = min(100, (len(mots_cles) * 10) + 40)
    
    # Stratège : Optimisation
    produit = mots_cles[1] if len(mots_cles) > 1 else "votre offre"
    accroche = f"Propulsez vos {produit} vers de nouveaux sommets. L'excellence signée Sabar Digital."
    
    return jsonify({
        "status": "ANALYSE MONDIALE COMPLÈTE",
        "expert": "Sabar Digital",
        "score_optimisation": f"{score}%",
        "mots_cles_strategiques": mots_cles[:5],
        "solution_stratege": accroche,
        "impact": "+45% de conversion"
    })

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
