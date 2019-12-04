from libpythonproVictor.spam.modelos import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome ='Victor')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuarios(sessao):
    usuarios = [Usuario(nome ='Victor'), Usuario(nome ='Aparecida')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
