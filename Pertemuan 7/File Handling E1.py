def write_biodata(filename, name, age, address, email):
    """Write user biodata into a text file."""
    with open(filename, "w") as file:
        file.write("Name: {name}\n")
        file.write("Age: {age}\n")
        file.write("Address: {address}\n")
        file.write("Email: {email}\n")


def read_biodata(filename):
    """Read and display biodata from the text file."""
    try: 
        with open(filename, "r") as file:
            content = file.read()
            print("=== Biodata Content ===")
            print(content)
    except FileNotFoundError:
            print("File not found. Please write biodata first.")

# Example usage
if __name__ == "__main__":
    # User input
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    address = input("Enter your address: ")
    email = input("Enter your email: ")

    filename = "Biodata.txt"
