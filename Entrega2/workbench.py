from bibliotecas import formas,sistema

Cart=sistema.cart()
P=formas.Ponto(0.5,0.5)
C=formas.Circulo(0.1,0.5,12)
Cart.inserirForma(P)
Cart.inserirForma(C)
Cart.listarFormas()
Cart.info(P)
Cart.info(C)

