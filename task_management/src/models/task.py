from dataclasses import dataclass
from datetime import datetime

@dataclass
class Task:
    name: str
    description: str
    priority: str
    created_at: datetime = datetime.now()
    
    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "priority": self.priority,
            "created_at": self.created_at.isoformat()
        }
    
    @staticmethod
    def from_dict(data):
        return Task(
            name=data["name"],
            description=data["description"],
            priority=data["priority"],
            created_at=datetime.fromisoformat(data["created_at"])
        )