class Account:
    def __init__(self,name,mail_id,password):
        self.name = name
        self.mail_id = mail_id
        self.password = password
        is_admin = False

    def __str__(self):
        return (f'name : {self.name} \nmail id : {self.mail_id}')
    
    def set_access(self,value):
        self.is_admin = value
