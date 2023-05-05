#Register of password
def get_pass():
    while True:
        print('Digite a senha numérica de 5 digitos\n')
        password = input('')
        if len(password) != 5:
            print('Senha deve ter 5 dígitos!\n')
        elif any(char not in '0123456789' for char in password):   
            print('Senha deve conter somente números!\n')
        else:
            print('\nSenha Registrada com Sucesso\n')
            return password
            

#Password confirmation
def pass_confirm():
    while True:
        print('Digite novamente a senha numérica de 5 digitos\n')
        confirm_password = input('')
        if len(confirm_password) != 5:
            print('Senha deve ter 5 dígitos!\n')
        elif any(char not in '0123456789' for char in confirm_password):   
            print('Senha deve conter somente números!\n')
        else:
            print('\nSenha Registrada com Sucesso\n')
            return confirm_password

#Password Program Main System
while True:
    print('Você tem 3 chances para confirmar sua senha corretamente\n')
    for i in range(1,4) :
        print(f'Tentativa {i}\n')
        password = get_pass()
        confirmation = pass_confirm()
        if password != confirmation and i == 3:
            print('Erro em Terceira tentativa')
            print('Refaça o processo novamente\n')
            continue
        elif password != confirmation:
            print('Senhas Incorretas')
            print('Tente Novamente\n')
        else:
            print('Senhas Identicas')
            print('Registro Finalizado')
            break
    break
    