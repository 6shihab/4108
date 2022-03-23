Alphabet = [(chr(65+i)) for i in range(26)]
Alphabet.pop(Alphabet.index("J"))

k = "monarchy"
key = k.upper()
print(k)
key_list = []

for i in key:
    if i not in key_list:
        key_list.append(i)

key_list += [i for i in Alphabet if i not in key_list]
key_mat = [[0 for i in range(5)] for j in range(5)]     # init 5*5 matrix

for i in range(0, 5):
    for j in range(0, 5):
        key_mat[i][j] = key_list[4*i+(i+j)]

for i in range(0, 5):
    print(key_mat[i])


def location(List_2d, String):
    for i, x in enumerate(List_2d):
        if String in x:
            return [i, x.index(String)]


def diagraph(String):
    paired_char_list = []
    List = [i for i in String]
    if len(List) % 2 != 0:
        List.append("X")
    pair_list = [[List[i], List[i+1]] for i in range(0, len(List), 2)]

    for i in range(0, len(pair_list)):
        char = ""
        if len(set(pair_list[i])) != len(pair_list[i]):
            char += pair_list[i][0] + "X"
            paired_char_list.append(char)
            char = ""
            char += pair_list[i][1] + "X"
            paired_char_list.append(char)
            char = ""
        else:
            char += pair_list[i][0] + pair_list[i][1]
            paired_char_list.append(char)
            char = ""
    print(paired_char_list)
    return paired_char_list


def encryption(String):
    encrypted = []
    char = ""
    index_1st = location(key_mat, String[0])
    index_2nd = location(key_mat, String[1])

    if index_1st[0] == index_2nd[0]:
        encrypted.append(key_mat[index_1st[0]][(index_1st[1] + 1) % 5])
        encrypted.append(key_mat[index_2nd[0]][(index_2nd[1] + 1) % 5])
        char += encrypted[0]
        char += encrypted[1]
        return char

    elif index_1st[1] == index_2nd[1]:
        encrypted.append(key_mat[index_1st[0] + 1 % 5][index_1st[1]])
        encrypted.append(key_mat[index_2nd[0] + 1 % 5][index_2nd[1]])
        char += encrypted[0]
        char += encrypted[1]
        return char
    else:
        encrypted.append(key_mat[index_1st[0]][index_2nd[1]])
        encrypted.append(key_mat[index_2nd[0]][index_1st[1]])
        char += encrypted[0]
        char += encrypted[1]
        return char


message = input("Insert mesage: ")
message = message.replace(" ", "")
message = message.upper()

msg = diagraph(message)
char = ""
for i in range(0, len(msg)):
    char += " " + encryption(msg[i])

print(char)

