
students_list = []

students_list.append(('K.Pacia',3.0))
students_list.append(('K.Wędzina',4.5))
students_list.append(('M.Mączka',3.0))
students_list.append(('Sz.Załęga',4.0))
students_list.append(('A.Wójs ',5.0))
students_list.append(('T.Walas',4.0))
students_list.append(('A.Mycek',2.0))
students_list.append(('W.Straszak',2.0))
students_list.append(('P.Poźniak',2.0))
students_list.append(('B.Fiter',2.0))
students_list.append(('M.Pycik',2.0))
students_list.append(('K.Siwek',2.0))
students_list.append(('K.Pazdur',2.0))
students_list.append(('M.Sikora',2.0))


passed_students = [i for i in students_list if i[1]!=2]

for i in passed_students:
    print(i)

