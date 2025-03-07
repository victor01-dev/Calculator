import customtkinter as ctk

class Calculadora:
  def __init__(self,root):
    self.root = root
    self.root.title("Calculadora")
    self.root.configure(bg = "#2b3e50")
    self.root.geometry("350x500")
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")
  # Obtener tamaño de pantalla
    screen_width = self.root.winfo_screenwidth()
    screen_height = self.root.winfo_screenheight()
    
    # Calcular la posición para centrar
    x_pos = (screen_width // 2) - (350 // 2)
    y_pos = (screen_height // 2) - (500 // 2)
    
    # Establecer la geometría con la nueva posición
    self.root.geometry(f"350x500+{x_pos}+{y_pos}")
    
    # Establecer autoajuste de tamaño para la ventana
    for i in range(5):  
            self.root.grid_rowconfigure(i, weight=1)
    for i in range(4):  
        self.root.grid_columnconfigure(i, weight=1)
    
    self.pantalla = ctk.CTkEntry(self.root, width=300, height=30, 
                                     font=("System", 30), justify="right") 
    self.pantalla.grid(row=0, column=0, padx=5, pady=10, columnspan=4, sticky="nsew")
    
    self.crear_botones()
  
  # Botones y posiciones
  def crear_botones(self):
    botones = [
      ("1", 1, 0), ("2", 1, 1), ("3", 1, 2),
      ("4", 2, 0), ("5", 2, 1), ("6", 2, 2),
      ("7", 3, 0), ("8", 3, 1), ("9", 3, 2),
      ("0", 4, 0), ("+", 1, 3), ("-", 2, 3),
      ("*", 3, 3), ("/", 4, 3), ("=", 4, 1),
      ("C", 4, 2)
    ]
    
    for (text, row, col) in botones:
      button = ctk.CTkButton(self.root, text=text, font=("System", 30),
                            fg_color="#6c3483", hover_color="#bb8fce",
                            command=lambda t=text: self.boton_click(t))
      button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
      
  def boton_click(self, valor):
    if valor == "=":
      try:
        result = str(eval(self.pantalla.get()))
        self.pantalla.delete(0, ctk.END)
        self.pantalla.insert(0, result)
      except:
        self.pantalla.delete(0, ctk.END)
        self.pantalla.insert(0, "Error")
    elif valor == "C":
      self.pantalla.delete(0, ctk.END)
    else:
      current = self.pantalla.get()
      self.pantalla.delete(0, ctk.END)
      self.pantalla.insert(0, current + valor)

root = ctk.CTk()
calculadora = Calculadora(root)
root.mainloop()