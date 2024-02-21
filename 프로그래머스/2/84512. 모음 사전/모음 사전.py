def solution(word):    
    alphabets = ['A', 'E', 'I', 'O', 'U']
    alphabet_dict = {}
    
    current_word = [""] * 5
    count = 1
    for i in range(5):
        current_word[0] = alphabets[i]
        for h in range(1, 5): current_word[h] = ""
        alphabet_dict["".join(current_word)] = count
        count += 1
        
        for j in range(5):
            current_word[1] = alphabets[j]
            for h in range(2, 5): current_word[h] = ""
            alphabet_dict["".join(current_word)] = count
            count += 1
            
            for k in range(5):
                current_word[2] = alphabets[k]
                for h in range(3, 5): current_word[h] = ""
                alphabet_dict["".join(current_word)] = count
                count += 1
                
                for x in range(5):
                    current_word[3] = alphabets[x]
                    for h in range(4, 5): current_word[h] = ""
                    alphabet_dict["".join(current_word)] = count
                    count += 1

                    for y in range(5):
                        current_word[4] = alphabets[y]
                        alphabet_dict["".join(current_word)] = count
                        count += 1
    
    answer = alphabet_dict.get(word)
    return answer