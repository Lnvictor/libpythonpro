class Enviador:

    def __init__(self):
        self.emails_enviados = 0

    def enviar(self, remetente, destinatario, asssunto, corpo):
        if not '@' in remetente:
            raise(EmailInvalido(f'Email inválido {remetente}'))
        self.emails_enviados += 1
        return remetente


class EmailInvalido(Exception):
    pass