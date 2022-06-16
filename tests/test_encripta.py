from cesar.cesar import decripta, encripta


def test_encripta_eduardo_retorna_rqhneqb():
    assert encripta('Eduardo') == 'rqhneqb'


def test_encripta_deve_retornar_minusculas():
    assert encripta('A').islower()


def test_encripta_deve_preservar_os_espaços():
    resultado = encripta('e a')
    assert resultado[1] == ' '


def test_decripta_rqhneqb_retorna_eduardo():
    assert encripta('rqhneqb') == 'eduardo'


def test_decripta_deve_retornar_minusculas():
    assert decripta('R').islower()


def test_encripta_deve_preservar_os_espaços():
    resultado = decripta('r h')
    assert resultado[1] == ' '
