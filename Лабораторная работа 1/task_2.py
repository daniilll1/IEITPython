# TODO Найдите количество книг, которое можно разместить на дискете
DiscV = 1.44*1024**2

Bytes = 4
page = 100
strok = 50
sym = 25

k = int(DiscV//(strok*sym*page*Bytes))
print("Количество книг, помещающихся на дискету:", k)

