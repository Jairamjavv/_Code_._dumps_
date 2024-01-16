def capital_indexes(str_in):
    indexes = [i for i in range(len(str_in)) if str_in[i].isupper()]
    return indexes

print(capital_indexes("Python Is a Programming LanguagE."))