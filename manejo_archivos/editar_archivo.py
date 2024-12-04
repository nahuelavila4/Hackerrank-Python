def create():
    f = open("default.txt", "w")
    f.write("Hello world, how are you?")
    f.close()
    f = open("default.txt", "r")
    print(f.read())


create()




