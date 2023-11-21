from itertools import combinations
import sys
input = sys.stdin.readline

pwd_length, alphabet_count = map(int, input().split())
alphabet_list = list(input().split())

password_dict = {}

for password in combinations(alphabet_list, pwd_length):    
    current_password = list(password)
    current_password.sort()

    predicted_password = "".join(current_password)

    if not password_dict.get(predicted_password):
        password_dict[predicted_password] = 1

passwords = list(password_dict.keys())
passwords.sort()

consonant = ['a', 'e', 'i', 'o', 'u']

for password in passwords:
    tot_length = len(password)

    consonant_length = 0
    for cons in consonant:
        consonant_length += password.count(cons)

    if tot_length - consonant_length < 2 or consonant_length < 1:
        continue

    print(password)