print("*** ИГРЫ С ЧИСЛАМИ ***")
print()
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
while 1: #пока единица, выполняется цикл
    try:
        a = (abs(int(input("Введите целое число => ")))) #Здесь были поставлены две скобочки. abs - возращающее абсолютное значения числа, с плавающей точкой и целыми числами.
        #int(input()) пишется чтобы присвоить значение А, введенное пользователем
        break #прекращает цикл
    except ValueError: #если в цикле обнаружена ошибка в цикле, мы ее пропускаем с помощью этой команды
         print("Это не целое число")
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
if a==0: #если пользовательно написал ноль, то выполняется команда принт и ничего не будет происходить до тех пор пока пользователь не введет целое число
    print("Нет смысла ничего делать с нулём")
else:
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Определяем, сколько в числе чётных и сколько нечётных цифр")
    print()
    c=b=a #убрал одно равно, все значения равны между собой, т.е. имеют одно и тоже значение
    paaris==0
    paaritu==0
    while b > 0: #тут я поставил двоеточие чтобы цикл начал работать
            if b % 2==0: #здесь было поставлено еще одно ровно, чтобы показат что значение будет равняться этому, процент значит
                                                                                                    #что число будет без остатка
                    paaris =+ 1
            else:
                    paaritu =+ 1
            b=b/10 #Здесь было сделано деление и поставлено на правильную строку, сделано деление
    
    print("Чётных цифр:",paaris) #Здесь была поставлена запятая после ковычек, чтобы показывалось значение после ковычек
    print("Нечётных цифр:",paaritu) #Здесь была поставлена запятая после ковычек, чтобы показывалось значение после ковычек
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("*Переворачиваем* введённое число")
    print()
    b=0
    while a > 0: #тут я поставил двоеточие чтобы цикл начал работать
        number = a % 10 #Здесь значение поставлено на правильную строку, вычисляется остаток (%)
        a = a // 10
        b = b * 10
        b =+ number #Здесь значение поставлено на правильную строку
    print("*Перевёрнутое* число", b)
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Проверяем гипотезу Сиракуз") #убрана скобка
    print()
    if c % 2==0: #поставлен еще одно равно
        print("c - чётное число. Делим на 2.")
    else:
         print("c - нечётное число. Умножаем на 3, прибавляем 1 и делим на 2.")
    while c!= 1: #если это число не будет равно единице
            if c % 2==0: #поставлено еще одно рaвно
                    c=c/2
            else:
                    c==(3*c + 1) / 2
            print(c, end="") #поствлена ковычка
    print("Гипотеза верна") #поствлена ковычка
