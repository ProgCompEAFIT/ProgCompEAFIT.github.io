nums = int(raw_input())
while(nums!=0):
    entrada = raw_input().strip().split()
    modificados = []
    for i in entrada: modificados.append(int("".join(sorted(i))))
    print(sorted(modificados)[-1])
    nums = int(raw_input())
