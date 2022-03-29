from account import Account

class Admin(Account):
    def __init__(self, name, mail_id, password):
        super().__init__(name, mail_id, password)
        super().set_access(True)
        self.history = []
    
    def add_theatre(self):
        pass
    
    def add_movie(self):
        pass