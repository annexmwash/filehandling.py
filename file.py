def modify_content(content):
    """
    Modify the content as needed.
    For example, convert to uppercase (you can customize this).
    """
    return content.upper()


def read_file(filename):
    """
    Read the content of the file.
    """
    with open(filename, 'r') as file:
        content = file.read()
    return content


def write_file(filename, content):
    """
    Write the modified content to a new file.
    """
    with open(filename, 'w') as file:
        file.write(content)


def main():
    filename = input("Enter the name of the file to read: ")

    try:
        content = read_file(filename)
        print("✅ File read successfully.")

        modified = modify_content(content)
        new_filename = "modified_" + filename
        write_file(new_filename, modified)

        print(f"✏️ Modified content written to: {new_filename}")

    except FileNotFoundError:
        print("❌ Error: File not found.")

    except IOError:
        print("❌ Error: Could not read/write the file.")


if __name__ == "__main__":
    main()
