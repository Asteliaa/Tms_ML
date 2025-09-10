def figure_move(a, b, c, d, figure):
    if figure == "queen":
        if a == c or b == d or abs(a - c) == abs(b - d):
            print("Ферзь угрожает")
        else:
            print("Ферзь не угрожает")
            
    elif figure == "horse":
        step1 = abs(a - c)
        step2 = abs(b - d)
        if (step1 == 1 and step2 == 2) or (step1 == 2 and step2 == 1):
            print("Конь угрожает")
        else:
            print("Конь не угрожает")
    else:
        print("Другая фигура")

(figure_move(4, 4, 4, 7, "queen"))   
(figure_move(4, 2, 6, 5, "horse"))  

