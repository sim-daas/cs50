def main(file):
    for i in range(len(file)):
        if file[i] == '.':
            ext = file[-(len(file) - i - 1):]
            if ext in ['gif', 'jpeg', 'jpg', 'png', 'pdf', 'txt', 'zip']:
                print('image/'+ext)
            else:
                print('application/octet-stream')
            break
    if '.' in file:
        pass
    else:
        print('application/octet-stream')


if __name__ == '__main__':
    while True:
        main(input("Enter file name - "))
