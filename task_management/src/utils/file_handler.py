from pathlib import Path
from typing import List
from ..models.task import Task
import json

class FileHandler:
    def __init__(self, filename: str = "data/tasks.json"):
        self.filename = Path(filename)
        self.filename.parent.mkdir(exist_ok=True)
        
        # Initialize file if it doesn't exist
        if not self.filename.exists():
            with open(self.filename, 'w', encoding='utf-8') as f:
                json.dump([], f)

    def save_tasks(self, tasks: List[Task]) -> None:
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump([task.to_dict() for task in tasks], f, indent=2)

    def load_tasks(self) -> List[Task]:
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return [Task.from_dict(task_dict) for task_dict in data]
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            # If file is corrupted, initialize with empty list
            with open(self.filename, 'w', encoding='utf-8') as f:
                json.dump([], f)
            return []