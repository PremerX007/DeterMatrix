###### Matrix Determinant ######

def DETERMINANT_4X4():
    m1 = ((f*k*p)+(g*l*n)+(h*j*o)) - ((n*k*h)+(o*l*f)+(p*j*g))
    m2 = ((e*k*p)+(g*l*m)+(h*i*o)) - ((m*k*h)+(o*l*e)+(p*i*g))
    m3 = ((e*j*p)+(f*l*m)+(h*i*n)) - ((m*j*h)+(n*l*e)+(p*i*f))
    m4 = ((e*j*o)+(f*k*m)+(g*i*n)) - ((m*j*g)+(n*k*e)+(o*i*f))
    det = (a*m1)+(b*(-1)*m2)+(c*m3)+(d*(-1)*m4)
    return det

def ADJOINT():
    o1 = (e*i)-(h*f)
    o2 = (d*i)-(g*f)
    o3 = (d*h)-(g*e)
    t1 = (b*i)-(h*c)
    t2 = (a*i)-(g*c)
    t3 = (a*h)-(g*b)
    h1 = (b*f)-(e*c)
    h2 = (a*f)-(d*c)
    h3 = (a*e)-(d*b)
    print("[%d %d %d]"%(o1,t1*-1,h1))
    print("[%d %d %d]"%(o2*-1,t2,h2*-1))
    print("[%d %d %d]"%(o3,t3*-1,h3))
    return

fx = "m"
print("****** DeterMatrix By PremerX007!! ******")
while(fx == "m"):
    fx = "y"
    print("\n[Matrix Menu]")
    print("(1) 3x3 Determinant")
    print("(2) 4x4 Determinant")
    print("(3) Adjoint Matrix\n...")
    selector = input("[!] You Select .. ")

    # 3X3 Matrix Determinant
    while(fx == "y" and selector == "1"):
        print("\n**************************")
        print("* 3x3 Matrix Determinant *")
        print("**************************")
        while(True):
            a, b, c = map(int , input("\nRow 1 : ").split())
            d, e, f = map(int , input("Row 2 : ").split())
            g, h, i = map(int , input("Row 3 : ").split())
            det = ((a*e*i)+(b*f*g)+(c*d*h)) - ((g*e*c)+(h*f*a)+(i*d*b))
            print("\nAnswer : %d"%det)
            fx = input("[!] (Press M to back Menu) | Next choices?? [y/n] .. ")
            if (fx == "n" or "m"):
                break

    # 4X4 Matrix Determinant
    while(fx == "y" and selector == "2"):
        print("\n**************************")
        print("* 4x4 Matrix Determinant *")
        print("**************************")
        while(True):
            a, b, c, d = map(int , input("\nRow 1 : ").split())
            e, f, g, h = map(int , input("Row 2 : ").split())
            i, j, k, l = map(int , input("Row 3 : ").split())
            m, n, o, p = map(int , input("Row 4 : ").split())        
            det = DETERMINANT_4X4()
            print("\nAnswer : %d"%det)
            fx = input("[!] (Press M to back Menu) | Next choices?? [y/n] .. ")
            if (fx == "n" or "m"):
                break

    # Adjoint Matrix
    while(fx == "y" and selector == "3"):
        print("\n******************")
        print("* Adjoint Matrix *")
        print("******************")
        while(True):
            a, b, c = map(int , input("\nRow 1 : ").split())
            d, e, f = map(int , input("Row 2 : ").split())
            g, h, i = map(int , input("Row 3 : ").split())        
            print("\n***Answer***")
            ADJOINT()
            fx = input("\n[!] (Press M to back Menu) | Next choices?? [y/n] .. ")
            if (fx == "n" or "m"):
                break

