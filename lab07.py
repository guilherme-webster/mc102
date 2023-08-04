from find_operador import f_operador

str_operador = input()
operando1 = input()
operando2 = input()
n_linhas = int(input())
msg_cripto = input()


def find_k(op, str_op1, str_op2, cripto):
    op1 = f_operador(str_op1, cripto)
    op2 = f_operador(str_op2,cripto)
    if op == '+':
        k = (op1 + op2) * (op1 + op2)
    elif op == '*':
        k = (op1 + op2) * (op1 * op2)
    elif op == '-':
        k = (op1 + op2) * (op1 - op2)
    return k
