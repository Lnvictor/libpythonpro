class Enviador:
    def enviar(self, remetente, destinatario, asssunto, corpo):
        if not '@' in remetente:
            raise(EmailInvalido(f'Email inválido {remetente}'))
        return remetente


class EmailInvalido(Exception):
    pass