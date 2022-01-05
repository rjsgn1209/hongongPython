while 1:
    try:
        r = float(input("값을 입력하세요: "))
        pi = 3.14

        l = float(2) * pi * r
        s = r ** float(2) * pi

        print("둘레:", l, "면적:", s)
    except:
        continue