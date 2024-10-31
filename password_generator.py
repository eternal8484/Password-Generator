password = "G5p*L9qW!k3@#n8R4eZ^f&O6y(2)mX1+C$v7D-Ju0a)bP%U_~iQcTzxYhM?V[N]o|lA:B;sF,E+Hw"

user_q1 = int(input("Enter the length of the password: "))

gap = None 
if(user_q1 == 8):
    gap = 3
elif(user_q1 == 10):
    gap = 4
else:
    gap = 2

generated_password = password[0::gap]
final = generated_password[0:user_q1]
print(final)
