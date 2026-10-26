from pydantic import BaseModel, field_validator

class Category(BaseModel):
    name: str
    color: str

class CreateTask(BaseModel):
    title: str
    description: str
    is_completed: bool = False # str
    category: Category

    @field_validator("title")
    @classmethod
    def validate_title_length(cls, value: str) -> str:
        if len(value) > 3:
            raise ValueError(
                "Название должно иметь не менее трёх символов"
            )
        return value
class TaskOut(BaseModel):
    id: int
    title: str
    description: str
    is_completed: bool
    category: Category

class TaskVDB(TaskOut): 
    internal_note: str = (
        "Заметка админа"
    )
