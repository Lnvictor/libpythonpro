from libpythonproVictor.spam.modelos import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome ='Victor', email='vh141299@gmail.com')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuarios(sessao):
    usuarios = [Usuario(nome ='Victor', email='vh141299@gmail.com'), Usuario(nome ='Aparecida', email='aparecidabarbosapereira@gmail.com')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
