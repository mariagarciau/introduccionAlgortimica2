def nomina(salario, horasNormales, horasExtra):
    if horasNormales+horasExtra>=36 and horasNormales+horasExtra<=43:
        salario=salario+horasExtra*1.25
    elif horasNormales+horasExtra>=44:
        salario=salario+horasExtra*1.5
    else:
        salario=salario
    return print(salario)
nomina(1500,35,0)
