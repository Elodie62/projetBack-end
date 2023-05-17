# projetBack-end

# Mon Projet

Projet Dev back python.
La base de donnée se trouve à la racine du projet. Elle est à importer dans phpmyadmin.
La connexion à la bdd se fait dans le fichier database (internals), il vous faudra peut être retirer le mdp et/ou changer le port :
host="localhost",
user="root",
password="root",
database="plannings",
port="8889"

# Setup

-> Clonez le dépôt : `git clone https://github.com/Elodie62/projetBack-end.git`

```bash
pip install -r requirements.txt
```

### Run with Uvicorn (python)

-> cd app

```bash
uvicorn main:app --reload
```

# Swagger

-> http://localhost:8000/docs#/

# Users

| username            | password       | role       |
| ------------------- | -------------- | ---------- |
| loic@poisot.com     | LoicPassword   | maintainer |
| elodie@leclercq.com | ElodiePassword | user       |
| admin@disney.com    | adminPassword  | admin      |

## Auteurs

- Elodie Leclercq - elodie602@free.fr
