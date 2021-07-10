# 3x3 Matrix Determinant
print("\n**************************")
print("* 3x3 Matrix Determinant *")
print("**************************")

fx = "y"
while(fx == "y"):
    while(True):
        a, b, c = map(int , input("\nแถว 1 : ").split())
        d, e, f = map(int , input("แถว 2 : ").split())
        g, h, i = map(int , input("แถว 3 : ").split())

        det = ((a*e*i)+(b*f*g)+(c*d*h)) - ((g*e*c)+(h*f*a)+(i*d*b))
        print("\nAnswer : %d"%det)
        fx = input("[!] Next?? [y/n] .. ")
        if (fx == "n"):
            break

