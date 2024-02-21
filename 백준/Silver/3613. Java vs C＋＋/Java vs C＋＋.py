def convertCPlusPlusToJava(variable):
    words = []

    word = ""
    for alpha in variable:
        if alpha.isupper():
            words.append(word + UNDERLINE)
            word = alpha.lower()
            continue

        word += alpha

    return "".join(words) + word

def convertJavaToCPlusPlus(variable):
    words = []

    word = ""
    for alpha in variable:
        if alpha == UNDERLINE:
            words.append(word)
            word = ""
            continue

        if len(word) == 0: word += alpha.upper()
        else: word += alpha
    
    return words[0][0].lower() + "".join(words)[1:] + word

UNDERLINE = "_"
ERROR_MSG = "Error!"

variable = input().strip()
isJava, isCPlusPlus = False, False
isError = False

answer = "Error!"

if variable[0].isupper() or variable[0] == UNDERLINE or variable[-1] == UNDERLINE:
    print(ERROR_MSG)
else:
    # Java, C++ Check
    for i, alpha in enumerate(variable):
        if alpha == UNDERLINE:
            isJava = True
            if i+1 < len(variable) and variable[i+1] == UNDERLINE:
                isError = True
        if alpha.isupper(): isCPlusPlus = True

    if isError:
        answer = ERROR_MSG
    elif isJava and not isCPlusPlus:
        answer = convertJavaToCPlusPlus(variable)
    elif not isJava and isCPlusPlus:
        answer = convertCPlusPlusToJava(variable)
    elif not isJava and not isCPlusPlus:
        answer = variable

    print(answer)