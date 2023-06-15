with open('appPage.py', 'rb') as f:
    for line in f:
        line_list = []
        for char in line:
            line_list.append("%02X" % (char))
        print(' '.join(line_list))