from account import Account

class Customer(Account):

    def __init__(self,name,mail_id,password) :
        super().__init__(name,mail_id,password)
        super().set_access(False)
        self.bookings = []
        self.history = []
        self.payment_detials = {'debit' : None,
                                'credit' : None
                                }
    
    def book_tickets(self):
        pass
    
    def __str__(self):
        return f"{self.name} ; {self.mail_id}"
    
    def print_history(self):
        for action,changes in self.history:
            print(f'{self.name} {action} : \n\t {changes.breif()}')