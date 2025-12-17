# skips over unlucky number 13

for x in range(1,21):
    if x == 13:
        continue
    else:
        print(x,end=" ")