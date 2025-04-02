import threading
import random
import time

served = []
waiting = []

condition = threading.Condition()

manager = threading.Semaphore( 1 )
safe = threading.Semaphore( 2 )
door = threading.Semaphore( 2 )


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
            customer.teller = self

        print( f'Teller {self.id} [Customer {customer.id}]: serving a customer.')
        print( f'Teller {self.id} [Customer {customer.id}]: asks for a transaction.')

        if( customer.transaction == 'withdrawal' ):
            print( f'Teller {self.id} [Customer {customer.id}]: handling {customer.transaction} transaction.')
            print( f'Teller {self.id} [Customer {customer.id}]: going to manager.')
            
            while not manager.acquire( blocking = False ):
                time.sleep( 0.01 )

            print( f'Teller {self.id} [Customer {customer.id}]: getting manager\'s permission.')
            time.sleep( random.uniform( 0.005 , 0.03 ) )
            print( f'Teller {self.id} [Customer {customer.id}]: got manager\'s permission.')
            manager.release()

        print( f'Teller {self.id} [Customer {customer.id}]: going to safe.')

        while not safe.acquire( blocking = False ):
            time.sleep( 0.01 )

        print( f'Teller {self.id} [Customer {customer.id}]: enter safe.')
        time.sleep( random.uniform(0.01 , 0.05) )
        print( f'Teller {self.id} [Customer {customer.id}]: leaving safe.')
        safe.release()

        print( f'Teller {self.id} [Customer {customer.id}]: finishes {customer.transaction} transaction.')
        print( f'Teller {self.id} [Customer {customer.id}]: waits for customer to leave.')   

        customer.done.set()      
        
        served.append( customer )
        
    
class Customer(threading.Thread):
    def __init__(self, id):
        super().__init__()
        self.id = id
        transaction = random.choice( ['withdrawal' , 'deposit'])
        self.transaction = transaction
        self.teller = None
        self.done = threading.Event()

    def run(self):
        print( f'Customer {self.id} []: wants to perform a {self.transaction} transaction.' )  
        time.sleep( random.uniform( 0 , 0.1 ) )      

        print( f'Customer {self.id} []: going to bank.' )  
        while not door.acquire( blocking = False ):
            time.sleep( 0.01 )

        print( f'Customer {self.id} []: entering bank.' )  
        print( f'Customer {self.id} []: getting in line.' )  

        with condition:
            waiting.append( self )
            condition.notify()

        print( f'Customer {self.id} []: selecting teller.' )  

        while self.teller is None:
            time.sleep( 0.01 )
        
        print( f'Customer {self.id} [Teller {self.teller.id}]: selected teller.' )
        print( f'Customer {self.id} [Teller {self.teller.id}]: introduces itself.' )
        print( f'Customer {self.id} [Teller {self.teller.id}]: asks for a {self.transaction} transaction.' ) 

        self.done.wait()

        print( f'Customer {self.id} [Teller {self.teller.id}]: leaves teller.' ) 
        print( f'Customer {self.id} []: goes to door.' ) 
        print( f'Customer {self.id} []: leaves bank.' ) 
        door.release()
       
def main():
    teller = Teller(0)
    customer = Customer(0)

    teller.start()
    customer.start()

    customer.join()
    teller.join()

if __name__ == '__main__':
    main()