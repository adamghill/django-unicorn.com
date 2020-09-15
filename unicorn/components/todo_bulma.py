from django_unicorn.components import UnicornView


class TodoBulmaView(UnicornView):
    task = ""
    tasks = []

    def add(self):
        if self.task:
            self.tasks.append(self.task)
            self.task = ""
