# TODO Найдите количество книг, которое можно разместить на дискете
diskMB = 1.44
pages = 100
lines_on_page = 50
chars_in_line = 25
one_char_in_byte = 4
book_in_bytes = pages * lines_on_page * chars_in_line * one_char_in_byte
book_in_MB = book_in_bytes / (1024 * 1024)
res = int(diskMB // book_in_MB)
print("Количество книг, помещающихся на дискету:", res)
