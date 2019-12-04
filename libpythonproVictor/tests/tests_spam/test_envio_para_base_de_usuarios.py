from libpythonproVictor.spam.main import EnviadorDeSpam
from libpythonproVictor.spam.enviador_de_email import Enviador
import pytest

from libpythonproVictor.spam.modelos import Usuario

@pytest.mark.parametrize('usuarios', [[Usuario(nome = 'Victor', email = 'vh141299@gmail.com'),
                                     Usuario(nome = 'Aparecida', email = 'aparecidabarbosapereira@gmail.com')],[Usuario(nome = 'Victor', email = 'vh141299@gmail.com')]])


def test_qtde_de_spam(usuarios, sessao):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Enviador()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails('vh141299@gmail.com',
                                   'Titulo',
                                   'corpo')

    assert len(usuarios) == enviador.emails_enviados
