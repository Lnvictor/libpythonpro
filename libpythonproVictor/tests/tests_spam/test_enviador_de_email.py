from libpythonproVictor.spam.enviador_de_email import Enviador, EmailInvalido
import pytest


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None

@pytest.mark.parametrize('remetente',
                         ['vh141299@gmail.com', 'v245055@dac.unicamp.br'])
def test_remetente(remetente):
    destinatario = 'aparecidabarbosapereira@gmail.com'
    enviador = Enviador()
    resultado = enviador.enviar(remetente, destinatario, 'Teste de Spam', 'Teste')
    assert remetente in resultado


@pytest.mark.parametrize('remetente',
                         ['vh141299gmail.com', 'v245055dac.unicamp.br'])
def test_remetente_invalido(remetente):
    destinatario = 'aparecidabarbosapereira@gmail.com'
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        resultado = enviador.enviar(remetente, destinatario, 'Teste de Spam', 'Teste')
        assert remetente in resultado
