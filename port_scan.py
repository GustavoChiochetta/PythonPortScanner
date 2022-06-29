import socket

print('PYTHON PORT SCANNER by Gustavo Prior Chiochetta')

continue_scanner = True

while(continue_scanner):
	target_ip = str(input('Ip alvo: '))
	open_ports = []
	socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	for port in range(1023):
		if (socket_obj.connect_ex((target_ip, port))):
			next
		else:
			open_ports.append(port)
			print(f'\nPorta {port} aberta')

	if (open_ports.__len__() == 0):
		print(f'\nNenhuma porta aberta no host {target_ip}')
	next_ip = ''

	while(next_ip != 's' and next_ip != 'n'):
		next_ip = str(input('\nDeseja continuar a execução? (s/n)'))
		if (next_ip == 'n'):
			continue_scanner = False
			print('\nAté logo')