import os
import time
from filelock import FileLock

def main():
    nombre_fichero = ""
    
    # Identificamos el sistema operativo
    if os.name == 'nt':  # Windows
        nombre_fichero = "C:\\PSP\\PROGRAMAS\\PYTHON\\buffer.txt"
    else:  # GNU/Linux
        nombre_fichero = "/home/usuario/buffer.txt"
    
    i = 0
    while i < 10:  # Escribiremos 10 datos
        try:
            # Abrimos el archivo y creamos un bloqueo
            with open(nombre_fichero, 'w+') as archivo, FileLock(nombre_fichero + ".lock"):
                print("Suministrador: ENTRA sección")
                
                # Si el archivo está vacío, escribimos un valor
                archivo.seek(0)
                contenido = archivo.read()
                if not contenido:  # El archivo está vacío
                    archivo.seek(0)
                    archivo.write(f"{i}\n")
                    archivo.flush()
                    print(f"Suministrador: valor escrito {i}")
                    i += 1
                else:
                    print("Suministrador: no puede escribir, archivo no está vacío.")
                
                print("Suministrador: SALE sección")
            
            # Simulamos tiempo de creación del dato
            time.sleep(0.5)
        
        except Exception as e:
            print(f"Suministrador. Error: {str(e)}")
            break

if __name__ == "__main__":
    main()
