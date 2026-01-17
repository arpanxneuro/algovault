if __name__ == '__main__':
    N = int(input())
    lst = []
    
    for _ in range(N):
        inp = input()
        if 'insert' in inp:
            splitted = inp.split()
            lst.insert(int(splitted[1]), int(splitted[2]))
        elif 'print' in inp:
            print(lst)
        elif 'remove' in inp:
            splitted = inp.split()
            lst.remove(int(splitted[1]))
        elif 'append' in inp:
            splitted = inp.split()
            lst.append(int(splitted[1]))
        elif 'sort' in inp:
            lst.sort()
        elif 'pop' in inp:
            lst.pop()
        elif 'reverse' in inp:
            lst.reverse()