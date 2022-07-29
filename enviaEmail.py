import smtplib, email.message, csv
from time import sleep
import verificaEmail as vremail

def envia_email(arq, remetente, password):
    subject = str(input('Assunto: ')).strip().capitalize()
    senha = password
    smtp = smtplib.SMTP('smtp.gmail.com: 587')
    smtp.starttls()
    smtp.login(remetente, senha)
    with open(arq, 'r', encoding='utf-8') as arquivo:
        arquivo_csv = csv.reader(arquivo, delimiter=',')
        print('alo')
        for i, linha in enumerate(arquivo_csv):
            if i > 0:
                msg = email.message.Message()
                msg['From'] = remetente
                msg['Subject'] = subject
                msg.add_header('Content-Type', 'text/html')
                nome_destinat = linha[0]
                msg['To'] = linha[1]
                print(f"Remetente: {remetente}\n"
                      f"Para: {msg['To']}\n"
                      f"Nome do destinatário: {nome_destinat}")
                corpo_email = f"""
                        <p>Olá, <strong>{nome_destinat}</strong>!</p>
                        <br>
                        <p>Seu email é {msg['To']}, certo?</p>
                    """
                msg.set_payload(corpo_email)
                smtp.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email(s) enviado(s)!')

'''print(f'\033[33;1;4m{" ENVIAR EMAIL ":=^30}\033[m')
sleep(1)
email_remetente = vremail.verifica_email()
password = str(input('Senha: ')).strip()
envia_email('testecsv.csv', email_remetente, password)'''