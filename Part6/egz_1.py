def length_dict(word_list):
    list_of_strs = {}
    for i in word_list:
        str_len = len(i)
        los_value = word_list[0:str_len]
        list_of_strs[str_len] = los_value

    for k,v in list_of_strs.items():
        print(k,v)

#-------------------------------

word_list = ['Jesli', 'uzytkownik', 'dwa', 'razy',
'poda', 'nieprawidłowy', 'dzien', 'program', 'ma',
'wypisac', 'nazwy', 'dni', 'tygodnia', 'i', 'zakonczyc', 'działanie']

length_dict(word_list)