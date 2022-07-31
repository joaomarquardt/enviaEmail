'''import imaplib, email.message, os, base64
import verificaEmail as vremail

def le_email(email_login, password):
    imap = imaplib.IMAP4_SSL("imap.gmail.com")
    imap.login(email_login, password)
    imap.select(mailbox='inbox', readonly=True)
    resp, id = imap.search(None, 'All')
    for n in id[0].split():
        corpo_email = imap.fetch(n, '(RFC822)')[0][1]
        corpo_email = corpo_email.encode('utf-8')
        corpo_email = email.message_from_string(str(corpo_email))
        print(corpo_email)
'''

from imap_tools import MailBox, AND, OR, NOT
import verificaEmail as vremail
from enviaEmail import envia_email

def le_email(email_login, password):
    imap = MailBox("imap.gmail.com")
    meu_email = imap.login(email_login, password)
    with meu_email as mailbox:
        for msg in mailbox.fetch(AND(from_='marquardt1402@gmail.com', subject='Registro de alunos')):
            if (len(msg.attachments) > 0):
                for anexo in msg.attachments:
                    if 'lista_alunos.csv' in anexo.filename:
                        informacoes = anexo.payload
                        with open('lista_alunos.csv', 'wb') as arquivo:
                            arquivo.write(informacoes)
                        with open('lista_alunos.csv', 'r', encoding='utf-8') as arquivo_csv:
                            envia_email("lista_alunos.csv", email_login, password)


print(f'\033[33;1;4m{" LER EMAIL ":=^30}\033[m')
email_login = 'enviaemailteste14@gmail.com'
password = 'omijmsvwyqapmbhj'
le_email(email_login, password)
