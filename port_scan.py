# SCRIPT PARA PORT SCAN
import socket #IMPORTANDO SOCKET PARA FAZER CONEXAO NAS PORTAS

print('PYTHON PORT SCANNER by Gustavo Prior Chiochetta')

continue_scanner = True

# LOOP PARA CONTINUAR EXECUTANDO O CÓDIGO APÓS TODAS PORTAS SEREM SCANEADAS
while(continue_scanner):
	# PEDINDO PARA O USUÁRIO QUAL O IP ALVO
	target_ip = str(input('Ip alvo: '))
	# CRIA UM ARRAY PARA AS PORTAS ABERTAS, VAI SER ÚTIL CASO NÃO TENHA NEHUMA
	open_ports = []
	# CRIANDO UMA VARIÁVEL PARA REFERENCIAR O OBJETO DO SOCKET
	socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	# LOOP FOR PARA PASSAR PELAS PORTAS 0 ATÉ 1023
	for port in range(1023):
		# SE A CONEXÃO FALHAR IRA ENTRAR NESSE IF, E ASSIM CONTINUARA O LOOP
		if (socket_obj.connect_ex((target_ip, port))):
			next
		# CASO A CONEXÃO NÃO FALHAR IRA LOGAR A PORTA ABERTA
		else:
			# ADICIONA A PORTA A LISTA DE PORTAS ABERTAS
			open_ports.append(port)
			print(f'\nPorta {port} aberta')
	
	# AVISA O USUÁRIO QUE NÃO TEM NENHUMA PORTA ABERTA NESSE HOST
	if (open_ports.__len__() == 0):
		print(f'\nNenhuma porta aberta no host {target_ip}')
	next_ip = ''
	
	# PEDE PARA O USUÁRIO SE ELE DESEJA CONTINUAR EXECUTANDO O CODIGO,
	# E VOLTA A PEDIR O MESMO CASO A RESPOSTA NÃO SEJA A ESPERADA
	while(next_ip != 's' and next_ip != 'n'):
		next_ip = str(input('\nDeseja continuar a execução? (s/n)'))
		if (next_ip == 'n'):
			continue_scanner = False
			print('\nAté logo')