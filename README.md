**Current Files**
- bank.py : This file contains all of the necessary code related to the project. It follows all of the specifications as given by the CS 4348 Project 2 document. It contains a Customer and Teller class which are implemented through threads and communicate with each other. There are 3 Tellers that serve 50 customers. Semaphores are used to implement times where there is a limit of how many people can enter (safe, talking to manager, fit through the door).
- devlog.md : This file contains a detailed breakdown of the process of building the multithreaded bank simulation.

**How to Compile**
In the command line, cd into the directory where this project resides and run 'python bank.py'. No other parameters are needed.

**Sample Run**
Teller 0 []: ready to serve
Teller 0 []: waiting for a customer
Teller 1 []: ready to serve
Teller 1 []: waiting for a customer
Teller 2 []: ready to serve
Teller 2 []: waiting for a customer
Customer 0 []: wants to perform a deposit transaction.
Customer 1 []: wants to perform a deposit transaction.
Customer 2 []: wants to perform a withdrawal transaction.
Customer 3 []: wants to perform a withdrawal transaction.
Customer 4 []: wants to perform a deposit transaction.
Customer 5 []: wants to perform a withdrawal transaction.
Customer 6 []: wants to perform a withdrawal transaction.
Customer 7 []: wants to perform a deposit transaction.
Customer 8 []: wants to perform a withdrawal transaction.
Customer 9 []: wants to perform a deposit transaction.
Customer 10 []: wants to perform a deposit transaction.
Customer 12 []: wants to perform a deposit transaction.
Customer 13 []: wants to perform a deposit transaction.
Customer 11 []: wants to perform a withdrawal transaction.
Customer 14 []: wants to perform a withdrawal transaction.
Customer 15 []: wants to perform a deposit transaction.
Customer 16 []: wants to perform a withdrawal transaction.
Customer 17 []: wants to perform a deposit transaction.
Customer 13 []: going to bank.
Customer 13 []: entering bank.
Customer 19 []: wants to perform a withdrawal transaction.
Customer 13 []: getting in line.
Customer 18 []: wants to perform a deposit transaction.
Customer 21 []: wants to perform a deposit transaction.
Customer 22 []: wants to perform a deposit transaction.
Customer 20 []: wants to perform a deposit transaction.
Teller 1 [Customer 13]: serving a customer
Customer 13 []: selecting a teller.
Customer 23 []: wants to perform a deposit transaction.
Customer 13 [Teller 1]: selects teller
Customer 13 [Teller 1] introduces itself
Customer 24 []: wants to perform a deposit transaction.
Customer 26 []: wants to perform a withdrawal transaction.
Customer 25 []: wants to perform a withdrawal transaction.
Customer 27 []: wants to perform a withdrawal transaction.
Customer 28 []: wants to perform a withdrawal transaction.
Customer 29 []: wants to perform a deposit transaction.
Customer 30 []: wants to perform a deposit transaction.
Customer 31 []: wants to perform a deposit transaction.
Teller 1 [Customer 13]: asks for transaction
Customer 32 []: wants to perform a deposit transaction.
Customer 33 []: wants to perform a deposit transaction.
Customer 13 [Teller 1]: asks for deposit transaction
Customer 34 []: wants to perform a deposit transaction.
Teller 1 [Customer 13]: handling deposit transaction
Teller 1 [Customer 13]: going to safe
Customer 35 []: wants to perform a withdrawal transaction.
Teller 1 [Customer 13]: enter safe
Customer 36 []: wants to perform a deposit transaction.
Customer 37 []: wants to perform a deposit transaction.
Customer 38 []: wants to perform a deposit transaction.
Customer 39 []: wants to perform a deposit transaction.
Customer 40 []: wants to perform a deposit transaction.
Customer 41 []: wants to perform a withdrawal transaction.
Customer 42 []: wants to perform a withdrawal transaction.
Customer 43 []: wants to perform a withdrawal transaction.
Customer 44 []: wants to perform a withdrawal transaction.
Customer 45 []: wants to perform a withdrawal transaction.
Customer 46 []: wants to perform a withdrawal transaction.
Customer 47 []: wants to perform a withdrawal transaction.
Customer 48 []: wants to perform a withdrawal transaction.
Customer 49 []: wants to perform a deposit transaction.
Customer 4 []: going to bank.
Customer 4 []: entering bank.
Customer 4 []: getting in line.
Customer 4 []: selecting a teller.
Teller 2 [Customer 4]: serving a customer
Customer 4 [Teller 2]: selects teller
Customer 4 [Teller 2] introduces itself
Teller 2 [Customer 4]: asks for transaction
Customer 4 [Teller 2]: asks for deposit transaction
Teller 2 [Customer 4]: handling deposit transaction
Teller 2 [Customer 4]: going to safe
Teller 2 [Customer 4]: enter safe
Customer 8 []: going to bank.
Customer 8 []: entering bank.
Customer 8 []: getting in line.
Customer 8 []: selecting a teller.
Customer 8 [Teller 0]: selects teller
Customer 8 [Teller 0] introduces itself
Teller 0 [Customer 8]: serving a customer
Teller 0 [Customer 8]: asks for transaction
Customer 8 [Teller 0]: asks for withdrawal transaction
Teller 0 [Customer 8]: handling withdrawal transaction
Teller 0 [Customer 8]: going to manager
Teller 0 [Customer 8]: getting manager's permission
Customer 49 []: going to bank.
Customer 49 []: entering bank.
Customer 49 []: getting in line.
Customer 49 []: selecting a teller.
Customer 32 []: going to bank.
Customer 32 []: entering bank.
Customer 32 []: getting in line.
Customer 32 []: selecting a teller.
Customer 20 []: going to bank.
Customer 20 []: entering bank.
Customer 20 []: getting in line.
Customer 20 []: selecting a teller.
Customer 26 []: going to bank.
Customer 26 []: entering bank.
Customer 26 []: getting in line.
Customer 26 []: selecting a teller.
Customer 21 []: going to bank.
Customer 21 []: entering bank.
Customer 21 []: getting in line.
Customer 21 []: selecting a teller.
Customer 47 []: going to bank.
Customer 47 []: entering bank.
Customer 47 []: getting in line.
Customer 47 []: selecting a teller.
Customer 39 []: going to bank.
Customer 39 []: entering bank.
Customer 39 []: getting in line.
Customer 39 []: selecting a teller.
Customer 24 []: going to bank.
Customer 24 []: entering bank.
Customer 24 []: getting in line.
Customer 24 []: selecting a teller.
Customer 43 []: going to bank.
Customer 43 []: entering bank.
Customer 42 []: going to bank.
Customer 43 []: getting in line.
Customer 42 []: entering bank.
Customer 42 []: getting in line.
Customer 42 []: selecting a teller.
Customer 43 []: selecting a teller.
Customer 7 []: going to bank.
Customer 7 []: entering bank.
Customer 7 []: getting in line.
Customer 7 []: selecting a teller.
Customer 27 []: going to bank.
Customer 27 []: entering bank.
Customer 27 []: getting in line.
Customer 27 []: selecting a teller.
Teller 0 [Customer 8]: got manager's permission
Teller 0 [Customer 8]: going to safe
Customer 30 []: going to bank.
Customer 30 []: entering bank.
Customer 30 []: getting in line.
Customer 30 []: selecting a teller.
Customer 15 []: going to bank.
Customer 15 []: entering bank.
Customer 15 []: getting in line.
Customer 15 []: selecting a teller.
Customer 31 []: going to bank.
Customer 31 []: entering bank.
Customer 31 []: getting in line.
Customer 31 []: selecting a teller.
Customer 40 []: going to bank.
Customer 40 []: entering bank.
Customer 40 []: getting in line.
Customer 40 []: selecting a teller.
Customer 11 []: going to bank.
Customer 11 []: entering bank.
Customer 11 []: getting in line.
Customer 11 []: selecting a teller.
Customer 23 []: going to bank.
Customer 23 []: entering bank.
Customer 23 []: getting in line.
Customer 23 []: selecting a teller.
Customer 16 []: going to bank.
Customer 16 []: entering bank.
Customer 16 []: getting in line.
Customer 16 []: selecting a teller.
Customer 18 []: going to bank.
Customer 18 []: entering bank.
Customer 18 []: getting in line.
Customer 25 []: going to bank.
Teller 1 [Customer 13]: leaving safe
Teller 1 [Customer 13]: finishes deposit transaction.
Teller 1 [Customer 13]: wait for customer to leave.
Teller 1 [Customer 18]: serving a customer
Customer 18 []: selecting a teller.
Customer 13 [Teller 1]: leaves teller
Customer 13 []: goes to door
Customer 13 []: leaves the bank
Customer 25 []: entering bank.
Customer 25 []: getting in line.
Customer 0 []: going to bank.
Customer 25 []: selecting a teller.
Customer 0 []: entering bank.
Customer 0 []: getting in line.
Customer 0 []: selecting a teller.
Customer 18 [Teller 1]: selects teller
Customer 18 [Teller 1] introduces itself
Teller 1 [Customer 18]: asks for transaction
Customer 18 [Teller 1]: asks for deposit transaction
Teller 1 [Customer 18]: handling deposit transaction
Teller 1 [Customer 18]: going to safe
Teller 1 [Customer 18]: enter safe
Customer 9 []: going to bank.
Customer 9 []: entering bank.
Customer 9 []: getting in line.
Customer 9 []: selecting a teller.
Teller 2 [Customer 4]: leaving safe
Teller 2 [Customer 4]: finishes deposit transaction.
Teller 2 [Customer 4]: wait for customer to leave.
Teller 2 [Customer 9]: serving a customer
Customer 4 [Teller 2]: leaves teller
Customer 4 []: goes to door
Customer 4 []: leaves the bank
Teller 0 [Customer 8]: enter safe
Customer 45 []: going to bank.
Customer 45 []: entering bank.
Customer 45 []: getting in line.
Customer 45 []: selecting a teller.
Customer 9 [Teller 2]: selects teller
Customer 9 [Teller 2] introduces itself
Teller 2 [Customer 9]: asks for transaction
Customer 19 []: going to bank.
Customer 9 [Teller 2]: asks for deposit transaction
Customer 19 []: entering bank.
Teller 2 [Customer 9]: handling deposit transaction
Customer 19 []: getting in line.
Teller 2 [Customer 9]: going to safe
Customer 19 []: selecting a teller.
Customer 3 []: going to bank.
Customer 3 []: entering bank.
Customer 3 []: getting in line.
Customer 3 []: selecting a teller.
Customer 14 []: going to bank.
Customer 14 []: entering bank.
Customer 14 []: getting in line.
Customer 14 []: selecting a teller.
Customer 10 []: going to bank.
Customer 10 []: entering bank.
Customer 10 []: getting in line.
Customer 34 []: going to bank.
Customer 10 []: selecting a teller.
Customer 34 []: entering bank.
Customer 48 []: going to bank.
Customer 34 []: getting in line.
Customer 48 []: entering bank.
Customer 34 []: selecting a teller.
Customer 48 []: getting in line.
Customer 48 []: selecting a teller.
Teller 0 [Customer 8]: leaving safe
Customer 33 []: going to bank.
Teller 0 [Customer 8]: finishes withdrawal transaction.
Customer 33 []: entering bank.
Teller 0 [Customer 8]: wait for customer to leave.
Teller 0 [Customer 48]: serving a customer
Customer 33 []: getting in line.
Customer 8 [Teller 0]: leaves teller
Customer 33 []: selecting a teller.
Customer 8 []: goes to door
Customer 8 []: leaves the bank
Teller 2 [Customer 9]: enter safe
Customer 44 []: going to bank.
Customer 44 []: entering bank.
Customer 44 []: getting in line.
Customer 44 []: selecting a teller.
Customer 46 []: going to bank.
Customer 46 []: entering bank.
Customer 46 []: getting in line.
Customer 46 []: selecting a teller.
Customer 6 []: going to bank.
Customer 6 []: entering bank.
Customer 6 []: getting in line.
Customer 6 []: selecting a teller.
Customer 28 []: going to bank.
Customer 28 []: entering bank.
Customer 28 []: getting in line.
Customer 28 []: selecting a teller.
Customer 48 [Teller 0]: selects teller
Customer 48 [Teller 0] introduces itself
Teller 0 [Customer 48]: asks for transaction
Customer 48 [Teller 0]: asks for withdrawal transaction
Teller 0 [Customer 48]: handling withdrawal transaction
Teller 0 [Customer 48]: going to manager
Teller 0 [Customer 48]: getting manager's permission
Teller 1 [Customer 18]: leaving safe
Teller 1 [Customer 18]: finishes deposit transaction.
Teller 1 [Customer 18]: wait for customer to leave.
Teller 1 [Customer 28]: serving a customer
Customer 18 [Teller 1]: leaves teller
Customer 18 []: goes to door
Customer 18 []: leaves the bank
Customer 5 []: going to bank.
Customer 38 []: going to bank.
Customer 5 []: entering bank.
Customer 5 []: getting in line.
Customer 5 []: selecting a teller.
Customer 38 []: entering bank.
Customer 38 []: getting in line.
Customer 38 []: selecting a teller.
Customer 29 []: going to bank.
Customer 29 []: entering bank.
Customer 29 []: getting in line.
Customer 29 []: selecting a teller.
Customer 35 []: going to bank.
Customer 35 []: entering bank.
Customer 35 []: getting in line.
Customer 35 []: selecting a teller.
Customer 1 []: going to bank.
Customer 1 []: entering bank.
Customer 1 []: getting in line.
Customer 1 []: selecting a teller.
Customer 22 []: going to bank.
Customer 22 []: entering bank.
Customer 22 []: getting in line.
Customer 22 []: selecting a teller.
Customer 28 [Teller 1]: selects teller
Customer 28 [Teller 1] introduces itself
Teller 1 [Customer 28]: asks for transaction
Customer 17 []: going to bank.
Customer 28 [Teller 1]: asks for withdrawal transaction
Customer 17 []: entering bank.
Teller 1 [Customer 28]: handling withdrawal transaction
Customer 17 []: getting in line.
Customer 17 []: selecting a teller.
Teller 1 [Customer 28]: going to manager
Customer 12 []: going to bank.
Customer 12 []: entering bank.
Customer 12 []: getting in line.
Customer 12 []: selecting a teller.
Customer 36 []: going to bank.
Customer 36 []: entering bank.
Customer 36 []: getting in line.
Customer 36 []: selecting a teller.
Customer 41 []: going to bank.
Customer 2 []: going to bank.
Customer 41 []: entering bank.
Customer 2 []: entering bank.
Customer 41 []: getting in line.
Customer 2 []: getting in line.
Customer 2 []: selecting a teller.
Customer 41 []: selecting a teller.
Teller 0 [Customer 48]: got manager's permission
Teller 0 [Customer 48]: going to safe
Teller 0 [Customer 48]: enter safe
Customer 37 []: going to bank.
Customer 37 []: entering bank.
Customer 37 []: getting in line.
Customer 37 []: selecting a teller.
Teller 2 [Customer 9]: leaving safe
Teller 2 [Customer 9]: finishes deposit transaction.
Teller 2 [Customer 9]: wait for customer to leave.
Teller 2 [Customer 37]: serving a customer
Customer 9 [Teller 2]: leaves teller
Customer 9 []: goes to door
Customer 9 []: leaves the bank
Teller 1 [Customer 28]: getting manager's permission
Customer 37 [Teller 2]: selects teller
Customer 37 [Teller 2] introduces itself
Teller 2 [Customer 37]: asks for transaction
Customer 37 [Teller 2]: asks for deposit transaction
Teller 2 [Customer 37]: handling deposit transaction
Teller 2 [Customer 37]: going to safe
Teller 2 [Customer 37]: enter safe
Teller 2 [Customer 37]: leaving safe
Teller 2 [Customer 37]: finishes deposit transaction.
Teller 2 [Customer 37]: wait for customer to leave.
Teller 2 [Customer 2]: serving a customer
Customer 37 [Teller 2]: leaves teller
Customer 37 []: goes to door
Customer 37 []: leaves the bank
Teller 1 [Customer 28]: got manager's permission
Teller 1 [Customer 28]: going to safe
Teller 1 [Customer 28]: enter safe
Customer 2 [Teller 2]: selects teller
Customer 2 [Teller 2] introduces itself
Teller 2 [Customer 2]: asks for transaction
Customer 2 [Teller 2]: asks for withdrawal transaction
Teller 2 [Customer 2]: handling withdrawal transaction
Teller 2 [Customer 2]: going to manager
Teller 2 [Customer 2]: getting manager's permission
Teller 0 [Customer 48]: leaving safe
Teller 0 [Customer 48]: finishes withdrawal transaction.
Teller 0 [Customer 48]: wait for customer to leave.
Teller 0 [Customer 41]: serving a customer
Customer 48 [Teller 0]: leaves teller
Customer 48 []: goes to door
Customer 48 []: leaves the bank
Customer 41 [Teller 0]: selects teller
Customer 41 [Teller 0] introduces itself
Teller 0 [Customer 41]: asks for transaction
Customer 41 [Teller 0]: asks for withdrawal transaction
Teller 0 [Customer 41]: handling withdrawal transaction
Teller 0 [Customer 41]: going to manager
Teller 1 [Customer 28]: leaving safe
Teller 1 [Customer 28]: finishes withdrawal transaction.
Teller 1 [Customer 28]: wait for customer to leave.
Teller 1 [Customer 36]: serving a customer
Customer 28 [Teller 1]: leaves teller
Customer 28 []: goes to door
Customer 28 []: leaves the bank
Customer 36 [Teller 1]: selects teller
Customer 36 [Teller 1] introduces itself
Teller 1 [Customer 36]: asks for transaction
Customer 36 [Teller 1]: asks for deposit transaction
Teller 1 [Customer 36]: handling deposit transaction
Teller 1 [Customer 36]: going to safe
Teller 1 [Customer 36]: enter safe
Teller 2 [Customer 2]: got manager's permission
Teller 2 [Customer 2]: going to safe
Teller 2 [Customer 2]: enter safe
Teller 0 [Customer 41]: getting manager's permission
Teller 1 [Customer 36]: leaving safe
Teller 1 [Customer 36]: finishes deposit transaction.
Teller 1 [Customer 36]: wait for customer to leave.
Teller 1 [Customer 12]: serving a customer
Customer 36 [Teller 1]: leaves teller
Customer 36 []: goes to door
Customer 36 []: leaves the bank
Teller 0 [Customer 41]: got manager's permission
Teller 0 [Customer 41]: going to safe
Teller 0 [Customer 41]: enter safe
Customer 12 [Teller 1]: selects teller
Customer 12 [Teller 1] introduces itself
Teller 1 [Customer 12]: asks for transaction
Customer 12 [Teller 1]: asks for deposit transaction
Teller 1 [Customer 12]: handling deposit transaction
Teller 1 [Customer 12]: going to safe
Teller 2 [Customer 2]: leaving safe
Teller 2 [Customer 2]: finishes withdrawal transaction.
Teller 2 [Customer 2]: wait for customer to leave.
Teller 2 [Customer 17]: serving a customer
Customer 2 [Teller 2]: leaves teller
Customer 2 []: goes to door
Customer 2 []: leaves the bank
Customer 17 [Teller 2]: selects teller
Customer 17 [Teller 2] introduces itself
Teller 2 [Customer 17]: asks for transaction
Customer 17 [Teller 2]: asks for deposit transaction
Teller 2 [Customer 17]: handling deposit transaction
Teller 2 [Customer 17]: going to safe
Teller 2 [Customer 17]: enter safe
Teller 0 [Customer 41]: leaving safe
Teller 0 [Customer 41]: finishes withdrawal transaction.
Teller 0 [Customer 41]: wait for customer to leave.
Teller 0 [Customer 22]: serving a customer
Customer 41 [Teller 0]: leaves teller
Customer 41 []: goes to door
Customer 41 []: leaves the bank
Teller 1 [Customer 12]: enter safe
Customer 22 [Teller 0]: selects teller
Customer 22 [Teller 0] introduces itself
Teller 0 [Customer 22]: asks for transaction
Customer 22 [Teller 0]: asks for deposit transaction
Teller 0 [Customer 22]: handling deposit transaction
Teller 0 [Customer 22]: going to safe
Teller 2 [Customer 17]: leaving safe
Teller 2 [Customer 17]: finishes deposit transaction.
Teller 2 [Customer 17]: wait for customer to leave.
Teller 2 [Customer 1]: serving a customer
Customer 17 [Teller 2]: leaves teller
Customer 17 []: goes to door
Customer 17 []: leaves the bank
Teller 1 [Customer 12]: leaving safe
Teller 1 [Customer 12]: finishes deposit transaction.
Teller 1 [Customer 12]: wait for customer to leave.
Teller 1 [Customer 35]: serving a customer
Customer 12 [Teller 1]: leaves teller
Customer 12 []: goes to door
Customer 12 []: leaves the bank
Customer 1 [Teller 2]: selects teller
Customer 1 [Teller 2] introduces itself
Teller 2 [Customer 1]: asks for transaction
Customer 1 [Teller 2]: asks for deposit transaction
Teller 0 [Customer 22]: enter safe
Teller 2 [Customer 1]: handling deposit transaction
Teller 2 [Customer 1]: going to safe
Teller 2 [Customer 1]: enter safe
Customer 35 [Teller 1]: selects teller
Customer 35 [Teller 1] introduces itself
Teller 1 [Customer 35]: asks for transaction
Customer 35 [Teller 1]: asks for withdrawal transaction
Teller 1 [Customer 35]: handling withdrawal transaction
Teller 1 [Customer 35]: going to manager
Teller 1 [Customer 35]: getting manager's permission
Teller 1 [Customer 35]: got manager's permission
Teller 1 [Customer 35]: going to safe
Teller 2 [Customer 1]: leaving safe
Teller 2 [Customer 1]: finishes deposit transaction.
Teller 2 [Customer 1]: wait for customer to leave.
Teller 2 [Customer 29]: serving a customer
Customer 1 [Teller 2]: leaves teller
Customer 1 []: goes to door
Customer 1 []: leaves the bank
Customer 29 [Teller 2]: selects teller
Customer 29 [Teller 2] introduces itself
Teller 2 [Customer 29]: asks for transaction
Customer 29 [Teller 2]: asks for deposit transaction
Teller 2 [Customer 29]: handling deposit transaction
Teller 2 [Customer 29]: going to safe
Teller 0 [Customer 22]: leaving safe
Teller 2 [Customer 29]: enter safe
Teller 0 [Customer 22]: finishes deposit transaction.
Teller 0 [Customer 22]: wait for customer to leave.
Teller 0 [Customer 38]: serving a customer
Customer 22 [Teller 0]: leaves teller
Customer 22 []: goes to door
Customer 22 []: leaves the bank
Teller 1 [Customer 35]: enter safe
Customer 38 [Teller 0]: selects teller
Customer 38 [Teller 0] introduces itself
Teller 0 [Customer 38]: asks for transaction
Customer 38 [Teller 0]: asks for deposit transaction
Teller 0 [Customer 38]: handling deposit transaction
Teller 0 [Customer 38]: going to safe
Teller 1 [Customer 35]: leaving safe
Teller 1 [Customer 35]: finishes withdrawal transaction.
Teller 1 [Customer 35]: wait for customer to leave.
Teller 1 [Customer 5]: serving a customer
Customer 35 [Teller 1]: leaves teller
Customer 35 []: goes to door
Customer 35 []: leaves the bank
Customer 5 [Teller 1]: selects teller
Customer 5 [Teller 1] introduces itself
Teller 1 [Customer 5]: asks for transaction
Customer 5 [Teller 1]: asks for withdrawal transaction
Teller 1 [Customer 5]: handling withdrawal transaction
Teller 1 [Customer 5]: going to manager
Teller 1 [Customer 5]: getting manager's permission
Teller 0 [Customer 38]: enter safe
Teller 2 [Customer 29]: leaving safe
Teller 2 [Customer 29]: finishes deposit transaction.
Teller 2 [Customer 29]: wait for customer to leave.
Teller 2 [Customer 6]: serving a customer
Customer 29 [Teller 2]: leaves teller
Customer 29 []: goes to door
Customer 29 []: leaves the bank
Teller 1 [Customer 5]: got manager's permission
Teller 1 [Customer 5]: going to safe
Teller 1 [Customer 5]: enter safe
Teller 0 [Customer 38]: leaving safe
Teller 0 [Customer 38]: finishes deposit transaction.
Teller 0 [Customer 38]: wait for customer to leave.
Teller 0 [Customer 46]: serving a customer
Customer 38 [Teller 0]: leaves teller
Customer 38 []: goes to door
Customer 38 []: leaves the bank
Customer 46 [Teller 0]: selects teller
Customer 46 [Teller 0] introduces itself
Teller 0 [Customer 46]: asks for transaction
Customer 46 [Teller 0]: asks for withdrawal transaction
Teller 0 [Customer 46]: handling withdrawal transaction
Teller 0 [Customer 46]: going to manager
Teller 0 [Customer 46]: getting manager's permission
Customer 6 [Teller 2]: selects teller
Customer 6 [Teller 2] introduces itself
Teller 2 [Customer 6]: asks for transaction
Customer 6 [Teller 2]: asks for withdrawal transaction
Teller 2 [Customer 6]: handling withdrawal transaction
Teller 2 [Customer 6]: going to manager
Teller 0 [Customer 46]: got manager's permission
Teller 0 [Customer 46]: going to safe
Teller 0 [Customer 46]: enter safe
Teller 1 [Customer 5]: leaving safe
Teller 1 [Customer 5]: finishes withdrawal transaction.
Teller 1 [Customer 5]: wait for customer to leave.
Teller 1 [Customer 44]: serving a customer
Customer 5 [Teller 1]: leaves teller
Customer 5 []: goes to door
Customer 5 []: leaves the bank
Customer 44 [Teller 1]: selects teller
Customer 44 [Teller 1] introduces itself
Teller 1 [Customer 44]: asks for transaction
Customer 44 [Teller 1]: asks for withdrawal transaction
Teller 1 [Customer 44]: handling withdrawal transaction
Teller 1 [Customer 44]: going to manager
Teller 1 [Customer 44]: getting manager's permission
Teller 1 [Customer 44]: got manager's permission
Teller 1 [Customer 44]: going to safe
Teller 1 [Customer 44]: enter safe
Teller 2 [Customer 6]: getting manager's permission
Teller 0 [Customer 46]: leaving safe
Teller 0 [Customer 46]: finishes withdrawal transaction.
Teller 0 [Customer 46]: wait for customer to leave.
Teller 0 [Customer 33]: serving a customer
Customer 46 [Teller 0]: leaves teller
Customer 46 []: goes to door
Customer 46 []: leaves the bank
Customer 33 [Teller 0]: selects teller
Customer 33 [Teller 0] introduces itself
Teller 0 [Customer 33]: asks for transaction
Customer 33 [Teller 0]: asks for deposit transaction
Teller 0 [Customer 33]: handling deposit transaction
Teller 0 [Customer 33]: going to safe
Teller 0 [Customer 33]: enter safe
Teller 2 [Customer 6]: got manager's permission
Teller 2 [Customer 6]: going to safe
Teller 1 [Customer 44]: leaving safe
Teller 1 [Customer 44]: finishes withdrawal transaction.
Teller 1 [Customer 44]: wait for customer to leave.
Teller 1 [Customer 34]: serving a customer
Customer 44 [Teller 1]: leaves teller
Customer 44 []: goes to door
Customer 44 []: leaves the bank
Customer 34 [Teller 1]: selects teller
Customer 34 [Teller 1] introduces itself
Teller 1 [Customer 34]: asks for transaction
Customer 34 [Teller 1]: asks for deposit transaction
Teller 1 [Customer 34]: handling deposit transaction
Teller 1 [Customer 34]: going to safe
Teller 2 [Customer 6]: enter safe
Teller 2 [Customer 6]: leaving safe
Teller 2 [Customer 6]: finishes withdrawal transaction.
Teller 2 [Customer 6]: wait for customer to leave.
Teller 2 [Customer 10]: serving a customer
Customer 6 [Teller 2]: leaves teller
Customer 6 []: goes to door
Customer 6 []: leaves the bank
Teller 1 [Customer 34]: enter safe
Teller 0 [Customer 33]: leaving safe
Teller 0 [Customer 33]: finishes deposit transaction.
Teller 0 [Customer 33]: wait for customer to leave.
Teller 0 [Customer 14]: serving a customer
Customer 33 [Teller 0]: leaves teller
Customer 33 []: goes to door
Customer 33 []: leaves the bank
Customer 10 [Teller 2]: selects teller
Customer 10 [Teller 2] introduces itself
Teller 2 [Customer 10]: asks for transaction
Customer 10 [Teller 2]: asks for deposit transaction
Teller 2 [Customer 10]: handling deposit transaction
Teller 2 [Customer 10]: going to safe
Teller 2 [Customer 10]: enter safe
Customer 14 [Teller 0]: selects teller
Customer 14 [Teller 0] introduces itself
Teller 0 [Customer 14]: asks for transaction
Customer 14 [Teller 0]: asks for withdrawal transaction
Teller 0 [Customer 14]: handling withdrawal transaction
Teller 0 [Customer 14]: going to manager
Teller 0 [Customer 14]: getting manager's permission
Teller 0 [Customer 14]: got manager's permission
Teller 0 [Customer 14]: going to safe
Teller 1 [Customer 34]: leaving safe
Teller 1 [Customer 34]: finishes deposit transaction.
Teller 1 [Customer 34]: wait for customer to leave.
Teller 1 [Customer 3]: serving a customer
Customer 34 [Teller 1]: leaves teller
Customer 34 []: goes to door
Customer 34 []: leaves the bank
Customer 3 [Teller 1]: selects teller
Customer 3 [Teller 1] introduces itself
Teller 2 [Customer 10]: leaving safe
Teller 1 [Customer 3]: asks for transaction
Teller 2 [Customer 10]: finishes deposit transaction.
Teller 2 [Customer 10]: wait for customer to leave.
Customer 3 [Teller 1]: asks for withdrawal transaction
Teller 2 [Customer 19]: serving a customer
Customer 10 [Teller 2]: leaves teller
Customer 10 []: goes to door
Teller 1 [Customer 3]: handling withdrawal transaction
Customer 10 []: leaves the bank
Teller 1 [Customer 3]: going to manager
Teller 1 [Customer 3]: getting manager's permission
Teller 0 [Customer 14]: enter safe
Customer 19 [Teller 2]: selects teller
Customer 19 [Teller 2] introduces itself
Teller 2 [Customer 19]: asks for transaction
Customer 19 [Teller 2]: asks for withdrawal transaction
Teller 2 [Customer 19]: handling withdrawal transaction
Teller 2 [Customer 19]: going to manager
Teller 1 [Customer 3]: got manager's permission
Teller 1 [Customer 3]: going to safe
Teller 1 [Customer 3]: enter safe
Teller 2 [Customer 19]: getting manager's permission
Teller 2 [Customer 19]: got manager's permission
Teller 2 [Customer 19]: going to safe
Teller 0 [Customer 14]: leaving safe
Teller 0 [Customer 14]: finishes withdrawal transaction.
Teller 0 [Customer 14]: wait for customer to leave.
Teller 0 [Customer 45]: serving a customer
Customer 14 [Teller 0]: leaves teller
Customer 45 [Teller 0]: selects teller
Customer 14 []: goes to door
Customer 45 [Teller 0] introduces itself
Customer 14 []: leaves the bank
Teller 0 [Customer 45]: asks for transaction
Customer 45 [Teller 0]: asks for withdrawal transaction
Teller 0 [Customer 45]: handling withdrawal transaction
Teller 0 [Customer 45]: going to manager
Teller 0 [Customer 45]: getting manager's permission
Teller 2 [Customer 19]: enter safe
Teller 1 [Customer 3]: leaving safe
Teller 1 [Customer 3]: finishes withdrawal transaction.
Teller 1 [Customer 3]: wait for customer to leave.
Teller 1 [Customer 0]: serving a customer
Teller 0 [Customer 45]: got manager's permission
Teller 0 [Customer 45]: going to safe
Teller 0 [Customer 45]: enter safe
Customer 3 [Teller 1]: leaves teller
Customer 3 []: goes to door
Customer 3 []: leaves the bank
Customer 0 [Teller 1]: selects teller
Customer 0 [Teller 1] introduces itself
Teller 1 [Customer 0]: asks for transaction
Customer 0 [Teller 1]: asks for deposit transaction
Teller 1 [Customer 0]: handling deposit transaction
Teller 1 [Customer 0]: going to safe
Teller 0 [Customer 45]: leaving safe
Teller 0 [Customer 45]: finishes withdrawal transaction.
Teller 0 [Customer 45]: wait for customer to leave.
Teller 0 [Customer 25]: serving a customer
Customer 45 [Teller 0]: leaves teller
Customer 45 []: goes to door
Customer 45 []: leaves the bank
Teller 2 [Customer 19]: leaving safe
Teller 2 [Customer 19]: finishes withdrawal transaction.
Teller 2 [Customer 19]: wait for customer to leave.
Teller 2 [Customer 16]: serving a customer
Customer 19 [Teller 2]: leaves teller
Customer 19 []: goes to door
Customer 19 []: leaves the bank
Customer 16 [Teller 2]: selects teller
Customer 16 [Teller 2] introduces itself
Teller 2 [Customer 16]: asks for transaction
Customer 16 [Teller 2]: asks for withdrawal transaction
Teller 2 [Customer 16]: handling withdrawal transaction
Teller 2 [Customer 16]: going to manager
Teller 2 [Customer 16]: getting manager's permission
Teller 1 [Customer 0]: enter safe
Customer 25 [Teller 0]: selects teller
Customer 25 [Teller 0] introduces itself
Teller 0 [Customer 25]: asks for transaction
Customer 25 [Teller 0]: asks for withdrawal transaction
Teller 0 [Customer 25]: handling withdrawal transaction
Teller 0 [Customer 25]: going to manager
Teller 2 [Customer 16]: got manager's permission
Teller 2 [Customer 16]: going to safe
Teller 2 [Customer 16]: enter safe
Teller 0 [Customer 25]: getting manager's permission
Teller 0 [Customer 25]: got manager's permission
Teller 0 [Customer 25]: going to safe
Teller 1 [Customer 0]: leaving safe
Teller 1 [Customer 0]: finishes deposit transaction.
Teller 1 [Customer 0]: wait for customer to leave.
Teller 1 [Customer 23]: serving a customer
Customer 0 [Teller 1]: leaves teller
Customer 0 []: goes to door
Customer 0 []: leaves the bank
Teller 2 [Customer 16]: leaving safe
Teller 2 [Customer 16]: finishes withdrawal transaction.
Teller 2 [Customer 16]: wait for customer to leave.
Teller 2 [Customer 11]: serving a customer
Customer 16 [Teller 2]: leaves teller
Customer 16 []: goes to door
Teller 0 [Customer 25]: enter safe
Customer 16 []: leaves the bank
Customer 11 [Teller 2]: selects teller
Customer 11 [Teller 2] introduces itself
Teller 2 [Customer 11]: asks for transaction
Customer 11 [Teller 2]: asks for withdrawal transaction
Teller 2 [Customer 11]: handling withdrawal transaction
Teller 2 [Customer 11]: going to manager
Teller 2 [Customer 11]: getting manager's permission
Customer 23 [Teller 1]: selects teller
Customer 23 [Teller 1] introduces itself
Teller 1 [Customer 23]: asks for transaction
Customer 23 [Teller 1]: asks for deposit transaction
Teller 1 [Customer 23]: handling deposit transaction
Teller 1 [Customer 23]: going to safe
Teller 1 [Customer 23]: enter safe
Teller 0 [Customer 25]: leaving safe
Teller 0 [Customer 25]: finishes withdrawal transaction.
Teller 0 [Customer 25]: wait for customer to leave.
Teller 0 [Customer 40]: serving a customer
Customer 25 [Teller 0]: leaves teller
Customer 25 []: goes to door
Customer 25 []: leaves the bank
Teller 2 [Customer 11]: got manager's permission
Teller 2 [Customer 11]: going to safe
Teller 2 [Customer 11]: enter safe
Customer 40 [Teller 0]: selects teller
Customer 40 [Teller 0] introduces itself
Teller 0 [Customer 40]: asks for transaction
Customer 40 [Teller 0]: asks for deposit transaction
Teller 0 [Customer 40]: handling deposit transaction
Teller 0 [Customer 40]: going to safe
Teller 2 [Customer 11]: leaving safe
Teller 2 [Customer 11]: finishes withdrawal transaction.
Teller 2 [Customer 11]: wait for customer to leave.
Teller 2 [Customer 31]: serving a customer
Customer 11 [Teller 2]: leaves teller
Customer 31 [Teller 2]: selects teller
Customer 31 [Teller 2] introduces itself
Customer 11 []: goes to door
Teller 2 [Customer 31]: asks for transaction
Customer 31 [Teller 2]: asks for deposit transaction
Teller 1 [Customer 23]: leaving safe
Teller 1 [Customer 23]: finishes deposit transaction.
Teller 1 [Customer 23]: wait for customer to leave.
Teller 2 [Customer 31]: handling deposit transaction
Teller 2 [Customer 31]: going to safe
Teller 0 [Customer 40]: enter safe
Teller 1 [Customer 15]: serving a customer
Teller 2 [Customer 31]: enter safe
Customer 11 []: leaves the bank
Customer 23 [Teller 1]: leaves teller
Customer 23 []: goes to door
Customer 23 []: leaves the bank
Customer 15 [Teller 1]: selects teller
Customer 15 [Teller 1] introduces itself
Teller 1 [Customer 15]: asks for transaction
Customer 15 [Teller 1]: asks for deposit transaction
Teller 1 [Customer 15]: handling deposit transaction
Teller 1 [Customer 15]: going to safe
Teller 2 [Customer 31]: leaving safe
Teller 2 [Customer 31]: finishes deposit transaction.
Teller 2 [Customer 31]: wait for customer to leave.
Teller 2 [Customer 30]: serving a customer
Customer 31 [Teller 2]: leaves teller
Customer 31 []: goes to door
Customer 31 []: leaves the bank
Teller 0 [Customer 40]: leaving safe
Teller 0 [Customer 40]: finishes deposit transaction.
Teller 0 [Customer 40]: wait for customer to leave.
Teller 0 [Customer 27]: serving a customer
Customer 40 [Teller 0]: leaves teller
Customer 40 []: goes to door
Customer 40 []: leaves the bank
Customer 30 [Teller 2]: selects teller
Customer 30 [Teller 2] introduces itself
Teller 2 [Customer 30]: asks for transaction
Customer 30 [Teller 2]: asks for deposit transaction
Teller 2 [Customer 30]: handling deposit transaction
Teller 2 [Customer 30]: going to safe
Teller 2 [Customer 30]: enter safe
Teller 1 [Customer 15]: enter safe
Customer 27 [Teller 0]: selects teller
Customer 27 [Teller 0] introduces itself
Teller 0 [Customer 27]: asks for transaction
Customer 27 [Teller 0]: asks for withdrawal transaction
Teller 0 [Customer 27]: handling withdrawal transaction
Teller 0 [Customer 27]: going to manager
Teller 0 [Customer 27]: getting manager's permission
Teller 2 [Customer 30]: leaving safe
Teller 2 [Customer 30]: finishes deposit transaction.
Teller 2 [Customer 30]: wait for customer to leave.
Teller 2 [Customer 7]: serving a customer
Customer 30 [Teller 2]: leaves teller
Customer 30 []: goes to door
Customer 30 []: leaves the bank
Customer 7 [Teller 2]: selects teller
Customer 7 [Teller 2] introduces itself
Teller 2 [Customer 7]: asks for transaction
Customer 7 [Teller 2]: asks for deposit transaction
Teller 2 [Customer 7]: handling deposit transaction
Teller 2 [Customer 7]: going to safe
Teller 2 [Customer 7]: enter safe
Teller 0 [Customer 27]: got manager's permission
Teller 0 [Customer 27]: going to safe
Teller 1 [Customer 15]: leaving safe
Teller 1 [Customer 15]: finishes deposit transaction.
Teller 1 [Customer 15]: wait for customer to leave.
Teller 1 [Customer 42]: serving a customer
Customer 15 [Teller 1]: leaves teller
Customer 15 []: goes to door
Customer 15 []: leaves the bank
Customer 42 [Teller 1]: selects teller
Customer 42 [Teller 1] introduces itself
Teller 1 [Customer 42]: asks for transaction
Customer 42 [Teller 1]: asks for withdrawal transaction
Teller 0 [Customer 27]: enter safe
Teller 1 [Customer 42]: handling withdrawal transaction
Teller 1 [Customer 42]: going to manager
Teller 1 [Customer 42]: getting manager's permission
Teller 2 [Customer 7]: leaving safe
Teller 2 [Customer 7]: finishes deposit transaction.
Teller 2 [Customer 7]: wait for customer to leave.
Teller 2 [Customer 43]: serving a customer
Customer 7 [Teller 2]: leaves teller
Customer 7 []: goes to door
Customer 7 []: leaves the bank
Customer 43 [Teller 2]: selects teller
Customer 43 [Teller 2] introduces itself
Teller 2 [Customer 43]: asks for transaction
Customer 43 [Teller 2]: asks for withdrawal transaction
Teller 2 [Customer 43]: handling withdrawal transaction
Teller 2 [Customer 43]: going to manager
Teller 1 [Customer 42]: got manager's permission
Teller 1 [Customer 42]: going to safe
Teller 1 [Customer 42]: enter safe
Teller 2 [Customer 43]: getting manager's permission
Teller 0 [Customer 27]: leaving safe
Teller 0 [Customer 27]: finishes withdrawal transaction.
Teller 0 [Customer 27]: wait for customer to leave.
Teller 0 [Customer 24]: serving a customer
Customer 27 [Teller 0]: leaves teller
Customer 27 []: goes to door
Customer 27 []: leaves the bank
Customer 24 [Teller 0]: selects teller
Customer 24 [Teller 0] introduces itself
Teller 0 [Customer 24]: asks for transaction
Customer 24 [Teller 0]: asks for deposit transaction
Teller 0 [Customer 24]: handling deposit transaction
Teller 0 [Customer 24]: going to safe
Teller 0 [Customer 24]: enter safe
Teller 2 [Customer 43]: got manager's permission
Teller 2 [Customer 43]: going to safe
Teller 1 [Customer 42]: leaving safe
Teller 1 [Customer 42]: finishes withdrawal transaction.
Teller 1 [Customer 42]: wait for customer to leave.
Teller 1 [Customer 39]: serving a customer
Customer 42 [Teller 1]: leaves teller
Customer 42 []: goes to door
Customer 39 [Teller 1]: selects teller
Customer 39 [Teller 1] introduces itself
Teller 2 [Customer 43]: enter safe
Teller 1 [Customer 39]: asks for transaction
Customer 39 [Teller 1]: asks for deposit transaction
Teller 1 [Customer 39]: handling deposit transaction
Teller 1 [Customer 39]: going to safe
Customer 42 []: leaves the bank
Teller 0 [Customer 24]: leaving safe
Teller 0 [Customer 24]: finishes deposit transaction.
Teller 0 [Customer 24]: wait for customer to leave.
Teller 0 [Customer 47]: serving a customer
Customer 24 [Teller 0]: leaves teller
Customer 24 []: goes to door
Teller 1 [Customer 39]: enter safe
Customer 24 []: leaves the bank
Customer 47 [Teller 0]: selects teller
Customer 47 [Teller 0] introduces itself
Teller 0 [Customer 47]: asks for transaction
Customer 47 [Teller 0]: asks for withdrawal transaction
Teller 0 [Customer 47]: handling withdrawal transaction
Teller 0 [Customer 47]: going to manager
Teller 0 [Customer 47]: getting manager's permission
Teller 0 [Customer 47]: got manager's permission
Teller 0 [Customer 47]: going to safe
Teller 2 [Customer 43]: leaving safe
Teller 2 [Customer 43]: finishes withdrawal transaction.
Teller 2 [Customer 43]: wait for customer to leave.
Teller 2 [Customer 21]: serving a customer
Customer 43 [Teller 2]: leaves teller
Customer 43 []: goes to door
Customer 43 []: leaves the bank
Teller 0 [Customer 47]: enter safe
Teller 1 [Customer 39]: leaving safe
Teller 1 [Customer 39]: finishes deposit transaction.
Teller 1 [Customer 39]: wait for customer to leave.
Teller 1 [Customer 26]: serving a customer
Customer 39 [Teller 1]: leaves teller
Customer 21 [Teller 2]: selects teller
Customer 21 [Teller 2] introduces itself
Customer 39 []: goes to door
Customer 39 []: leaves the bank
Customer 26 [Teller 1]: selects teller
Teller 2 [Customer 21]: asks for transaction
Customer 26 [Teller 1] introduces itself
Customer 21 [Teller 2]: asks for deposit transaction
Teller 1 [Customer 26]: asks for transaction
Teller 2 [Customer 21]: handling deposit transaction
Teller 2 [Customer 21]: going to safe
Teller 2 [Customer 21]: enter safe
Customer 26 [Teller 1]: asks for withdrawal transaction
Teller 1 [Customer 26]: handling withdrawal transaction
Teller 1 [Customer 26]: going to manager
Teller 1 [Customer 26]: getting manager's permission
Teller 1 [Customer 26]: got manager's permission
Teller 1 [Customer 26]: going to safe
Teller 2 [Customer 21]: leaving safe
Teller 2 [Customer 21]: finishes deposit transaction.
Teller 2 [Customer 21]: wait for customer to leave.
Teller 2 [Customer 20]: serving a customer
Customer 21 [Teller 2]: leaves teller
Customer 21 []: goes to door
Customer 21 []: leaves the bank
Customer 20 [Teller 2]: selects teller
Customer 20 [Teller 2] introduces itself
Teller 2 [Customer 20]: asks for transaction
Customer 20 [Teller 2]: asks for deposit transaction
Teller 2 [Customer 20]: handling deposit transaction
Teller 2 [Customer 20]: going to safe
Teller 2 [Customer 20]: enter safe
Teller 0 [Customer 47]: leaving safe
Teller 0 [Customer 47]: finishes withdrawal transaction.
Teller 0 [Customer 47]: wait for customer to leave.
Teller 0 [Customer 32]: serving a customer
Teller 1 [Customer 26]: enter safe
Customer 47 [Teller 0]: leaves teller
Customer 47 []: goes to door
Customer 47 []: leaves the bank
Customer 32 [Teller 0]: selects teller
Customer 32 [Teller 0] introduces itself
Teller 0 [Customer 32]: asks for transaction
Customer 32 [Teller 0]: asks for deposit transaction
Teller 0 [Customer 32]: handling deposit transaction
Teller 0 [Customer 32]: going to safe
Teller 2 [Customer 20]: leaving safe
Teller 2 [Customer 20]: finishes deposit transaction.
Teller 2 [Customer 20]: wait for customer to leave.
Teller 2 [Customer 49]: serving a customer
Customer 20 [Teller 2]: leaves teller
Customer 20 []: goes to door
Customer 20 []: leaves the bank
Customer 49 [Teller 2]: selects teller
Teller 1 [Customer 26]: leaving safe
Customer 49 [Teller 2] introduces itself
Teller 1 [Customer 26]: finishes withdrawal transaction.
Teller 1 [Customer 26]: wait for customer to leave.
Teller 2 [Customer 49]: asks for transaction
Customer 26 [Teller 1]: leaves teller
Customer 26 []: goes to door
Customer 26 []: leaves the bank
Customer 49 [Teller 2]: asks for deposit transaction
Teller 2 [Customer 49]: handling deposit transaction
Teller 2 [Customer 49]: going to safe
Teller 2 [Customer 49]: enter safe
Teller 0 [Customer 32]: enter safe
Teller 0 [Customer 32]: leaving safe
Teller 0 [Customer 32]: finishes deposit transaction.
Teller 0 [Customer 32]: wait for customer to leave.
Customer 32 [Teller 0]: leaves teller
Customer 32 []: goes to door
Customer 32 []: leaves the bank
Teller 2 [Customer 49]: leaving safe
Teller 2 [Customer 49]: finishes deposit transaction.
Teller 2 [Customer 49]: wait for customer to leave.
Customer 49 [Teller 2]: leaves teller
Customer 49 []: goes to door
Customer 49 []: leaves the bank
Teller 2 []: leaving for the day.
Teller 1 []: leaving for the day.
Teller 0 []: leaving for the day.
The bank closes for the day.