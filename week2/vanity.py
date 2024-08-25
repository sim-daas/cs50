def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    res = False
    l = len(s)
    alp = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
           'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    if l >= 2 and l <= 6 and ' ' not in s and '_' not in s and '.' not in s and '!' not in s and '\"' not in s:
        if s[1] and s[0] in alp:
            for i in range(len(s)):
                if s[i] in alp:
                    res = True
                    pass
                else:
                    if s[i] == '0':
                        res = False
                        break
                    else:
                        for a in range(i+1, len(s)):
                            if s[a] in alp:
                                res = False
                                break
                        break
    return res


if __name__ == '__main__':
    while True:
        main()
