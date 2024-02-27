ipv6 = input().strip().split(":")
if ipv6[0] == '': ipv6 = ipv6[1:]
if ipv6[-1] == '': ipv6 = ipv6[:-1]

result = []
for group in ipv6:
    if len(group) == 0: result += ['0000'] * (8-len(ipv6)+1)
    else: result += [group.zfill(4)]

print(":".join(result))