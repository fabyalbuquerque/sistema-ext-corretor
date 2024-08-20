import customtkinter as ctk
from tkinter import *

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.windows_config()
        self.tema_config()
        self.frontend()

    #layout janela
    def windows_config(self):
        self.title("EXT CORRETOR") #titulo
        self.geometry("800x650") #tamanho
        self._set_appearance_mode("Sytem")
        self.minsize(width=800, height=650) #nao minimiza
    
    #switch tema (dark or light)
    def tema_config(self):
        
        #Definindo valores iniciais das variaveis
        self.switch_var = ctk.StringVar(value="off")
        self.text_var = ctk.StringVar(value="Light")
        
        #função do comando
        def set_tema():  
              
            if self.switch_var.get() == 'on':
                ctk.set_appearance_mode("Dark")
                self.text_var.set("Dark")
                            
            elif self.switch_var.get() == 'off':
                ctk.set_appearance_mode("Light")
                self.text_var.set("Light")
                
            else:
                ctk.set_appearance_mode("System")
            
        
        self.switch = ctk.CTkSwitch(self, textvariable=self.text_var, variable=self.switch_var, onvalue="on", offvalue="off", command=set_tema)
        self.switch.place(x=25, y=20)
        
    def frontend(self):
        
        # TÍTULO
        self.tt = ctk.CTkLabel(self, text="GERENCIAMENTO", font=("arial bold", 30))
        self.tt.pack(pady=20)
        
        # MENU
        self.tabview = ctk.CTkTabview(self,
                                      width=700,
                                      height=500,
                                      corner_radius=8,
                                      border_width=2,
                                      segmented_button_fg_color="grey",
                                      segmented_button_selected_color="#037",
                                      segmented_button_selected_hover_color="#111",
                                      segmented_button_unselected_color="#333",)
        self.tabview.pack(pady=10)
        self.tabview.add("Clientes")
        self.tabview.add("Apólices")
        self.tabview.add("Pagamentos")
        self.tabview.tab("Clientes").grid_columnconfigure(1,weight=1)
        self.tabview.tab("Apólices").grid_columnconfigure(1, weight=1)
        self.tabview.tab("Pagamentos").grid_columnconfigure(1, weight=1)
        
        # TELA CLIENTES
        self.trm = ctk.CTkLabel(self.tabview.tab("Clientes"), text="Busca e Cadastro de Clientes", font=("arial bold", 20))
        self.nome = ctk.CTkLabel(self.tabview.tab("Clientes"), text="Nome", font=("arial bold", 14))
        self.cpf = ctk.CTkLabel(self.tabview.tab("Clientes"), text="CPF", font=("arial bold", 14))
        self.endereco = ctk.CTkLabel(self.tabview.tab("Clientes"), text="Endereço", font=("arial bold", 14))
        self.info = ctk.CTkLabel(self.tabview.tab("Clientes"), text="Informações Adicionais", font=("arial bold", 14))
        
        self.cl_nome_entry = ctk.CTkEntry(self.tabview.tab("Clientes"), width=450, height=35, font=("arial", 16))
        self.cl_cpf_entry = ctk.CTkEntry(self.tabview.tab("Clientes"), width=150, height=35, font=("arial", 16))
        self.cl_endereco_entry = ctk.CTkEntry(self.tabview.tab("Clientes"), width=275, height=35, font=("arial", 16))
        self.cl_seguro_entry = ctk.CTkComboBox(self.tabview.tab("Clientes"), values=["AUTO", "RESIDENCIAL", "EMPRESARIAL", "VIDA", "DENTAL", "SAUDE"], 
                                            fg_color="#333", width=150, height=35, font=("arial", 16))
        self.cl_seguro_entry.set("Seguro")
        self.cl_dados_bancarios_entry = ctk.CTkOptionMenu(self.tabview.tab("Clientes"), values=["CAIXA", "BRADESCO", "NUBANK", "ITAU", "BANCO DO BRASIL", "SICOOB"], 
                                            fg_color="#333", width=130, height=35, font=("arial", 16))
        self.cl_dados_bancarios_entry.set("Banco")
        self.cl_info_textbox = ctk.CTkTextbox(self.tabview.tab("Clientes"), width=620, height=70, border_spacing=10, activate_scrollbars=True, font=("arial", 16))
        self.cl_save_btn = ctk.CTkButton(self.tabview.tab("Clientes"), text="Salvar dados".upper(), font=("arial bold", 14), fg_color="#037", hover_color="#026")       
        
        #POSICIONANDO OS WIDGETS
        self.trm.pack()
        self.nome.place(x=25, y=50)     
        self.cl_nome_entry.place(x=25, y=80)
        self.cpf.place(x=495, y=50)
        self.cl_cpf_entry.place(x=495, y=80)
        self.endereco.place(x=25, y=130)
        self.cl_endereco_entry.place(x=25, y=160) 
        self.cl_seguro_entry.place(x=325, y=160)
        self.cl_dados_bancarios_entry.place(x=495, y=160)
        self.info.place(x=25, y=210)
        self.cl_info_textbox.place(x=25, y=240)
        self.cl_save_btn.place(x=260, y=335)
        
                 
        

if __name__=="__main__":
    app = App()
    app.mainloop()
