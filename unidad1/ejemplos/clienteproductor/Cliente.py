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
    
    valor = 0
    while valor < 9:  # Leeremos 9 datos
        try:
            # Abrimos el archivo y creamos un bloqueo
            with open(nombre_fichero, 'r+') as archivo, FileLock(nombre_fichero + ".lock"):
                print("Cliente: ENTRA sección")
                
                # Leemos el valor del archivo
                archivo.seek(0)
                contenido = archivo.read().strip()
                if contenido:  # Si hay contenido
                    valor = int(contenido)
                    archivo.seek(0)
                    archivo.truncate()  # Vaciamos el archivo
                    print(f"Cliente: valor leído {valor}")
                else:
                    print("Cliente: no puede leer, archivo está vacío.")
                
                print("Cliente: SALE sección")
            
            # Simulamos tiempo de procesamiento del dato
            time.sleep(1)
        
        except Exception as e:
            print(f"Cliente. Error: {str(e)}")
            break

if __name__ == "__main__":
    main()
