#txt dosyası okunuyor.
file1 = open('myfile.txt', 'r')

Lines = file1.readlines()



line_counter = 0

# Her satıra göre ayırma işlemi yapılıyor.
for line in Lines:

    line_counter += 1

    a = line.split(")")
    # a = Kapalı parantez ")" gördüğü her yerde satırdaki cümleyi bölüp kendisine kayıt ediyor.

    for i in a:

        if str(input_numara) == i

            # Verilen numaralı satıra ulaşıldı. Bu satırı silebilirsin

            print(line_counter)
