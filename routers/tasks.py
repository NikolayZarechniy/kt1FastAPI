from fastapi import APIRouter, HTTPException, status
from models import CreateTask, TaskVDB, TaskOut, Category

router = APIRouter(prefix="/tasks", tags=["tasks"])

tasks_db: list[TaskVDB] = [
    TaskVDB(
        id=1,
        title="Подготовить отчет",
        description="Квартальный отчет попроекту",
        is_completed=False,
        category=Category(name="Работа", color="blue"),
        internal_note="Служебная инфа (без апи)"
    )
]

@router.get("/", response_model=list[TaskOut])
def get_tasks():
    return tasks_db

@router.post("/", response_model=TaskOut, status_code=status.HTTP_201_CREATED)
def create_task(task_data: CreateTask):
    new_id = len(tasks_db) + 1
    new_task = TaskVDB(
        id=new_id,
        **task_data.model_dump(),
        internal_note="заметка админа"
    )
    tasks_db.append(new_task)
    return new_task

@router.get("/{task_id}", response_model=TaskOut)
def get_task(task_id: int):
    for task in tasks_db:
        if task.id == task_id:
            return task
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Ничего не найдено"
    )