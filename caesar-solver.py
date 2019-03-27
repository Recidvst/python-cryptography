
alpha = "abcdefghijklmnopqrstuvwxyz"

str_in = input("Enter message to decrypt: ").lower()

n = len(str_in)
str_out = ""

shift = 1
attempts = 26

for t in range(attempts) :
    for i in range(n) : 
        c = str_in[i]
        loc = alpha.find(c)
        newloc = (loc + shift)%26
        str_out += alpha[newloc]
        if len(str_out) == n :
            print(str_out)
    str_out = ''
    shift += 1 
        
