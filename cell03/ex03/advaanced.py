import sys

def print_multiplication_tables():
    # Loop through numbers 0 to 10
    i = 0
    while i <= 10:
        # Print the table for number i
        j = 0
        print(f"Table de {i}: ", end="")
        while j <= 10:
            print(i * j, end=" ")
            j += 1
        print()  # New line after each table
        i += 1

def main():
    # Check if a command-line argument is passed
    if len(sys.argv) > 1 and sys.argv[1] == "yolo":
        print("none$")
        return

    # Otherwise, print the multiplication tables
    print_multiplication_tables()

if __name__ == "__main__":
    main()