import random
a = random.randint(1,100)
b = 10
while b > 0:
    c = 0
    while True:
        str = input("Tahmininiz:\n")
        try:
            c = int(str)
            break
        except:
            print("Lütfen sayı giriniz")
    if c == a:
        print("Tebrikler doğru bildin")
    elif c > a:
        print("Hop kardeş fazla attın azalt azıcık")
    else:
        print("Artır az kardeşim ya")
    b = b-1