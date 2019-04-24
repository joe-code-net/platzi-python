#Clients List
clients = 'Pablo, Ricardo, '

#Function to create a new client
def create_client(client_name):
    global clients #global for use the clients variable with the global values
	
    clients += client_name
    _add_coma()

#Function to add a comma et the end of customers list
def _add_coma(): 
   global clients #global for use the clients variable with the global values
   clients += ', '

#Function to print the list of clients
def list_clients(): 
	global clients
	print (clients)

#Main function
if __name__ == '__main__':
	
	create_client('Joe') #ejecutamos la funcion crear cliente
	
	list_clients() #Volvemos a ejecutar la funcion listar clientes 

#To wait the user action
input()
