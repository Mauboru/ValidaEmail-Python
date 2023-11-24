from email_validator import validate_email, EmailNotValidError

def verificar_emails(lista_emails):
    for email in lista_emails:
        try:
            v = validate_email(email)
            print(f'O e-mail {email} é válido.')
        except EmailNotValidError as e:
            print(f'O e-mail {email} não é válido. Detalhes: {str(e)}.')

lista_de_emails = ['josue21henrique@gmail.com']

verificar_emails(lista_de_emails)