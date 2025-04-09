
# Handling Multiple Exceptions

try:
    with open ("Existing_file.txt","r") as file:
       for line in file:
           print(line.strip())
     
except FileNotFoundError:
    print("Error: The file not found .")
except Exception as e:
    print(f"An unexpectid error occurred: {e}")


    # Finally Blog
finally:
    #db close
    print("clearing up......")