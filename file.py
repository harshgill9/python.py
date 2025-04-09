# with open ("C:/Users/A/OneDrive/Desktop/Python_project/data.txt", "r") as f:
#     content = f.read()
#     print(content)
#     for line in f:
#         print(line.strip())

#      res=f.readline()
#      print(res)

with open ("C:/Users/A/OneDrive/Desktop/Python_project/data.txt", "w") as f:
    f.write("This is a python")
    f.write("\nThis is a python")

    
with open ("C:/Users/A/OneDrive/Desktop/Python_project/data2.txt", "a") as f:
    f.write("This is a python")
    f.write("\nThis is a python")