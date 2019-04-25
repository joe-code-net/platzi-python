#Clients List
clients = 'Pablo, Ricardo, '

#Function to create a new client
def create_client(client_name):
   global clients #global for use the clients variable with the global values
	
   if client_name not in clients:
      clients += client_name
      _add_coma()
   else:
      print('Client alredy is in the client\'s list')

#Function to add a comma et the end of customers list
def _add_coma(): 
   global clients #global for use the clients variable with the global values
   clients += ', '

#Function to print the list of clients
def list_clients(): 
	global clients
	print (clients)

def _print_welcome():
   print('WELCOME TO SALES PLATZI APP')
   print('*' * 50)
   print('What would you like to do today?')
   print('[C]reate client')
   print('[D]elete client')

#Main function
if __name__ == '__main__':
   _print_welcome() 
    
   command = input()
    
   if command == 'C':
      client_name = input('What is the client name? ')
      create_client(client_name)
      list_clients()
   elif command == 'D':
      pass
   else:
      print('Invalid command') 

#To wait the user action
input()
