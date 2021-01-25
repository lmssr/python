def sum_of_multiples_of_3_and_5(number):

    resultat = 0 
    for i in range (number):
        if i%3 == 0 or i%5 == 0:
            resultat += i
    return resultat



