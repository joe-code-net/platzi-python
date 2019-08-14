import sys

#Clients List
clients = [
   {
      'name': 'Pablo',
      'company': 'Google'
      'email': 'pablo@google.com'
      'position': 'Software engineer'
   },
   {
      'name': 'Ricardo'
      'compay': 'Facebook'
      'email': 'ricardo@facebook.com',
      'position': 'Data engineer'
   }
]

#Function to create a new client
def create_client(client_name):
   global clients #global for use the clients variable with the global values
	
   if client not in clients:
      clients.append(client)
   else:
      print('Client alredy is in the client\'s list')

#Function to delete a client
def delete_client(client_name):
   global clients #global for use the clients variable with the global values

   if client_name in clients:
      #clients = clients.replace(client_name + ',', '')
      clients.remove(client_name)
   else:
      print('Client is not in clients list')

#Function to search a client
def search_client(client_name):
   #clients_list = clients.split(',')

   for client in clients:
      if client != client_name:
          continue
      else:
         return True

#Function to print the list of clients
def list_clients():
   for idx, client in enumerate(clients):
	      print ('{} : {}'.format(idx, client))

def update_client(client_name, update_client_name):
   global clients

   if client_name in clients:
          #clients = clients.replace(client_name + ',', update_client_name + ',')
          index = clients.index(client_name)
          clients[index] = update_client_name
   else:
          print('Client is not in clients list')

def _print_welcome():
   print('WELCOME TO SALES PLATZI APP')
   print('*' * 50)
   print('What would you like to do today?')
   print('[C]reate client') 
   print('[L]ist clients')
   print('[U]date client')
   print('[D]elete client')
   print('[S]earch client')

def _get_client_name():
   client_name = None

   while not client_name:
      client_name = input('What is the client name? ')

      if client_name == 'exit':
         client_name = None
         break

   if not client_name:
      sys.exit()

   return  client_name


#Main function
if __name__ == '__main__':
   _print_welcome() 
    
   command = input()
   command = command.upper()

   if command == 'C':
      client_name = _get_client_name()
      create_client(client_name)
      list_clients()
   elif command == 'L':
      list_clients()
   elif command == 'D':
      client_name = _get_client_name()
      delete_client(client_name)
      list_clients()
   elif command == 'U':
      client_name = _get_client_name()
      update_client_name = input('What is the updated client name ')
      update_client(client_name, update_client_name)
      list_clients()
   elif command == 'S':
      client_name = _get_client_name()
      found = search_client(client_name)

      if found:
             print('The client is in the client\'s list')
      else:
             print('The client: {} is not in  our client\'s list'.format(client_name))
   else:
      print('Invalid command') 

#To wait the user action
input()
