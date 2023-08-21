while True:
    sentence = input().upper()

    if sentence == '.':
        break

    sentence = sentence.replace(" ", "")

    parenthesis = []
    for i in range(len(sentence)):
        if not (sentence[i] >= 'A' and sentence[i] <= 'Z'):
            parenthesis.append(sentence[i])
    
    quiz = "".join(parenthesis)
    
    while quiz.count('()') or quiz.count('[]'):
        quiz = quiz.replace('()', '')
        quiz = quiz.replace('[]', '')
    
    if quiz == '.':
        print("yes")
    else:
        print("no")