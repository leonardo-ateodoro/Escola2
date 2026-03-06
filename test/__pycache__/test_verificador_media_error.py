import pytest 
from escola import verificador_media


def test_string_como_entrada():
    with pytest.raises (TypeError, match= "Tipo invalido, a entrada deve estar errado"):
        verificador_media("OITO")
def test_menor_que_0_como_entrada():
    with pytest.raises(TypeError, match= "O VALOR DEVE SER MAIOR OU IGUAL A 0 E MENOR OU IGUAL A  10"):
        verificador_media (-5)

def test_maior_que_10_como_entrada():
    with pytest.raises(TypeError, match= " o valor deve ser maior igual a 0 e menor ou igual A 10"):
        verificador_media(2000)
    