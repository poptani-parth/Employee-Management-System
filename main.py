import tkinter as tk
from tkinter import messagebox

class ManagerLoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Shree Ganesh Diamond | Manager Access")
        self.root.geometry("400x550")
        self.root.resizable(False, False)
        
        # --- Modern Color Palette ---
        self.bg_color = "#F3F4F6"       # Light Gray (Background)
        self.card_bg = "#FFFFFF"        # White (Card)
        self.primary_color = "#2563EB"  # Modern Blue
        self.text_header = "#1F2937"    # Dark Charcoal
        self.text_label = "#4B5563"     # Medium Gray
        self.entry_bg = "#F9FAFB"       # Very Light Gray for inputs
        self.border_color = "#D1D5DB"   # Light border

        self.root.configure(bg=self.bg_color)

        self.create_widgets()

    def create_widgets(self):
        # =========================
        # CENTERED CARD FRAME
        # =========================
        # We use place() to center this frame perfectly in the window
        self.card_frame = tk.Frame(
            self.root, 
            bg=self.card_bg, 
            bd=1, 
            relief=tk.SOLID
        )
        self.card_frame.place(relx=0.5, rely=0.5, anchor="center", width=340, height=450)
        # Adding a border color workaround (Frame inside a Frame usually, but using bd=1 relief=SOLID is simple)
        self.card_frame.configure(highlightbackground=self.border_color, highlightthickness=1)

        # =========================
        # HEADER SECTION
        # =========================
        header_frame = tk.Frame(self.card_frame, bg=self.card_bg)
        header_frame.pack(fill="x", pady=(30, 20), padx=20)

        title_label = tk.Label(
            header_frame,
            text="MANAGER LOGIN",
            font=("Segoe UI", 16, "bold"),
            bg=self.card_bg,
            fg=self.text_header
        )
        title_label.pack()

        subtitle_label = tk.Label(
            header_frame,
            text="Shree Ganesh Diamond",
            font=("Segoe UI", 10),
            bg=self.card_bg,
            fg=self.primary_color
        )
        subtitle_label.pack(pady=(5, 0))

        # =========================
        # INPUT SECTION
        # =========================
        input_frame = tk.Frame(self.card_frame, bg=self.card_bg)
        input_frame.pack(fill="x", padx=30)

        # --- 1. Manager Name ---
        tk.Label(
            input_frame, 
            text="USERNAME", 
            font=("Segoe UI", 9, "bold"),
            bg=self.card_bg,
            fg=self.text_label
        ).pack(anchor="w", pady=(0, 5))

        self.manager_name_entry = tk.Entry(
            input_frame, 
            font=("Segoe UI", 11),
            bg=self.entry_bg,
            bd=1,
            relief=tk.SOLID,
            highlightthickness=1,
            highlightcolor=self.primary_color,
            highlightbackground=self.border_color
        )
        self.manager_name_entry.pack(fill="x", ipady=5, pady=(0, 20))
        self.manager_name_entry.focus()

        # --- 2. Password (4 Boxes) ---
        tk.Label(
            input_frame, 
            text="PASSWORD PIN", 
            font=("Segoe UI", 9, "bold"),
            bg=self.card_bg,
            fg=self.text_label
        ).pack(anchor="w", pady=(0, 5))

        # Container for the 4 boxes
        self.pass_frame = tk.Frame(input_frame, bg=self.card_bg)
        self.pass_frame.pack(fill="x", pady=(0, 10))

        self.pass_entries = []
        self.pass_vars = []

        # Create 4 evenly spaced boxes
        for i in range(4):
            var = tk.StringVar()
            entry = tk.Entry(
                self.pass_frame, 
                width=4, 
                font=("Segoe UI", 14, "bold"), 
                justify="center",
                textvariable=var,
                bg=self.entry_bg,
                bd=1,
                relief=tk.SOLID,
                show="●", # Modern dot character
                highlightthickness=1,
                highlightcolor=self.primary_color,
                highlightbackground=self.border_color
            )
            # Pack with spacing
            entry.pack(side=tk.LEFT, padx=(0, 10) if i < 3 else 0, ipady=5)
            
            # Events
            var.trace("w", lambda name, index, mode, i=i: self.on_digit_entry(i))
            entry.bind("<BackSpace>", lambda event, i=i: self.on_backspace(event, i))
            entry.bind("<FocusIn>", lambda event, e=entry: e.configure(bg="#EBF5FF")) # Highlight on focus
            entry.bind("<FocusOut>", lambda event, e=entry: e.configure(bg=self.entry_bg))

            self.pass_entries.append(entry)
            self.pass_vars.append(var)

        # =========================
        # BUTTON SECTION
        # =========================
        # Login Button
        self.login_btn = tk.Button(
            self.card_frame,
            text="LOGIN",
            bg=self.primary_color,
            fg="white",
            font=("Segoe UI", 11, "bold"),
            activebackground="#1d4ed8",
            activeforeground="white",
            cursor="hand2",
            relief=tk.FLAT,
            command=self.manager_login
        )
        self.login_btn.pack(fill="x", padx=30, pady=30, ipady=5)

        # Bind 'Enter' key to login globally
        self.root.bind('<Return>', lambda event: self.manager_login())

    def on_digit_entry(self, i):
        """Handle typing in a password box: enforce digit & jump next"""
        text = self.pass_vars[i].get()
        if len(text) > 0:
            if not text.isdigit():
                self.pass_vars[i].set("") 
                return
            
            if len(text) > 1:
                self.pass_vars[i].set(text[-1])

            if i < 3:
                self.pass_entries[i+1].focus()
            else:
                # If last digit entered, set focus to login button or hide keyboard
                self.root.focus()

    def on_backspace(self, event, i):
        """Handle backspace: jump to previous box if empty"""
        if len(self.pass_vars[i].get()) == 0 and i > 0:
            self.pass_entries[i-1].focus()

    def manager_login(self):
        """Validates input and checks credentials"""
        name = self.manager_name_entry.get().strip()
        password = "".join([var.get() for var in self.pass_vars])

        # -----------------------------
        # 1. VALIDATION
        # -----------------------------
        if not name or len(password) < 4:
            messagebox.showwarning("Incomplete", "Please enter your Username and 4-digit PIN.")
            return

        # -----------------------------
        # 2. DATABASE LOGIC (COMMENTED)
        # -----------------------------
        # Connect to DB, hash password check, etc.
        # cursor.execute("SELECT * FROM managers WHERE name=? AND pin=?", (name, password))
        
        # MOCK LOGIN
        if name == "admin" and password == "1234":
            messagebox.showinfo("Success", f"Welcome, {name}!")
        else:
            messagebox.showerror("Failed", "Invalid Credentials.")
            # Clear password fields on failure
            for var in self.pass_vars:
                var.set("")
            self.pass_entries[0].focus()

if __name__ == "__main__":
    root = tk.Tk()
    app = ManagerLoginApp(root)
    root.mainloop()