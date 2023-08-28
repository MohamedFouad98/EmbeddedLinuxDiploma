import sys

def main():
    # The first command-line argument is the script name itself
    script_name = sys.argv[0]
    print(f"Script name: {script_name}")

    # The rest of the command-line arguments are provided by the user
    if len(sys.argv) > 1:
        arguments = sys.argv[1:]
        print("Command-line arguments:")
        for index, arg in enumerate(arguments, start=1):
            print(f"{index}. {arg}")
    else:
        print("No additional command-line arguments provided.")

if __name__ == "__main__":
   
     main()
