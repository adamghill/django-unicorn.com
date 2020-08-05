from django_unicorn.components import UnicornView


class TodoBulmaView(UnicornView):
    task = ""
    tasks = []

    def add(self):
        self.tasks.append(self.task)
        self.task = ""
