salario_bruto=float(input(""))
if salario_bruto<=1903:
    print(salario_bruto)
elif salario_bruto<=2826:
    pag= -(salario_bruto* 0.075)
    print (pag)
elif salario_bruto<=3751:
    pag= salario_bruto-(salario_bruto* 0.15)
    print (pag)
elif salario_bruto<= 4664:
    pag= salario_bruto-(salario_bruto* 0.225)
    print (pag)
elif salario_bruto>= 4664:
    pag= salario_bruto-(salario_bruto* 0.275)
    print (pag)
else:
    print("")