def convert(time):
    t = ''
    for a in time:
        if a != ':':
            t += a
        else:
            f = (float('0.' + time[-2:]) / 0.6)
            # t = t + '.' + time[-2:]
            t = float(t) + f
            print(t)
            break
    return t


def main():
    time = convert(input("What time is it? "))
    if time >= 7 and time <= 8:
        print("breakfast time")
    elif time >= 12 and time <= 13:
        print("lunch time")
    elif time >= 18 and time <= 19:
        print("dinner time")
    else:
        pass


if __name__ == '__main__':
    while True:
        main()
