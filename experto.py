def sistema_experto_clima():
    sol = input("¿es un dia asoleado ? (s/n): ").lower() == 's'
    calor = input("¿demaciado calor? (s/n): ").lower() == 's'

    if sol and calor:
        return "Lleva paragua y agua para hidratarse"
    elif sol and not calor:
        return "Lleva bloqueador "
    elif not sol and calor:
        return "Lleva una poker"
    else:
        return "Disfruta del buen clima "

print(sistema_experto_clima())
# experto omar gabriel