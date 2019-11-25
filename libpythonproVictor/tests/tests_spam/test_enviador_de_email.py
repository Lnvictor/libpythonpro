from libpythonproVictor.spam.enviador_de_email import Enviador
import pytest


def test_enviador_de_email():
    enviador = Enviador
    assert enviador is not None

@pytest.mark.parametrize('destinatario',
                         ['aparecidabarbosapereira@gmail.com', 'v245055@dac.unicamp.br'])
def test_remetente(destinatario):
    enviador = Enviador()
    destinatario = ['aparecidabarbosapereira@gmail.com', 'v245055@dac.unicamp.br']
    resultado = enviador.enviar(remetente, destinatatio, 'Teste de Spam', 'Teste')
    assert destinatario in resultado