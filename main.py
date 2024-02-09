# Código - Metodo de Euler - Anna

# Especificações
'''
yin - valor inicial
a - lim inferior
b - lim superior
m - num de subintervalos
yb - f(x,y)
h - (b-a)/m
'''
import time

def funcao_calc(funcao,x,y):
    print(x,y, funcao)
    print(eval(funcao))
    return eval(funcao)

def funcao_calc_sist(funcao,x,y1,y2):
    print(x,y1,y2, funcao)
    print(eval(funcao))
    return eval(funcao)


keep = 0

while keep == 0:
    print("\n\n\n\n Bem vindo a Calculadora - Método de Euler ! \n")
    OP = input("  1) Equação diferencial. \n  2) Sistema de 2 Equações diferenciais. \n  Escolha 1/2:\n >")
    if OP == "1":
        print("A")
        #OP = 0
        yin = int(input("Valor inicial: "))
        a = int(input("Limite inferior: "))
        b = int(input("Limite superior: "))
        m = int(input("Numero de subintervalos: "))
        funcao = input("Função y': ")
        h = (b-a)/m
        print(yin, a, b, m, h, funcao)
        lista = [yin, a, b, m, h]

        '''print('interação 1 \n')
        y2 = yin + h*funcao
        print(y2)
        time.sleep(5)
'''
        y = [0]*20
        y[1] = yin
        x = a

        for i in range(1,m):
            y[i+1] = y[i] + h*funcao_calc(funcao,x,y[i])
            x = x + h
            print(h, y[i], y[i+1])


    elif OP == "2":
        yin1 = float(input("Valor inicial de y1: "))
        yin2 = float(input("Valor inicial de y2: "))
        a = float(input("Limite inferior: "))
        b = float(input("Limite superior: "))
        m = int(input("Numero de subintervalos: "))
        funcao1 = input("Função f(x, y1, y2): ")
        funcao2 = input("Função g(x, y1, y2): ")
        h = (b - a) / m
        x = a
        y1 = yin1
        y2 = yin2
        print("\nResultados:")
        for j in range(m):
            y1_j = y1 + h * funcao_calc_sist(funcao1, x, y1, y2)
            y2_j = y2 + h * funcao_calc_sist(funcao2, x, y1, y2)
            y1 = y1_j
            y2 = y2_j
            x += h
            print("x =", x, ", y1 =", y1, ", y2 =", y2)


    #OP = 0 ou outros
    else:
        print("\n Escolha uma opção válida.")
        keep = int(input("Prosseguir? (0 - Sim, 1 - Não)"))

    # See PyCharm help at https://www.jetbrains.com/help/pycharm/
