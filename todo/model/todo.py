# TODO: Add code here
class Todo:

    def __init__(self,code_id: int, title: str,descripction: str):
        self.code_id: int= code_id
        self.title: str= title
        self.description: str= descripction
        self.completed: bool= False
        self.tags: list[str]= []

    def mark_completed(self):
        self.completed = True

    def add_tag(self, tag: str):
        if tag not in self.tags:
            self.tags.append(tag)
    def __str__(self)->str:
        return f"el codigo es:{self.code_id} - y el titulo es {self.title}"
    class TodoBook:
        def __init__(self):
            self.todos: dict[int, Todo] = {}
        #def add_todo(self, title: str,description: str):







