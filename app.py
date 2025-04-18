from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os
from datetime import datetime

app = Flask(__name__)
CORS(app)

CANDIDATURES_FILE = "candidatures.json"
RECRUTEURS_FILE = "recruteurs.json"
OFFRES_FILE = "offres.json"

# Chargement des fichiers JSON

def charger_json(fichier):
    if os.path.exists(fichier):
        with open(fichier, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def enregistrer_json(fichier, data):
    with open(fichier, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

# Scoring IA

def calculer_score(candidat_competences, offre_competences):
    c_set = set(c.strip().lower() for c in candidat_competences.split(","))
    o_set = set(o.strip().lower() for o in offre_competences.split(","))
    if not o_set:
        return 0
    score = len(c_set & o_set) / len(o_set) * 100
    return round(score, 2)

# Routes API

@app.route("/candidature", methods=["POST"])
def soumettre_candidature():
    data = request.json
    data["Date"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Score IA basé sur la dernière offre ajoutée
    offres = charger_json(OFFRES_FILE)
    derniere_offre = offres[-1] if offres else {"competences": ""}
    data["Score"] = calculer_score(data.get("competences", ""), derniere_offre["competences"])

    candidatures = charger_json(CANDIDATURES_FILE)
    candidatures.append(data)
    enregistrer_json(CANDIDATURES_FILE, candidatures)
    return jsonify({"message": "Candidature enregistrée avec succès", "score": data["Score"]}), 200

@app.route("/candidatures", methods=["GET"])
def lister_candidatures():
    return jsonify(charger_json(CANDIDATURES_FILE))

@app.route("/inscription", methods=["POST"])
def inscription():
    data = request.json
    recruteurs = charger_json(RECRUTEURS_FILE)
    recruteurs.append(data)
    enregistrer_json(RECRUTEURS_FILE, recruteurs)
    return jsonify({"message": "Inscription réussie"}), 200

@app.route("/connexion", methods=["POST"])
def connexion():
    data = request.json
    for r in charger_json(RECRUTEURS_FILE):
        if r["email"] == data["email"] and r["motdepasse"] == data["motdepasse"]:
            return jsonify({"message": "Connexion réussie"}), 200
    return jsonify({"message": "Email ou mot de passe incorrect"}), 401

@app.route("/offres", methods=["POST"])
def ajouter_offre():
    data = request.json
    offres = charger_json(OFFRES_FILE)
    offres.append(data)
    enregistrer_json(OFFRES_FILE, offres)
    return jsonify({"message": "Offre ajoutée avec succès"}), 200

@app.route("/offres", methods=["GET"])
def lister_offres():
    return jsonify(charger_json(OFFRES_FILE))

if __name__ == "__main__":
    app.run(debug=True)