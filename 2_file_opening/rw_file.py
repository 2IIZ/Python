


# r - read / w - write (data erased when opened) / a - append (add to the end of file)
file_object  = open("rw_file.html", "r")

print(file_object.read())

file_object.close() # close the file - good practice
