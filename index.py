from tkinter import END, N, OUTSIDE

        

A = int( input("Donner la valeur de A : "))
B = int( input("Donner la valeur de B : "))

while B > 0 :
        r = A % B
        A = B
        B = r
print(A)