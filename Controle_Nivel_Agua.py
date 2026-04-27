from colorama import Fore, Style, init
init(autoreset=True)
niveis = [
    "Muito baixo (crítico)",
    "Baixo",
    "Médio",
    "Alto",
    "Muito alto (alerta)"
]
def definir_cor(nivel):
    if nivel == 1:
        return Fore.RED
    elif nivel == 2:
        return Fore.YELLOW
    elif nivel == 3:
        return Fore.GREEN
    elif nivel == 4:
        return Fore.CYAN
    elif nivel == 5:
        return Fore.BLUE
    else:
        return Fore.WHITE
for i in range(1, 6):
    cor = definir_cor(i)
    mensagem = niveis[i - 1]
    print(cor + f"Nível {i}: {mensagem}")
print(Style.RESET_ALL)