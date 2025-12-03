def create_file(filename, data):
    """Create a new file and write initial data."""
    with open(filename, "w") as file:
        file.write(data + "\n")
    print(f"File '{filename}' created successfully.")


def read_file(filename):
    """Read and display the content of a file."""
    try:
        with open(filename, "r") as file:
            print("\n=== File Content ===")
            print(file.read())
    except FileNotFoundError:
        print(f"File '{filename}' not found. Please create it first.")


def append_file(filename, data):
    """Append new data to an existing file."""
    try:
        with open(filename, "a") as file:
            file.write(data + "\n")
        print(f"Data appended to '{filename}' successfully.")
    except FileNotFoundError:
        print(f"File '{filename}' not found. Please create it first.")


def main():
    """Main program loop with branching and looping."""
    while True:
        print("\n=== File Handling Menu ===")
        print("1. Create File")
        print("2. Read File")
        print("3. Append to File")
        print("4. Close Program")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            filename = input("Enter file name: ")
            data = input("Enter initial data: ")
            create_file(filename, data)

        elif choice == "2":
            filename = input("Enter file name: ")
            read_file(filename)

        elif choice == "3":
            filename = input("Enter file name: ")
            data = input("Enter data to append: ")
            append_file(filename, data)

        elif choice == "4":
            print("Closing program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


# Run the program
if __name__ == "__main__":
    main()
