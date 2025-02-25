# Projet Merchex

Ce projet est une application Django pour gérer des listings et des groupes de musique.

## Installation

1. Clonez le dépôt :

   ```bash
   git clone https://github.com/votre-utilisateur/merchex.git
   ```

2. Naviguez dans le répertoire du projet :

   ```bash
   cd merchex
   ```

3. Créez et activez un environnement virtuel :

   ```bash
   python -m venv venv
   source venv/bin/activate  # Pour Windows: .\venv\Scripts\activate
   ```

4. Installez les dépendances :

   ```bash
   pip install -r requirements.txt
   ```

5. Appliquez les migrations :

   ```bash
   python manage.py migrate
   ```

6. Lancez le serveur de développement :
   ```bash
   python manage.py runserver
   ```

## Utilisation

- Accédez à l'application via `http://127.0.0.1:8000/`.
- Utilisez l'interface d'administration pour gérer les listings et les groupes de musique.

## Contribuer

1. Forkez le projet.
2. Créez une branche pour votre fonctionnalité (`git checkout -b feature/ma-fonctionnalité`).
3. Commitez vos modifications (`git commit -m 'Ajout de ma fonctionnalité'`).
4. Poussez votre branche (`git push origin feature/ma-fonctionnalité`).
5. Ouvrez une Pull Request.

## Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.
