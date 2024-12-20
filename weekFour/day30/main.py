try:
    file = open("a_file.text")
    a_dictionary = {"key": "value"}
    print(a_dictionary["adgahwwg"])
except FileNotFoundError:
    file = open("a_file.text", "w")
    file.write("This is the content of the file.")
except KeyError as error_message:
    print(f"The key {error_message} you're trying to access does not exist in the dictionary.")