###### Matrix Determinant ######

def DETERMINANT_4X4():
    m1 = ((f*k*p)+(g*l*n)+(h*j*o)) - ((n*k*h)+(o*l*f)+(p*j*g))
    m2 = ((e*k*p)+(g*l*m)+(h*i*o)) - ((m*k*h)+(o*l*e)+(p*i*g))
    m3 = ((e*j*p)+(f*l*m)+(h*i*n)) - ((m*j*h)+(n*l*e)+(p*i*f))
    m4 = ((e*j*o)+(f*k*m)+(g*i*n)) - ((m*j*g)+(n*k*e)+(o*i*f))
    det = (a*m1)+(b*(-1)*m2)+(c*m3)+(d*(-1)*m4)
    return det

fx = "y"
print("****** DeterMatrix By PremerX007!! ******")
print("[Matrix Options]")
print("(1) 3x3 Determinant ")
print("(2) 4x4 Determinant ")
selector = input("[!] You Select .. ")

# 3X3 Matrix Determinant
while(fx == "y" and selector == "1"):
    print("\n**************************")
    print("* 3x3 Matrix Determinant *")
    print("**************************")
    while(True):
        a, b, c = map(int , input("\nแถว 1 : ").split())
        d, e, f = map(int , input("แถว 2 : ").split())
        g, h, i = map(int , input("แถว 3 : ").split())
        det = ((a*e*i)+(b*f*g)+(c*d*h)) - ((g*e*c)+(h*f*a)+(i*d*b))
        print("\nAnswer : %d"%det)
        fx = input("[!] Next?? [y/n] .. ")
        if (fx == "n"):
            break

# 4X4 Matrix Determinant
while(fx == "y" and selector == "2"):
    print("\n**************************")
    print("* 4x4 Matrix Determinant *")
    print("**************************")
    while(True):
        a, b, c, d = map(int , input("\nแถว 1 : ").split())
        e, f, g, h = map(int , input("แถว 2 : ").split())
        i, j, k, l = map(int , input("แถว 3 : ").split())
        m, n, o, p = map(int , input("แถว 4 : ").split())        
        det = DETERMINANT_4X4()
        print("\nAnswer : %d"%det)
        fx = input("[!] Next?? [y/n] .. ")
        if (fx == "n"):
            break

