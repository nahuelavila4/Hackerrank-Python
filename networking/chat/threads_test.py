import threading

def saludar(nombre="Coco"):
    print("Hola como estas "+ nombre + "?")

if __name__ =="__main__":
    thread1 = threading.Thread(target=saludar)
    thread2 = threading.Thread(target=saludar, args=("Manuel",))

    thread1.start()
    thread2.start()
    
    thread1.join()
    thread2.join()

    print("Listo")
