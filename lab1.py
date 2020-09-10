import math, cmath
print("ИУ5-52б Дума Эмилия Михайловна Лаб1\nПрограмма для решения (би)квадратных уравнений.\nВведите тип уравнения, которое хотите решить\n1. Квадратное\n2. Биквадратнрое")
q = int(input())
if q == 1:
    args = []
    i = 0
    while i < 3:
        try:
            print("Введите коэффициент:")
            args.append(float(input()))
            i = i + 1
        except ValueError:
            print("Введите число, а не string или char")
    a, b, c = args
    print("Вы ввели уравнение: ",a,"x^2 +",b,"x +",c,"= 0")
    D = b*b - 4*a*c
    print("Дискриминант:", D)
    if D > 0: print("Дискриминант положительный\nВсего 2 корня: ", "%.5f" % ((-b + math.sqrt(D))/2*a), "%.5f" % ((-b - math.sqrt(D))/2*a))
    elif D == 0: print("Дискриминант равне нулю\nВсего 1 корень: ", "%.5f" % ((-b)/2*a))
    elif D < 0:
        print("Дискриминант меньше нуля\nВсего 2 комплексных корня: ", "%.5f" % ((-b + math.sqrt(D*-1))/2*a),"* i,", "%.5f" % ((-b - math.sqrt(D*-1))/2*a),"* i")
elif q == 2:
    args = []
    i = 0
    while i < 3:
        try:
            print("Введите коэффициент:")
            args.append(float(input()))
            i = i + 1
        except ValueError:
            print("Введите число, а не string или char")
    a, b, c = args
    print("Вы ввели уравнение: ", a, "x^4 +", b, "x^2 +", c, "= 0")
    D = b * b - 4 * a * c
    print("Дискриминант:", D)
    print("Всего 4 корня: \n", "%.5f" % (math.sqrt(((-b+math.sqrt((b*b-4*a*c)))/(2*a)))), "%.5f" % (math.sqrt(((-b-math.sqrt((b*b-4*a*c)))/(2*a)))))
    print(                     "%.5f" % (-math.sqrt(((-b+math.sqrt((b*b-4*a*c)))/(2*a)))),"%.5f" % (-math.sqrt(((-b-math.sqrt((b*b-4*a*c)))/(2*a)))))

else: print("Такого типа уравнения нет, кажется, вы ошиблись :(")