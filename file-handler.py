def read_and_write_file():
    while True:
        try:
            # Ask user for input filename
            input_file = input("Enter the filename to read: ")
            
            # Read the content of the input file
            with open(input_file, 'r') as file:
                content = file.read()
            
            break  # Exit loop if file is read successfully
        except FileNotFoundError:
            print(f"Error: '{input_file}' not found. Please try again.")
        except IOError:
            print(f"Error: Unable to read '{input_file}'. Please try again.")

    # Modify the content (example: convert to uppercase)
    modified_content = content.upper()

    # Write the modified content to a new file
    output_file = "modified_" + input_file
    try:
        with open(output_file, 'w') as file:
            file.write(modified_content)
        print(f"Success! Modified content written to '{output_file}'.")
    except IOError:
        print(f"Error: Unable to write to '{output_file}'.")

# Run the program
if __name__ == "__main__":
    read_and_write_file()