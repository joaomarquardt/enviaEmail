def verifica_email():
    pat = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
    while True:
        email_remetente = str(input("Email remetente: ")).strip()
        if re.match(pat, email_remetente):
            return email_remetente
        else:
            print("[ERRO] Email inválido. Tente novamente.")
            sleep(1)