import tkinter as tk
from tkinter import ttk, messagebox

class FourFunctionsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Four Functions Processor")
        self.root.geometry("500x400")
        self.root.resizable(False, False)
        
        # Set dark theme colors
        self.bg_color = "#121212"
        self.fg_color = "#00FFFF"  # Cyan text color
        self.entry_bg = "#1E1E1E"
        self.button_bg = "#00BFFF"
        self.button_fg = "#000000"
        self.result_bg = "#1E1E1E"
        
        self.root.configure(bg=self.bg_color)
        
        # Create main frame
        self.main_frame = tk.Frame(root, bg=self.bg_color, padx=20, pady=20)
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title label
        self.title_label = tk.Label(
            self.main_frame, 
            text="Four Functions Processor",
            font=("Arial", 20, "bold"),
            bg=self.bg_color,
            fg=self.fg_color
        )
        self.title_label.pack(pady=(10, 30))
        
        # Input frame
        self.input_frame = tk.Frame(self.main_frame, bg=self.bg_color)
        self.input_frame.pack(fill=tk.X, pady=10)
        
        # Input label
        self.input_label = tk.Label(
            self.input_frame,
            text="Type in a Whole Number",
            font=("Arial", 12),
            bg=self.bg_color,
            fg=self.fg_color
        )
        self.input_label.pack(side=tk.LEFT, padx=(0, 10))
        
        # Input entry
        self.input_var = tk.StringVar()
        self.input_entry = tk.Entry(
            self.input_frame,
            textvariable=self.input_var,
            font=("Arial", 12),
            width=10,
            bg=self.entry_bg,
            fg=self.fg_color,
            insertbackground=self.fg_color  # Cursor color
        )
        self.input_entry.pack(side=tk.LEFT)
        
        # Generate button
        self.generate_button = tk.Button(
            self.main_frame,
            text="Generate",
            font=("Arial", 12, "bold"),
            command=self.generate_results,
            bg=self.button_bg,
            fg=self.button_fg,
            activebackground=self.fg_color,
            activeforeground=self.bg_color,
            padx=20,
            pady=5
        )
        self.generate_button.pack(pady=20)
        
        # Results frame
        self.results_frame = tk.LabelFrame(
            self.main_frame,
            text="RESULTS",
            font=("Arial", 12, "bold"),
            bg=self.bg_color,
            fg=self.fg_color,
            padx=15,
            pady=15
        )
        self.results_frame.pack(fill=tk.BOTH, expand=True)
        
        # Results display
        self.results_grid = tk.Frame(self.results_frame, bg=self.bg_color)
        self.results_grid.pack(fill=tk.BOTH, expand=True)
        
        # Create labels and result entries
        self.create_result_row("Double", 0)
        self.create_result_row("Half", 1)
        self.create_result_row("Square", 2)
        self.create_result_row("Cube", 3)
        
    def create_result_row(self, label_text, row):
        # Label
        label = tk.Label(
            self.results_grid,
            text=label_text,
            font=("Arial", 12),
            bg=self.bg_color,
            fg=self.fg_color,
            anchor="w"
        )
        label.grid(row=row, column=0, sticky="w", padx=(0, 10), pady=5)
        
        # Result entry
        result_var = tk.StringVar()
        setattr(self, f"{label_text.lower()}_var", result_var)
        
        result_entry = tk.Entry(
            self.results_grid,
            textvariable=result_var,
            font=("Arial", 12),
            width=10,
            bg=self.result_bg,
            fg=self.fg_color,
            readonlybackground=self.result_bg,
            state="readonly"
        )
        result_entry.grid(row=row, column=1, sticky="w", pady=5)
    
    def generate_results(self):
        try:
            # Get input value
            input_text = self.input_var.get().strip()
            
            # Validate input
            if not input_text:
                messagebox.showerror("Error", "Please enter a number.")
                return
            
            input_number = int(input_text)
            
            # Validate positive whole number
            if input_number <= 0:
                messagebox.showerror("Error", "Please enter a positive whole number.")
                return
            
            # Calculate results
            double_result = self.double_the_number(input_number)
            half_result = self.half_the_number(input_number)
            square_result = self.square_the_number(input_number)
            cube_result = self.cube_the_number(input_number)
            
            # Update result displays
            self.double_var.set(str(double_result))
            self.half_var.set(str(half_result))
            self.square_var.set(str(square_result))
            self.cube_var.set(str(cube_result))
            
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid whole number.")
    
    # The four functions
    def double_the_number(self, number):
        """Double the input number."""
        return number * 2
    
    def half_the_number(self, number):
        """Half the input number."""
        return number / 2
    
    def square_the_number(self, number):
        """Square the input number."""
        return number ** 2
    
    def cube_the_number(self, number):
        """Cube the input number."""
        return number ** 3

if __name__ == "__main__":
    root = tk.Tk()
    app = FourFunctionsApp(root)
    root.mainloop()
