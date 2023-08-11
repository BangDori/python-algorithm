croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

alpha = input()
word = 0

for i in range(len(croatia)):
    if alpha.find(croatia[i]) >= 0:
        temp = alpha.split(croatia[i])
        count = len(temp)
        word += (count-1)
        alpha = " ".join(temp)

word += len(alpha.replace(" ", ""))
print(word)
