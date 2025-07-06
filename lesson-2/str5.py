satr = input("Satr kiriting: ").lower()
unli = 'aeiouаеёиоуэюяӣўүұ'
undosh = 'bcdfghjklmnpqrstvwxyzбвгджзйклмнпрстфхцчшщқғхҳ'
u = sum(1 for i in satr if i in unli)
c = sum(1 for i in satr if i in undosh)
print("Unlilar:", u)
print("Undoshlar:", c)
