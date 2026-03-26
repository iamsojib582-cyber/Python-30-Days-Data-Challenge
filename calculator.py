
import tkinter as tk

class Calculator:
    def __init__(self, window):
        self.window = window
        self.window.title("Calculator")
        self.window.geometry("300x400")
        self.bg_color = "#2d2d2d"           
        self.display_bg = "#ffffff"         
        self.display_fg = "#000000"         
        self.button_bg = "#4d4d4d"          
        self.button_fg = "#ffffff"          
        self.operator_bg = "#ff9800"        
        self.operator_fg = "#ffffff"        
        self.equals_bg = "#4caf50"          
        self.equals_fg = "#ffffff"          
        self.clear_bg = "#f44336"           
        self.clear_fg = "#ffffff"   

        self.display_font = ("Arial", 20, "bold")      
        self.button_font = ("Arial", 14, "bold")   
        
        self.expression = ""
        self.window.configure(bg=self.bg_color)
        self.display = tk.Entry(
            self.window,
            font=self.display_font,
            justify="right",
            insertwidth=2,
            bg=self.display_bg,
            fg=self.display_fg,
            bd=5
        )
        
        
        self.display.pack(fill=tk.BOTH, padx=10, pady=10, ipady=10)
        self.display.insert(0, "0")
        
        self.create_buttons()
    def create_buttons(self):
        """Create all calculator buttons"""
        buttons_layout = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["0", ".", "=", "+"],
            ["C", "Delete", "√", "%"]
        ]
        
        buttons_frame = tk.Frame(self.window, bg=self.bg_color)
        buttons_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        for row in buttons_layout:
            row_frame = tk.Frame(buttons_frame, bg=self.bg_color)
            row_frame.pack(fill=tk.BOTH, expand=True)
            
            for button_text in row:
                
                if button_text == "=":
                    bg_color = self.equals_bg
                    fg_color = self.equals_fg
                elif button_text == "C":
                    bg_color = self.clear_bg
                    fg_color = self.clear_fg
                elif button_text in ["/", "*", "-", "+"]:
                    bg_color = self.operator_bg
                    fg_color = self.operator_fg
                else:
                    bg_color = self.button_bg
                    fg_color = self.button_fg
                btn = tk.Button(
                    row_frame,
                    text=button_text,
                    font=self.button_font,
                    bg=bg_color,
                    fg=fg_color,
                    bd=2,
                    command=lambda x=button_text: self.on_button_click(x)
                )
                btn.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=2, pady=2)
    
    def on_button_click(self, button_text):
        """Handle button click events"""
        
        current_display = self.display.get()
        
        if button_text == "C":
            self.display.delete(0, tk.END)
            self.display.insert(0, "0")
            self.expression = ""
            return
        
        if button_text == "Delete":
            if len(current_display) > 1:
                new_display = current_display[:-1]
                self.display.delete(0, tk.END)
                self.display.insert(0, new_display)
            else:
                self.display.delete(0, tk.END)
                self.display.insert(0, "0")
            return
        
        if button_text == "√":
            try:
                import math
                result = math.sqrt(float(current_display))
                self.display.delete(0, tk.END)
                self.display.insert(0, str(result))
                self.expression = str(result)
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
            return
        if button_text == "%":
            try:
                result = float(current_display) / 100
                self.display.delete(0, tk.END)
                self.display.insert(0, str(result))
                self.expression = str(result)
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
            return
        
        if button_text in ["+", "-", "*", "/"]:
            if current_display != "0":
                self.expression += current_display + button_text
                self.display.delete(0, tk.END)
                self.display.insert(0, "0")
            return
        if button_text == "=":
            try:
                self.expression += current_display
                result = eval(self.expression)
                self.display.delete(0, tk.END)
                self.display.insert(0, str(result))
                self.expression = str(result)
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
                self.expression = ""
            return
        
        if button_text == ".":
            if "." not in current_display:
                if current_display == "0":
                    self.display.delete(0, tk.END)
                    self.display.insert(0, "0.")
                else:
                    self.display.insert(tk.END, ".")
            return
    
        if button_text.isdigit():
            if current_display == "0":
                self.display.delete(0, tk.END)
                self.display.insert(0, button_text)
            else:
                self.display.insert(tk.END, button_text)


if __name__ == "__main__":
    root = tk.Tk()
    app =Calculator(root)
    root.mainloop()
                

            
