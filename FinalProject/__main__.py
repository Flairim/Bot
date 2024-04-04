from abc import ABC, abstractmethod
from Bot import Bot 

class UserInterface(ABC):
    
    @abstractmethod
    def display_message(self, message):
        pass
    
    @abstractmethod
    def get_user_input(self, prompt):
        pass

    @abstractmethod
    def run(self):
        pass


class ConsoleInterface(UserInterface):

    def __init__(self):
        self.bot = Bot()
        self.bot.book.load("auto_save")
        self.commands = ['Add', 'Search', 'Edit', 'Load', 'Remove', 'Save', 'Congratulate', 'View', 'Exit']

    def display_message(self, message):
        print(message)

    def get_user_input(self, prompt):
        return input(prompt).strip().lower()

    def run(self):
        self.display_message('Hello. I am your contact-assistant. What should I do with your contacts?')
        while True:
            action = self.get_user_input('Type help for list of commands or enter your command\n')
            
            if action == 'help':
                format_str = str('{:%s%d}' % ('^', 20))
                for command in self.commands:
                    self.display_message(format_str.format(command))
                action = self.get_user_input('')
                self.bot.handle(action)
                if action in ['add', 'remove', 'edit']:
                    self.bot.book.save("auto_save")
            else:
                self.bot.handle(action)
                if action in ['add', 'remove', 'edit']:
                    self.bot.book.save("auto_save")
            if action == 'exit':
                break

if __name__ == "__main__":
    interface = ConsoleInterface()
    interface.run()
