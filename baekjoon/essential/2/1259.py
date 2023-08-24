while True:
    word_list = list(input())

    if word_list[0] == '0':
        break

    word = "".join(word_list)
    word_list.reverse()
    reversed_word = "".join(word_list) 

    if word == reversed_word:
        print("yes")
    else:
        print("no")