
alpha = "abcdefghijklmnopqrstuvwxyz"

str_in = input("Enter message to encrypt: ").lower()
shift = int(input("Enter a shift value to encrypt with: "))

n = len(str_in)
str_out = ""

for i in range(n) : 
    print(str_in[i])
    c = str_in[i]
    loc = alpha.find(c)
    print(loc)
    newloc = (loc + shift)%26
    print(newloc)
    str_out += alpha[newloc]
    print(alpha[newloc])

print ("Obfuscated version:", str_out) 