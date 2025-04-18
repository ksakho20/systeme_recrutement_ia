# route_affichage.py
from flask import Flask, jsonify
import csv

app = Flask(__name__)

@app.route('/candidatures', methods=['GET'])
def afficher_candidatures():
    candidatures = []
    try:
        with open('candidatures.csv', newline='', encoding='utf-8') as csvfile:
            lecteur = csv.DictReader(csvfile)
            for ligne in lecteur:
                candidatures.append(ligne)
    except FileNotFoundError:
        return jsonify({"message": "Aucune candidature enregistrée."}), 404

    return jsonify(candidatures)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
