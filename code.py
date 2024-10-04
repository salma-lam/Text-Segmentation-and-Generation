import re

# Étape 1: Segmentation d'un texte en phrases
def segmenter_en_phrases(texte):
    # On segmente les phrases en utilisant des marqueurs de fin de phrase suivis d'un espace (avec gestion des guillemets).
    phrases = re.split(r'(?<=[.!?;])\s+(?="?)', texte.strip())
    return [phrase for phrase in phrases if phrase]

# Étape 2: Segmentation d'une phrase en mots
def segmenter_en_mots(phrase):
    # Expression régulière modifiée pour capturer les mots, les contractions, les nombres et les unités (par ex. 19h30).
    mots = re.findall(r"\b\w+(?:[-']\w+)*\b|\d+[hH]?\d*|[.,!?;\"']", phrase)
    return mots

# Étape 3: Génération d'une phrase à partir d'une liste de mots
def generer_phrase(mots):
    phrase = ' '.join(mots).replace("  ", " ").strip()
    # On ajoute un point à la fin si la phrase ne se termine pas déjà par un signe de ponctuation
    if not re.match(r'[.!?;]$', phrase):
        phrase += '.'
    return phrase

# Programme principal
if __name__ == "__main__":
    texte = input("Veuillez entrer un texte en français : ")

    # Étape 1 : Découpage en phrases
    phrases = segmenter_en_phrases(texte)
    print("\nPhrases segmentées :")
    for i, phrase in enumerate(phrases, start=1):
        print(f"{i}. {phrase}")

    # Étape 2 : Découpage de chaque phrase en mots
    print("\nMots dans chaque phrase :")
    for phrase in phrases:
        mots = segmenter_en_mots(phrase)
        print(f"Phrase : '{phrase}'")
        print(f"Mots : {mots}")

    # Étape 3 : Génération de phrases à partir d'une liste de mots
    print("\nGénération de phrases à partir de listes de mots :")
    for phrase in phrases:
        mots = segmenter_en_mots(phrase)
        phrase_generee = generer_phrase(mots)
        print(f"Phrase générée : {phrase_generee}")

    # Exemple de test : "À l'âge de 10 ans, Maxime a découvert qu'il avait un talent particulier pour la musique. 'Vas-tu jouer à la fête de ce soir?' demanda sa mère, intriguée. 'Bien sûr !' répondit-il avec enthousiasme. Le concert a commencé à 19h30, et l'auditorium était rempli de familles et d'amis. À la fin, tout le monde a applaudi, et Maxime a reçu une ovation. 'Que puis-je faire pour vous remercier?' s'interrogea-t-il."
