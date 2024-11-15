from ..managers.task_manager import TaskManager

class Menu:
    def __init__(self):
        self.task_manager = TaskManager()
        self.options = {
            "1": self.add_task,
            "2": self.remove_task,
            "3": self.show_tasks,
            "4": self.process_tasks,
            "5": self.exit_program
        }

    def display_menu(self):
        print("\n=== Sistema de Gestión de Tareas ===")
        print("1. Agregar tarea")
        print("2. Eliminar tarea")
        print("3. Mostrar tareas")
        print("4. Procesar tareas")
        print("5. Salir")

    def run(self):
        while True:
            self.display_menu()
            choice = input("\nSeleccione una opción: ")
            action = self.options.get(choice)
            if action:
                action()
            else:
                print("Opción inválida")

    def add_task(self):
        name = input("Nombre de la tarea: ")
        description = input("Descripción: ")
        priority = input("Prioridad (alta/media/baja): ")
        
        if self.task_manager.add_task(name, description, priority):
            print("Tarea agregada exitosamente")
        else:
            print("Error en los datos ingresados")

    def remove_task(self):
        name = input("Nombre de la tarea a eliminar: ")
        if self.task_manager.remove_task(name):
            print("Tarea eliminada exitosamente")
        else:
            print("Tarea no encontrada")

    def show_tasks(self):
        tasks_by_priority = self.task_manager.get_tasks_by_priority()
        if not any(tasks_by_priority.values()):
            print("No hay tareas pendientes")
            return

        for priority in ["alta", "media", "baja"]:
            print(f"\nTareas de prioridad {priority}:")
            for task in tasks_by_priority[priority]:
                print(f"- {task.name}: {task.description}")

    def process_tasks(self):
        processed = self.task_manager.process_tasks()
        if processed:
            print("Tareas procesadas:")
            for task in processed:
                print(f"- {task.name}")
        else:
            print("No hay tareas para procesar")

    def exit_program(self):
        print("¡Hasta luego!")
        exit()