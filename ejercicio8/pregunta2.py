def intereses(capital,interes,meses):
    for i in range (0,meses):
        capital= capital+capital*interes/100
    return print(capital)
intereses(100,5,3)