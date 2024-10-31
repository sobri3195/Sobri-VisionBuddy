import tkinter as tk
from tkinter import messagebox
import time
import threading
import random

class SobriVisionBuddy:
    def __init__(self, root):
        self.root = root
        self.root.title("Sobri-VisionBuddy")
        self.root.geometry("400x300")
        
        self.screen_time = 0
        self.break_interval = 20 * 60  # Interval istirahat dalam detik (20 menit)
        self.running = True
        self.tips = [
            "Gunakan aturan 20-20-20: setiap 20 menit, lihat sesuatu sejauh 20 kaki selama 20 detik.",
            "Jaga jarak layar minimal 50-60 cm dari mata Anda.",
            "Sesuaikan kecerahan layar agar tidak terlalu terang atau terlalu gelap.",
            "Gunakan layar anti-silau jika sering bekerja di depan komputer.",
            "Pastikan ruang kerja Anda memiliki pencahayaan yang memadai.",
            "Istirahat mata selama 15 menit setelah 2 jam di depan komputer."
        ]

        self.create_widgets()
        self.update_screen_time()

    def create_widgets(self):
        tk.Label(self.root, text="Sobri-VisionBuddy", font=("Helvetica", 16, "bold")).pack(pady=10)
        tk.Label(self.root, text="Screen Time Tracker and Eye Care Reminder", font=("Helvetica", 10)).pack()

        self.screen_time_label = tk.Label(self.root, text="Screen Time: 0 minutes", font=("Helvetica", 12))
        self.screen_time_label.pack(pady=10)

        self.tip_label = tk.Label(self.root, text="Eye Care Tip:", font=("Helvetica", 12))
        self.tip_label.pack(pady=10)

        self.tip_text = tk.Label(self.root, text=random.choice(self.tips), wraplength=350, font=("Helvetica", 10))
        self.tip_text.pack(pady=5)

        tk.Button(self.root, text="Get New Tip", command=self.show_new_tip).pack(pady=10)
        tk.Button(self.root, text="Reset Timer", command=self.reset_screen_time).pack(pady=5)
        tk.Button(self.root, text="Exit", command=self.exit_program).pack(pady=10)

    def update_screen_time(self):
        if self.running:
            self.screen_time += 1
            minutes = self.screen_time // 60
            self.screen_time_label.config(text=f"Screen Time: {minutes} minutes")
            if self.screen_time % self.break_interval == 0:
                self.remind_break()
            self.root.after(1000, self.update_screen_time)

    def remind_break(self):
        messagebox.showinfo("Break Reminder", "It's time to rest your eyes for a few minutes!")

    def show_new_tip(self):
        self.tip_text.config(text=random.choice(self.tips))

    def reset_screen_time(self):
        self.screen_time = 0
        self.screen_time_label.config(text="Screen Time: 0 minutes")

    def exit_program(self):
        self.running = False
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = SobriVisionBuddy(root)
    root.mainloop()
