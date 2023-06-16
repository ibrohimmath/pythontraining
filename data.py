sign = 0
game = [[['_', 0] for __ in range(8)] for _ in range(8)]
for i in range(3):
    for j in range(8):
        if (i + j ) % 2:
            game[i][j][0] = 0
for i in range(5, 8):
    for j in range(8):
        if (i + j) % 2:
            game[i][j][0] = 1
def shash():
    for i in range(8):
        for j in range(8):
            print(game[i][j][0], end = ' ')
        print()
shash()
black = white = 12
while black and white:
    a, b = map(str, input("Koordinatalarni kiriting!!! ").split())
    x, y = int(a[1]) - 1, ord(a[0]) - ord('A')
    x1, y1 = int(b[1]) - 1, ord(b[0]) - ord('A')
    if game[x][y][0] == sign and game[x1][y1][0] == '_':
        # navbat to'g'riligi va o'tayotgan joyi bo'shligini tekshirish
        if game[x][y][1] == 0:
            #damka emasligini tekshirish
            if abs(x - x1) == 1 and abs(y - y1) == 1:
                #qo'shni joyga yurish
                game[x1][y1][0] = sign
                game[x][y][0] = '_'
                game[x][y][1] = 0
                if (sign == 1 and x1 == 0) or (sign == 0 and x1 == 7):
                #qora yoki oq oxiriga borib damkaga aylanishini tekshirish
                    game[x1][y1][1] = 1
                sign = 1 - sign
                shash()
            elif abs(x - x1) == 2 and abs(y - y1) == 2:
                #urish holatini tekshirish
                x2 = (x + x1) // 2
                y2 = (y + y1) // 2
                if game[x2][y2][0] == 1 - sign:
                    #qo'shni raqib ekanligini tekshirish
                    game[x1][y1][0] = sign 
                    game[x][y][0] = game[x2][y2][0] = '_'
                    game[x][y][1] = game[x2][y2][1] = 0
                    if (sign == 1 and x1 == 0) or (sign == 0 and x1 == 7):
                    #qora yoki oq oxiriga borib damkaga aylanishini tekshirish
                        game[x1][y1][1] = 1
                    black -= sign == 0
                    white -= sign == 1
                    sign = 1 - sign
                    shash()
                else:
                    print("Shashka qoidalariga to'g'ri kelmaydi, chunki qora qorani, oq oqni ura olmaydi")
                    continue    
            else:
                #xatolik
                print("Shashka qoidalariga to'g'ri kelmaydi, chunki bu oddiy shashka")
                continue
        else:
        #damka bo'lgan holatlarni ko'rish
            if abs(x - x1) == abs(y - y1):
            #diagonallikka tushishni tekshirish
                dx = (x1 - x) // abs(x1 - x)
                dy = (y1 - y) // abs(y1 - y)
                i, j = x, y 
                ext = 0
                while (i, j) != (x1 - 1, y1 - 1):
                #ikkita qo'shni nuqtada donachalar borligini tekshirish
                    if game[i][j][0] != '_' and game[i + dx][j + dy][0] != '_':
                        ext = 1
                        print("2 ta qo'shni donalar chiqdi orada")
                        break
                    i += dx 
                    j += dy 
                i, j = x, y
                while (i, j) != (x1, y1):
                #damka yo'lida o'zining rangidagi donacha borligini tekshirish    
                    if game[i][j][0] == sign and i != x and j != y:
                        ext = 1
                        print("orada o'ziniki chiqdi")
                        break
                    i += dx 
                    j += dy
                if ext == 0:
                    i, j = x, y 
                    while (i, j) != (x1, y1):
                        if game[i][j][0] == 1 - sign:
                            game[i][j][0] = '_'
                            game[i][j][1] = 0
                            black -= sign == 0
                            white -= sign == 1
                        i += dx 
                        j += dy
                    game[x1][y1][0] = sign 
                    game[x1][y1][1] = 1 
                    game[x][y][0] = '_'
                    game[x][y][1] = 0
                    sign = 1 - sign
                    shash()    
                else:
#xatolik
                    print("Shashka qoidalariga to'g'ri kelmaydi,chunki oradagi narsalarni damka ura olmaydi")             
            else:
                #xatolik
                print("Shashka qoidalariga to'g'ri kelmaydi, chunki damka bunday yurish qila olmaydi")
    else:
        #xatolik
        print('Shashka qoidalariga to\'g\'ri kelmaydi')
        continue

if black: print('Qoralar yutdi!!!')
elif white: print('Oqlar yutdi!!!!')