satr = input("Satr: ")
unli = 'aeiouаеёиоуэюяӣўүұ'
for harf in unli:
    satr = satr.replace(harf, '*').replace(harf.upper(), '*')
print(satr)
