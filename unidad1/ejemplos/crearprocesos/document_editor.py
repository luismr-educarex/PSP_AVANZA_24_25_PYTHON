import tkinter as tk
from tkinter import filedialog, messagebox

class DocumentEditor(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Editor de Texto")
        self.geometry("600x400")

        # Crear un área de texto con barra de desplazamiento
        self.text_area = tk.Text(self)
        self.scroll_bar = tk.Scrollbar(self, command=self.text_area.yview)
        self.text_area.config(yscrollcommand=self.scroll_bar.set)
        self.scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
        self.text_area.pack(expand=True, fill=tk.BOTH)

        # Crear un menú
        self.menu_bar = tk.Menu(self)
        self.config(menu=self.menu_bar)

        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Archivo", menu=self.file_menu)

        self.file_menu.add_command(label="Abrir", command=self.open_file)
        self.file_menu.add_command(label="Guardar", command=self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Salir", command=self.exit_app)

    def open_file(self):
        try:
            file_path = filedialog.askopenfilename()
            if file_path:
                with open(file_path, 'r') as file:
                    content = file.read()
                    self.text_area.delete(1.0, tk.END)
                    self.text_area.insert(tk.END, content)
        except Exception as e:
            messagebox.showerror("Error", f"Error al abrir el archivo: {str(e)}")

    def save_file(self):
        try:
            file_path = filedialog.asksaveasfilename(defaultextension=".txt")
            if file_path:
                with open(file_path, 'w') as file:
                    content = self.text_area.get(1.0, tk.END)
                    file.write(content)
        except Exception as e:
            messagebox.showerror("Error", f"Error al guardar el archivo: {str(e)}")

    def exit_app(self):
        self.quit()

if __name__ == "__main__":
    app = DocumentEditor()
    app.mainloop()
