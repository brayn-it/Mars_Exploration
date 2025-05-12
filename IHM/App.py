import customtkinter as ctk
from IHM.Home_GUI import Home_GUI

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("MARS EXPLORATION")
        self.geometry("1200x800+50x50")
        self.minsize(600,600)
        
        #self.mainloop()
        #self.prev_page = None
        #self.current_page = Home_GUI(self)
        self.pages = {}
        self.add_page("home",Home_GUI(self))

        self.current_page = self.pages["home"]
        #self.show_page(self.current_page)
        self.current_page.pack(expand=True,fill="both")

        self.prev_page = None
        
    def change_page_to(self,page_name):
        """Maj de la page actuelle de la fenetre"""
        for widget in self.winfo_children():
            widget.pack_forget()
            
        self.current_page= self.pages[page_name]
        self.current_page.pack(expand=True,fill="both")

    def add_page(self,page_name,page):
        self.pages[page_name] = page

    def show_page(self,page_name):
        page = self.pages[page_name]
        page.pack(expand=True,fill="both")

    def hide_page(self, page_name):
        self.pages[page_name].pack_forget()


if __name__ == "__main__":
    app = App()
    
    app.mainloop()