while True:
    try:
        height = int(input("Height: "))
        if type(height) is int:
            if height > 0 and height < 9:
                for i in range(1,height+1):
                    print(" "*(height-i)+"#"*i +"  "+"#"*i)
                break
            else:
                continue
        else:
            continue
    except ValueError:
        continue