#FUNÇÃO COMIDA DE CACHORRO
def comida(peso):
	if  peso <= 4:
		comi = 55
		coma = 95
		porte = 'Miniatura'
	else:
		if peso <= 8:
			comi = 95
			coma = 155
			porte = 'Pequeno'
		else:
			if peso <= 20:
				comi = 160
				coma = 320
				porte = 'Médio'
			else:
				if peso <= 40:
					comi = 320
					coma = 530
					porte = 'Grande'
				else:
					comi = 530
					coma = 810
					porte = 'Gigante' 
	return [comi, coma, porte]
#FUNÇÃO COMIDA DE GATO
def gatomida(peso):
	if  peso <= 3:
		comi = 40
		coma = 53
		return [comi, coma]
	else:
		if peso == 4: 
			com = 70
			return [com]
		else:
			if peso == 5:
				com = 81
				return [com]
			else:
				if peso == 6:
					com = 93
					return [com]
				else:
					if peso == 7: 
						com = 103
						return [com]
					else:
						if peso > 7:
							comi = 75
							coma = 78
							return [comi, coma]
#FUNÇÃO LIMITANTE DE RESPOSTAS PARA REMÉDIOS
def remedios():
	loop = 0
	lup = 0
	while loop == 0:
		loop = 1
		if lup == 0:
			rem = input('Medicações? ')
			if rem == 'Sim':
				vr = float(input('Valor '))
				return[rem, vr]
			else:
				if rem == 'Não':
						loop = 1
						return [rem]
				else:
					if rem != "Não":
						loop = 0
						lup = 1
		else:
			if lup == 1:
				rem = input('Insira uma resposta válida ')
				if rem == 'Sim':
					vr = float(input('Valor '))
					loop = 1
					return[rem, vr]
				else:
					if rem == 'Não':
						loop = 1
						return [rem]
					else: 
						lup = 1
						loop = 0
#FUNÇÃO LIMITANTE DE INTERNAÇÃO
def internacao():
    loop = 0
    lup = 0
    while loop == 0:
        loop = 1
        if lup == 0:
            inter = input('Internação? ')
            if inter == 'Sim':
                vi = float(input('Valor '))
                return [inter, vi]
            else:
                if inter == 'Não':
                    return [inter]
                else:
                    loop = 0
                    lup = 1
            if lup == 1:
                inter = input('Insira uma resposta válida ')
                if inter == 'Sim':
                    vi = float(input('Valor '))
                    return [inter, vi]
                    loop = 1
                else:
                    if inter == 'Não':
                        loop = 1
                        return [inter]
                    else: 
                        lup = 1
                        loop = 0
#FUNÇÃO LIMITANTE DE TIPO SANGUÍNEO
def sangue():
    loop = 0
    lup = 0 
    while loop == 0:
        loop = 1 
        if lup == 0:
            tip = input('Tipo Sanguineo ')
        
        if tip not in ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-'] :
                tip = input('Insira uma resposta válida ')
                lup = 1
                loop = 0
    return tip 						



qnt = int(input('Número de animais '))
while qnt > 0:
	nome = input('Nome ')
	esp = input('Espécie ')
	rac = input('Raça ')
	peso = float(input('Peso '))
	if esp == 'Cachorro':
		li = comida(peso)
	else:
		if esp == 'Gato':
			li = gatomida(peso)
	nac = input('Data de nascimento ')
	li2 = remedios()
	li3 = internacao()
	li4 = sangue() 
	print('Ficha:')
	print('Nome:', nome)
	print('Espécie:', esp)
	print('Raça:', rac)
	print('Peso:', str(peso), 'kg')
	if esp == 'Cachorro':
		print('Ração diária: de', str(li[0]), 'a', str(li[1]), 'g')
		print('Porte:', li[2])
	else:
		if esp == 'Gato':
			print('Ração diária:', str(li[0]), 'g')
			if peso > 7:
				print('Gato com obesidade, por favor consulte seu veterinário')
	print('Data de nascimento:', nac)
	if li2[0] == 'Sim':
		print('Medicamentos: Sim')
		print('Valor:', str(li2[1]), 'R$')
	else:
		print('Medicamentos: Não')
	if li3[0] == 'Sim':
		print('Internação: Sim')
		print('Valor:', str(li3[1]), 'R$')
	else:
		print('Internação: Não')
	if li2[0] and li3[0] == 'Sim':
		print('Valor a pagar:', float(li2[1]) + float(li3[1]))
	else:
		if li2[0] == 'Sim':
			print('Valor a pagar:', str(li2[1]), 'R$')
		else:
			if li3 == 'Sim':
				print('Valor a pagar:', str(li3[1]))
	print('Tipo sanguíneo:', li4)

	qnt = qnt - 1


		