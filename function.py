try:
    # Ask the user for a filename
    filename = input("Enter the filename to read: ")

    # Open the file for reading
    with open(filename, "r") as file:
        content = file.read()

    # Modify the content (example: convert text to uppercase)
    modified_content = content.upper()

    # Save the modified content to a new file
    new_filename = f"modified_{filename}"
    with open(new_filename, "w") as new_file:
        new_file.write(modified_content)

    print(f"File modified and saved as {new_filename}")

except FileNotFoundError:
    print("Error: The file was not found. Please check the filename and try again.")

except PermissionError:
    print("Error: Permission denied. You may not have access to this file.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")
