from typing import Dict
from uuid import UUID, uuid4
from datetime import datetime, timedelta
from app.schemas import Task

# Mocked in-memory database: dictionnaire UUID -> Task
db: Dict[UUID, Task] = {}

# Préremplir avec quelques tâches d'exemple (2) puis générer plusieurs tâches mockées
tid1 = uuid4()
db[tid1] = Task(
    id=tid1,
    title="Apprendre FastAPI",
    description="Suivre le tutoriel officiel et pratiquer",
    status="pending",
    created_at=datetime.utcnow(),
)

tid2 = uuid4()
db[tid2] = Task(
    id=tid2,
    title="Écrire le README",
    description="Documenter les endpoints et instructions de lancement",
    status="done",
    created_at=datetime.utcnow(),
)

# Générer 30 tâches supplémentaires mockées
statuses = ["pending", "in_progress", "done"]
for i in range(3, 33):
    tid = uuid4()
    db[tid] = Task(
        id=tid,
        title=f"Tâche #{i} - Exercice {i}",
        description=f"Description simulée pour la tâche numéro {i}.",
        status=statuses[i % len(statuses)],
        created_at=datetime.utcnow() - timedelta(days=i % 7, hours=i % 5, minutes=i * 3),
    )
