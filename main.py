import smtplib
import email.message
from time import sleep
import re

def verifica_email():
   pat = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
   while True:
       email_remetente = str(input("Email remetente: ")).strip()
       if re.match(pat, email_remetente):
           return email_remetente
       else:
           print("[ERRO] Email inválido. Tente novamente.")
           sleep(1)

def enviar_email(remetente, password, destinatario):

    msg = email.message.Message()
    msg['From'] = remetente
    msg['To'] = destinatario
    msg['Subject'] = str(input('Assunto: '))
    corpo_email = """
        <p>Olá, amigo!</p>
        <p>Testando email automático</p>
        """
    senha = password
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)
    smtp = smtplib.SMTP('smtp.gmail.com: 587')
    smtp.starttls()
    smtp.login(msg['From'], senha)
    smtp.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado, rapaz.')


print(f'\033[32;1;4m{" ENVIAR EMAIL ":=^30}\033[m')
sleep(0.5)
email_remetente = verifica_email()
password = str(input("Senha: ")).strip()
email_destinatario = str(input('Email(s) destinatário(s): ')).strip()
enviar_email(email_remetente, password, email_destinatario)