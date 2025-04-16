def modify_and_write_file():
    """
    Reads a file specified by the user, modifies its content,
    and writes the modified content to a new file.
    Handles potential file-related errors.
    """
    while True:
        input_filename = input("Enter the name of the file to read: ")
        try:
            with open(input_filename, 'r') as infile:
                content = infile.readlines()
            break  # Exit the loop if the file is read successfully
        except FileNotFoundError:
            print(f"Error: File '{input_filename}' not found. Please try again.")
        except PermissionError:
            print(f"Error: Permission denied to read file '{input_filename}'.")
        except Exception as e:
            print(f"An unexpected error occurred while reading the file: {e}")

    # Modify the content (example: add a line number to each line)
    modified_content = [f"{i+1}: {line}" for i, line in enumerate(content)]

    output_filename = input("Enter the name for the new output file: ")
    try:
        with open(output_filename, 'w') as outfile:
            outfile.writelines(modified_content)
        print(f"Successfully wrote the modified content to '{output_filename}'.")
    except PermissionError:
        print(f"Error: Permission denied to write to file '{output_filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred while writing to the file: {e}")

if __name__ == "__main__":
    modify_and_write_file()