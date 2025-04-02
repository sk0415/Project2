import threading

class Teller(threading.Thread):
    def __init__(self, id):
        super().__init__()
        self.id = id

    def run(self):
        print(f"Teller {self.id} is ready.")


class Customer(threading.Thread):
    def __init__(self, id):
        super().__init__()
        self.id = id

    def run(self):
        pass


def main():
    teller = Teller(0)
    customer = Customer(0)

    teller.start()
    customer.start()

    customer.join()
    teller.join()

if __name__ == "__main__":
    main()
