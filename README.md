# FastAPI Task API (petit exemple)

Ceci est une petite API de gestion de tâches pour démontrer FastAPI, Pydantic et une organisation en plusieurs fichiers.

Installation:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

Lancer le serveur en développement:

```bash
uvicorn app.main:app --reload
```

Endpoints principaux:

- `GET /health` — vérifie que l'API répond
- `GET /tasks` — liste toutes les tâches
- `GET /tasks/{task_id}` — récupère une tâche par `id`
- `POST /tasks` — créer une tâche
- `PUT /tasks/{task_id}` — remplacer une tâche
- `PATCH /tasks/{task_id}` — modifier partiellement une tâche
- `DELETE /tasks/{task_id}` — supprimer une tâche

Chaque tâche a les champs: `id`, `title`, `description`, `status`, `created_at`.

La base de données n'est pas persistante: les tâches sont en mémoire.
