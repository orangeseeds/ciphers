def encrypt(message, key):
    if not (key >= 2 and key <= len(message)//2):
        print('key should be in the range [2,(message length)/2]')
        return ''
    n = key - 1
    length = len(message)
    cipher_text = ''
    try:
        for i in range(0,key):
            for j in range(0 , length//key + key + 1):
                if(j*key + i) < length:
                    cipher_text = cipher_text + message[j*key + i]
        return(cipher_text)
    except Exception as e:
        print(e)
        raise

def decrypt(message, key):
    if not (key >= 2 and key <= len(message)//2):
        print('key should be in the range [2,(message length)/2]')
        return ''
    n = key - 1
    length = len(message)

    main_array = []
    new_array = []
    plain_text = ''
    for i in range(0, key):
        main_array.append([i])
        for j in range(1, length//key):
            main_array[i].append(j*key + i)
        if i < length%key:
            main_array[i].append((len(main_array[i]))*key+i)

    # for k in range(0, length%key):
    #     main_array[k].append((len(main_array[k]))*key+k)
    # for member in main_array:
    #     new_array = new_array+member

    new_array = [item for sublist in main_array for item in sublist]

    for l in range(0, length):
        index = new_array.index(l)
        plain_text = plain_text + message[index]
    return(plain_text)
    # print(plain_text)


# cipher_text = encrypt('''The primary goal of this event wasto raise  awareness  of  technical  talent  at  OSU  and  foster  a competitive,  yet  cooperative,  and  congenial  culture  for  talented  individuals.It  also  allowed participants to connect with faculty, labs, centers on campus, and most importantly, with each other: "We didn't know each other before we did this", said one team, who went from being strangers to working  together  over  20+  hours  and  producing  a  demonstrable  project.''', 4)
# plain_text = decrypt(cipher_text, 4)
#
# print(cipher_text)
# print(plain_text)
