from typing import List
from ..models.task import Task
from ..utils.file_handler import FileHandler
from ..utils.validators import TaskValidator

class TaskManager:
    def __init__(self):
        self.file_handler = FileHandler()
        self.tasks: List[Task] = []
        self.load_tasks()

    def load_tasks(self) -> None:
        self.tasks = self.file_handler.load_tasks()

    def save_tasks(self) -> None:
        self.file_handler.save_tasks(self.tasks)

    def add_task(self, name: str, description: str, priority: str) -> bool:
        if not all([
            TaskValidator.validate_name(name),
            TaskValidator.validate_description(description),
            TaskValidator.validate_priority(priority)
        ]):
            return False
        
        task = Task(name, description, priority)
        self.tasks.append(task)
        self.save_tasks()
        return True

    def remove_task(self, name: str) -> bool:
        initial_length = len(self.tasks)
        self.tasks = [task for task in self.tasks if task.name != name]
        if len(self.tasks) < initial_length:
            self.save_tasks()
            return True
        return False

    def get_tasks_by_priority(self) -> dict:
        return {
            "alta": [t for t in self.tasks if t.priority == "alta"],
            "media": [t for t in self.tasks if t.priority == "media"],
            "baja": [t for t in self.tasks if t.priority == "baja"]
        }

    def process_tasks(self) -> List[Task]:
        if not self.tasks:
            return []
        
        processed = []
        tasks_by_priority = self.get_tasks_by_priority()
        
        for priority in ["alta", "media", "baja"]:
            processed.extend(tasks_by_priority[priority])
        
        self.tasks = []
        self.save_tasks()
        return processed