import csv
import os

CLIENT_TABLE = '.clients.csv'
CLIENT_SCHEMA = ['name', 'company', 'email', 'position']
clients =[]

def _initialize_clients_from_storage():
	with open(CLIENT_TABLE, mode ='r') as f:
		reader = csv.DictReader(f, fieldnames= CLIENT_SCHEMA)

		for row in reader: 
			clients.append(row)

def _save_clients_to_storage():
	tmp_table_name = '{}.tmp'.format(CLIENT_TABLE)
	with open(tmp_table_name, mode='w') as f:
		writer = csv.DictWriter(f, fieldnames=CLIENT_SCHEMA)
		writer.writerows(clients)
		

		os.remove(CLIENT_TABLE)
		f.close
		os.rename(tmp_table_name, CLIENT_TABLE) 

#Function to create a new client
def create_client(client):
   global clients #global for use the clients variable with the global values
	
   if client not in clients:
      clients.append(client)
   else:
      print('Client alredy is in the client\'s list')

#Function to print the list of clients
def list_clients():
   for idx, client in enumerate(clients):
	      print ('{uid} | {name} | {company} | {email} | {position}'.format(
            uid=idx,
            name=client['name'],
            company=client['company'],
            email=client['email'],
            position=client['position']))

def update_client(client_id, update_client_name):
   global clients

   if len(clients) - 1 >= client_id:
      clients[client_id] = updated_client
   else:
      print('Client not in client\'s list')

#Function to delete a client
def delete_client(client_id):
   global clients #global for use the clients variable with the global values

   for idx, client in enumerate(clients):
      if idx == client_id:
         del clients[idx]
         break
    
#Function to search a client
def search_client(client_name):
   for client in clients:
      if client['name'] != client_name:
          continue
      else:
         return True

def _get_client_field(field_name, message='What is the client {}?'):
   field = None

   while not field:
         field = input(message.format(field_name))

   return field


def _get_client_from_user():
   client = {
         'name': _get_client_field('name'),
         'company': _get_client_field('company'),
         'email': _get_client_field('email'),
         'position': _get_client_field('position'),
   }

   return client

def _print_welcome():
   print('WELCOME TO SALES PLATZI APP')
   print('*' * 50)
   print('What would you like to do today?')
   print('[C]reate client') 
   print('[L]ist clients')
   print('[U]date client')
   print('[D]elete client')
   print('[S]earch client')

#Main function
if __name__ == '__main__':
   _initialize_clients_from_storage()
   
   _print_welcome() 
    
   command = input()
   command = command.upper()

   if command == 'C':
      client = _get_client_from_user()
      create_client(client)
      #list_clients()
   elif command == 'L':
      list_clients()
   elif command == 'D':
      client_id = int(_get_client_field('id'))

      delete_client(client_id)
      #list_clients()
   elif command == 'U':
      client_id = int(_get_client_field('id'))
      updated_client = _get_client_from_user()

      update_client(client_id, updated_client)
      #list_clients()
   elif command == 'S':
      client_name = _get_client_field('name')
      found = search_client(client_name)

      if found:
             print('The client is in the client\'s list')
      else:
             print('The client: {} is not in  our client\'s list'.format(client_name))
   else:
      print('Invalid command') 

   _save_clients_to_storage()

#To wait the user action
#input()
