import sys

def print_multiplication_tables():

    i = 0
    while i <= 10:
  
        j = 0
        print(f"Table de {i}: ", end="")
        while j <= 10:
            print(i * j, end=" ")
            j += 1
        print() 
        i += 1

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "yolo":
        print("none$")
        return


    print_multiplication_tables()

if __name__ == "__main__":
    main()