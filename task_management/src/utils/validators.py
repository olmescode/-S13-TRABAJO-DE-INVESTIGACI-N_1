class TaskValidator:
    VALID_PRIORITIES = ["alta", "media", "baja"]

    @staticmethod
    def validate_priority(priority: str) -> bool:
        return priority.lower() in TaskValidator.VALID_PRIORITIES

    @staticmethod
    def validate_name(name: str) -> bool:
        return bool(name.strip())

    @staticmethod
    def validate_description(description: str) -> bool:
        return bool(description.strip())