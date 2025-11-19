def addition(value1 = 0, value2 = 0):
    return value1 + value2;
    
def addition(value1 = 0, value2 = 0):
    return value1 - value2;
    
def addition(value1 = 0, value2 = 0):
    return value1 / value2;
    
def addition(value1 = 0, value2 = 0):
    return value1 * value2;
    
def addition(value1 = 0, value2 = 0):
    return value1 % value2;
    
def banner():
    print("""
--------------------
| Stefanus Marlo G |
|     Bintaro      |
--------------------
    """)
    
banner()

while(True):
    menu = input("Enter Menu (+|-|/|*|%|stop): ") 
    
    if (menu == "stop"):
        break
    elif (menu == "+"):
        value1 = int(input("Masukan Nilai 1: "))
        value2 = int(input("Masukan Nilai 2: "))
        hasil = addition(value1, value2)
        print("The result of subtraction", value1, "+", value2, "is", hasil)
        
    if (menu == "stop"):
        break
    elif (menu == "-"):
        value1 = int(input("Masukan Nilai 1: "))
        value2 = int(input("Masukan Nilai 2: "))
        hasil = addition(value1, value2)
        print("The result of subtraction", value1, "-", value2, "is", hasil)
        
    if (menu == "stop"):
        break
    elif (menu == "/"):
        value1 = int(input("Masukan Nilai 1: "))
        value2 = int(input("Masukan Nilai 2: "))
        hasil = addition(value1, value2)
        print("The result of subtraction", value1, "/", value2, "is", hasil) 
        
    if (menu == "stop"):
        break
    elif (menu == "*"):
        value1 = int(input("Masukan Nilai 1: "))
        value2 = int(input("Masukan Nilai 2: "))
        hasil = addition(value1, value2)
        print("The result of subtraction", value1, "*", value2, "is", hasil)
    
    if (menu == "stop"):
        break
    elif (menu == "%"):
        value1 = int(input("Masukan Nilai 1: "))
        value2 = int(input("Masukan Nilai 2: "))
        hasil = addition(value1, value2)
        print("The result of subtraction", value1, "%", value2, "is", hasil)
    
    operation_names = {
        "+" "addition",
        "-" "subtraction",
        "/" "division",
        "*" "multiplication",
        "%" "modulus",
        
#Run the program
    }
