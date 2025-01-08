from flask import Flask, render_template, request
from markupsafe import escape
import re

app = Flask(__name__)

def sanitize_input(data):
    """Nettoie les entrées utilisateur pour éviter les injections XSS."""
    return escape(data)

def is_valid_email(email):
    """Vérifie si une adresse email est valide."""
    return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None

@app.route('/')
def index():
    """Affiche le formulaire."""
    return render_template('form.html', data={}, errors={})

@app.route('/thanks', methods=['POST'])
def thanks():
    """Traite le formulaire et affiche une page de remerciement ou retourne des erreurs."""
    errors = {}
    data = {}

    # Récupérer et nettoyer les données
    data['first_name'] = sanitize_input(request.form.get('first_name', '').strip())
    data['last_name'] = sanitize_input(request.form.get('last_name', '').strip())
    data['email'] = sanitize_input(request.form.get('email', '').strip())
    data['country'] = sanitize_input(request.form.get('country', '').strip())
    data['message'] = sanitize_input(request.form.get('message', '').strip())
    data['gender'] = request.form.get('gender', '')
    data['subject'] = request.form.getlist('subject')
    honeypot = request.form.get('honeypot', '')

    # Validation
    if not data['first_name']:
        errors['first_name'] = "Prénom requis."
    if not data['last_name']:
        errors['last_name'] = "Nom requis."
    if not is_valid_email(data['email']):
        errors['email'] = "Email invalide."
    if not data['subject']:
        errors['subject'] = "Sujet requis."
    if honeypot:  # Vérification anti-spam
        errors['honeypot'] = "Spam détecté."

    # Si erreurs, renvoyer le formulaire avec erreurs et données précédentes
    if errors:
        return render_template('form.html', data=data, errors=errors)

    # Si tout est valide, afficher la page de remerciement
    return render_template('thanks.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
