

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_take(self, item):
        print(f'\nYou have picked up a {item.name}\n')
    
    def on_drop(self, item):
        print(f'\nYou have dropped a {item.name}')


    def __str__(self):
        return f'\nItem is {self.name}: {self.description}'