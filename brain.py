import spacy

# Initialisation du modèle une seule fois
try:
    nlp = spacy.load("fr_core_news_md")
except:
    # Si le modèle n'est pas chargé, on utilise une logique de repli simple
    nlp = None

def audit(texte):
    if nlp:
        doc = nlp(texte)
        mots_cles = [token.text for token in doc if not token.is_stop and not token.is_punct]
    else:
        mots_cles = texte.split()
    
    score = min(100, (len(mots_cles) * 10) + 40)
    produit = mots_cles[1] if len(mots_cles) > 1 else "votre offre"
    
    return {
        "score": f"{score}%",
        "mots_cles": mots_cles[:5],
        "message": f"Propulsez votre {produit} vers de nouveaux sommets. L'excellence signée Sabar Digital."
    }
