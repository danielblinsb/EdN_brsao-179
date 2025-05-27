def senha_forte(senha):
    if len(senha) < 8:
        return False
    if not any(char.isdigit() for char in senha):
        return False
    return True

while True:
    senha = input("Digite uma senha (ou 'sair' para encerrar): ")
    if senha.lower() == 'sair':
        print("Encerrando o programa.")
        break
    if senha_forte(senha):
        print("Senha forte! Acesso concedido.")
        break
    else:
        print("Senha fraca. Tente novamente.")

