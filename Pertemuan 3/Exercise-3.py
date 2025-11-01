print ("""Temperature Conversion Program
Menu
1. C to F
2. C to K
3. F to C
4. F to K
5. K to C
6. K to F
""")

menu = int(input("Masukan Nomor Menu: "))

if (menu == 1):
    print(f"°C = .2f°F")
elif (menu == 2):
    print(f"°C = .2f}K")
elif (menu == 3):
    print(f"°F = .2f}°C")
elif (menu == 4):
    print(f"°F = .2f}K")
elif (menu == 5):
    print(f"K = .2f}°C")
elif (menu == 6):
    print(f"K = .2f}°F")
else:
    print("Invalid option selected.") 
