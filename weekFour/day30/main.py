try:
    file = open("a_file.text")
    a_dictionary = {"key": "value"}
    print(a_dictionary["key"])
except FileNotFoundError:
    file = open("a_file.text", "w")
    file.write("This is the content of the file.")
except KeyError as error_message:
    print(f"The key {error_message} you're trying to access does not exist in the dictionary.")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("The file has been closed.")