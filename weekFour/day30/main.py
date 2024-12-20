try:
    file = open("a_file.text")
except:
    file = open("a_file.text", "w")
    file.write("This is the content of the file.")