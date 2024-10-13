import tkinter as tk
from tkinter import messagebox
from document_editor import DocumentEditor  # Importa la clase DocumentEditor

class CrearProcesosView(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Crear Procesos")
        self.geometry("400x200")
        
        # Crear componentes
        self.status_message_label = tk.Label(self, text="Presiona el botón para abrir un nuevo editor.")
        self.status_message_label.pack(pady=20)

        self.crear_proceso_button = tk.Button(self, text="Abrir Editor", command=self.crear_nuevo_editor)
        self.crear_proceso_button.pack(pady=20)

    def crear_nuevo_editor(self):
        try:
            # En lugar de crear un proceso externo, instanciamos el editor directamente
            nuevo_editor = DocumentEditor()
            nuevo_editor.mainloop()  # Abrir la ventana del editor
            self.status_message_label.config(text="Editor abierto exitosamente.")
        except Exception as ex:
            self.status_message_label.config(text=f"Error al abrir el editor: {str(ex)}")
            messagebox.showerror("Error", f"Error al abrir el editor: {str(ex)}")

if __name__ == "__main__":
    app = CrearProcesosView()
    app.mainloop()
