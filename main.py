import customtkinter,pygame
import math
import time
from time import strftime

class RelogioDigital(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        master.title("Relógio")
        # Ajustando as cores conforme o tema
        self.cor_fundo ='black'
        self.cor_relogio = "white" if customtkinter.get_appearance_mode() == "Dark" else "black"

        # Label para o relógio digital
        self.linha = customtkinter.CTkLabel(master, text="hora", font=("Arial", 40))
        
        # Canvas para o relógio analógico
        self.frame = customtkinter.CTkCanvas(master, width=400, height=400, bg=self.cor_fundo, highlightthickness=0)
        
        self.frame.pack()
        self.linha.pack(pady=20)

        self.atualizar_relogio()  
        self.RelogioAnalogico()  

    def atualizar_relogio(self):
        texto = strftime("%H:%M:%S %p")
        self.linha.configure(text=texto)
        self.linha.after(1000, self.atualizar_relogio)

    def tocar_som(self):
        pygame.init()
        try:
            pygame.mixer.Sound("tic_tac.mp3").play()  # Toca o som do tic-tac
        except Exception as e:
            print("Erro ao tocar som:", e)

    def RelogioAnalogico(self):
        self.frame.delete("all")  

        # Desenha o círculo do relógio
        self.frame.create_oval(50, 50, 350, 350, width=4, outline=self.cor_relogio)

        # Desenha os números
        for i in range(12):
            angle = math.radians(i * 30)
            x1 = 200 + 120 * math.sin(angle)
            y1 = 200 - 120 * math.cos(angle)
            self.frame.create_text(x1, y1, text=str(i if i != 0 else 12), font=("Arial", 14, "bold"), fill=self.cor_relogio)

        # Obtém a hora atual
        t = time.localtime()

        # Calcula os ângulos dos ponteiros
        second_angle = math.radians((t.tm_sec * 6) - 90)
        minute_angle = math.radians((t.tm_min * 6) - 90)
        hour_angle = math.radians(((t.tm_hour % 12) * 30 + t.tm_min * 0.5) - 90)        

        # Ponteiro dos segundos
        second_x = 200 + 100 * math.cos(second_angle)        
        second_y = 200 + 100 * math.sin(second_angle)
        self.frame.create_line(200, 200, second_x, second_y, fill='red', width=2)

        # Ponteiro dos minutos
        minute_x = 200 + 80 * math.cos(minute_angle)
        minute_y = 200 + 80 * math.sin(minute_angle)
        self.frame.create_line(200, 200, minute_x, minute_y, fill=self.cor_relogio, width=4)

        # Ponteiro das horas
        hour_x = 200 + 60 * math.cos(hour_angle)
        hour_y = 200 + 60 * math.sin(hour_angle)        
        self.frame.create_line(200, 200, hour_x, hour_y, fill=self.cor_relogio, width=6)

        # Ponto central
        self.frame.create_oval(195, 195, 205, 205, fill=self.cor_relogio)
        self.tocar_som()
        # Atualiza o relógio a cada segundo
        self.frame.after(1000, self.RelogioAnalogico)

# Criando a janela principal
app = customtkinter.CTk()
relogio = RelogioDigital(app)
app.mainloop()
pygame.quit()
