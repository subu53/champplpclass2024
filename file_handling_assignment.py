def create_file(filename):
  try:
    with open(filename, "w") as file:
      content = [
          "This is Nairobi\n",
          "1\n",
          "Python master\n"
      ]
      file.writelines(content)
      print(f"File '{filename}' created successfully!")
  except Exception as e:
    print(f"Error creating file: {e}")

def read_file(filename):
  try:
    with open(filename, "r") as file:
      content = file.read()
      print(f"Contents of '{filename}':\n{content}")
  except FileNotFoundError:
    print(f"Error: File '{filename}' not found!")
  except Exception as e:
    print(f"Error reading file: {e}")

def append_to_file(filename, content):
  try:
    with open(filename, "a") as file:
      file.write(content)
      print(f"Content appended to '{filename}' successfully!")
  except Exception as e:
    print(f"Error appending to file: {e}")

# Create the file
create_file("my_file.txt")

# Read and display the file contents (assuming the file was created successfully)
read_file("my_file.txt")

# Append additional content
append_to_file("my_file.txt", "\nTo have ever lived\n")

# Read and display the file contents again to see the appended text
read_file("my_file.txt")
