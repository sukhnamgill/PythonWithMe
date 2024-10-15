class train:
    def __init__(self,ticket_no):
        self.ticket_no=ticket_no
    def book_ticket(self,vocher):
        print(f"Ticket no.{self.ticket_no} is booked sir, Congratulations now and yout discount voucher no is {vocher}")
    @staticmethod
    def status():
        print("The status is :The Train is on the proper time ")
    
obj=train(221233)
obj.book_ticket(122)
obj.status()
