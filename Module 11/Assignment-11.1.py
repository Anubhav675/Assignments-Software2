class Publication():
    def __init__(self, name):
        self.name = name


class Book(Publication):
    def __init__(self, name, author, page_count):
        super().__init__(name)
        self.author = author
        self.page_count = page_count

    def print_information(self):
        print(f'Name of Publication is {self.name} Name of author is {self.author} Number of pages = {self.page_count}')


class Magazine(Publication):
    def __init__(self, name, chief_editor):
        super().__init__(name)
        self.chief_editor = chief_editor

    def print_information(self):
        print(f'Name of Publication is {self.name} Name of chief editor is {self.chief_editor}')
