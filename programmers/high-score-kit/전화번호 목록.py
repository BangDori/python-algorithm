def solution(phone_book):
    phone_dict = {}
    
    phone_book.sort(key=lambda k: len(k))
    min_length = len(phone_book[0])
    
    phone_dict[phone_book[0]] = True

    for phone in phone_book:
        max_length = len(phone)
        
        if phone_book[0] == phone:
            continue
        
        for count in range(min_length, len(phone)+1):
            if phone_dict.get(phone[:count]):
                print(phone)
                print(phone[:count])
                return False
        
        phone_dict[phone] = True
        
    return True