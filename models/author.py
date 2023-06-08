class Author:

    def __init__(self, genre, author, completed = False,  id = None, ):
        self.description = genre
        self.user = author
        self.completed = completed
        self.id = id

    def mark_complete(self):
        self.completed = True