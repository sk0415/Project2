import threading
import random

served = []
waiting = []

condition = threading.Condition()

class Teller(threading.Thread):
    def __init__(self, id):
        super().__init__()
        self.id = id

    def run(self):
        print( f'Teller {self.id} []: ready to serve' )
        print( f'Teller {self.id} []: waiting for a customer' )
        # while True:
        with condition:
            while not waiting:
                condition.wait()
            
            customer = waiting.pop( 0 )
            print( f'Teller {self.id} [{customer.id}]: serving a customer.')
            print( f'Teller {self.id} [{customer.id}]: asks for a {customer.transaction}.')
            served.append( customer )
                
                


class Customer(threading.Thread):
    def __init__(self, id):
        super().__init__()
        self.id = id
        transaction = random.choice( ['withdrawal' , 'deposit'])
        self.transaction = transaction

    def run(self):
        print( f'Customer {self.id} []: wants to perform a {self.transaction} transaction.' )        
        with condition:
            waiting.append( self )

       
def main():
    teller = Teller(0)
    customer = Customer(0)

    teller.start()
    customer.start()

    customer.join()
    teller.join()

if __name__ == '__main__':
    main()
