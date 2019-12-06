from libpythonproVictor.spam.main import EnviadorDeSpam
import pytest

from libpythonproVictor.spam.modelos import Usuario
from unittest.mock import Mock


# class EnviadorMock(Enviador):
#     def __init__(self):
#         super().__init__()
#         self.emails_enviados = 0
#         self.parametros_de_envio = None
#
#     def enviar(self, remetente, destinatario, asssunto, corpo):
#         self.parametros_de_envio = (remetente, destinatario, asssunto, corpo)
#         self.emails_enviados += 1

@pytest.mark.parametrize('usuarios', [[Usuario(nome='Victor', email='vh141299@gmail.com'),
                                      Usuario(nome='Aparecida', email='aparecidabarbosapereira@gmail.com')],
                                      [Usuario(nome='Victor', email='vh141299@gmail.com')]])
def test_qtde_de_spam(usuarios, sessao):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails('vh141299@gmail.com',
                                   'Titulo',
                                   'corpo')

    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Victor', email='vh141299@gmail.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails('aparecida@gmail.com',
                                   'Titulo',
                                   'corpo')

    enviador.enviar.assert_called_once_with('aparecida@gmail.com',
                                            usuario.email,
                                            'Titulo',
                                            'corpo')
