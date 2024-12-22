import os
import subprocess
import tkinter as tk
from tkinter import messagebox, filedialog, ttk
import threading
import re


# ---------- RoundedButton Class ----------
class RoundedButton(tk.Canvas):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, width=kwargs.get('width', 150), height=kwargs.get('height', 40), 
                         bg=parent['bg'], highlightthickness=0)
        
        self.radius = kwargs.get('radius', 10)
        self.color = kwargs.get('color', '#0abde3')
        self.active_color = kwargs.get('active_color', '#0984e3')
        self.command = kwargs.get('command', lambda: None)
        self.text = kwargs.get('text', 'Button')
        self.font = kwargs.get('font', ("Segoe UI", 12, "bold"))
        
        self.bind("<Button-1>", self.on_click)
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)
        
        self.draw()
        
    def draw(self):
        """Draws the rounded button."""
        self.delete("all")
        self.create_oval(0, 0, self.radius * 2, self.radius * 2, fill=self.color, outline="")
        self.create_oval(self.winfo_reqwidth() - self.radius * 2, 0, self.winfo_reqwidth(), self.radius * 2, fill=self.color, outline="")
        self.create_oval(0, self.winfo_reqheight() - self.radius * 2, self.radius * 2, self.winfo_reqheight(), fill=self.color, outline="")
        self.create_oval(self.winfo_reqwidth() - self.radius * 2, self.winfo_reqheight() - self.radius * 2, self.winfo_reqwidth(), self.winfo_reqheight(), fill=self.color, outline="")
        self.create_rectangle(self.radius, 0, self.winfo_reqwidth() - self.radius, self.winfo_reqheight(), fill=self.color, outline="")
        self.create_rectangle(0, self.radius, self.winfo_reqwidth(), self.winfo_reqheight() - self.radius, fill=self.color, outline="")
        
        # Place text in the center
        self.create_text(self.winfo_reqwidth() / 2, self.winfo_reqheight() / 2, 
                         text=self.text, font=self.font, fill='white')
    
    def on_click(self, event):
        """Executes the assigned command."""
        if self.command:
            self.command()
    
    def on_enter(self, event):
        """Changes button color on hover."""
        self.color = self.active_color
        self.draw()
    
    def on_leave(self, event):
        """Restores default button color."""
        self.color = '#0abde3'
        self.draw()


# ---------- Main Application Class ----------
class YouTubeConverter:
    def __init__(self):
        self.YTDLP_PATH = os.path.join(os.path.dirname(__file__), "yt-dlp.exe")
        self.FFMPEG_PATH = os.path.join(os.path.dirname(__file__), "ffmpeg.exe")
        self.setup_ui()

    def setup_ui(self):
        self.root = tk.Tk()
        self.root.title("🎵 YouTube Audio Downloader")
        self.root.geometry("800x600")
        self.root.minsize(600, 500)  # Mindestgröße festlegen
        self.root.state('normal')
        self.root.configure(bg='#1e272e')
        
        # Bind resize event
        self.root.bind("<Configure>", self.on_resize)

        # Header
        self.header_frame = tk.Frame(self.root, bg='#0abde3')
        self.header_frame.pack(fill='x')
        self.header_label = tk.Label(self.header_frame, text="🎵 YouTube Audio Downloader", 
                                     font=("Segoe UI", 20, "bold"), bg='#0abde3', fg='white')
        self.header_label.pack(pady=10)

        # URL Input
        self.url_frame = tk.Frame(self.root, bg='#1e272e')
        self.url_frame.pack(fill='x', pady=10, padx=20)
        self.url_label = tk.Label(self.url_frame, text="🔗 Enter YouTube URL:", 
                                  font=("Segoe UI", 12), bg='#1e272e', fg='white')
        self.url_label.pack(anchor='w')

        self.url_var = tk.StringVar()
        self.url_entry = tk.Entry(self.url_frame, textvariable=self.url_var,
                                  font=("Segoe UI", 12), bg='#ffffff', relief='solid', bd=1)
        self.url_entry.pack(fill='x', pady=5, ipady=5)

        # Audio Quality
        self.options_frame = tk.Frame(self.root, bg='#1e272e')
        self.options_frame.pack(fill='x', pady=10, padx=20)
        self.quality_label = tk.Label(self.options_frame, text="🎧 Select Audio Quality:", 
                                      font=("Segoe UI", 12), bg='#1e272e', fg='white')
        self.quality_label.pack(anchor='w')

        self.quality_var = tk.StringVar(value="320")
        for text, value in [("320 kbps", "320"), ("192 kbps", "192"), ("128 kbps", "128")]:
            tk.Radiobutton(self.options_frame, text=text, variable=self.quality_var, value=value,
                           font=("Segoe UI", 10), bg='#1e272e', fg='white').pack(side='left', padx=10)

        # Progress Bar
        self.progress_frame = tk.Frame(self.root, bg='#1e272e')
        self.progress_frame.pack(fill='x', pady=10, padx=20)
        self.progress_label = tk.Label(self.progress_frame, text="📊 Download Progress:", 
                                       font=("Segoe UI", 12), bg='#1e272e', fg='white')
        self.progress_label.pack(anchor='w')
        
        self.progress_var = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(self.progress_frame, orient="horizontal",
                                            mode="determinate", variable=self.progress_var)
        self.progress_bar.pack(fill='x', pady=10)

        self.status_var = tk.StringVar(value="Ready")
        self.status_label = tk.Label(self.progress_frame, textvariable=self.status_var,
                                     font=("Segoe UI", 10), bg='#1e272e', fg='white')
        self.status_label.pack(pady=5)

        # Download Button
        self.button_frame = tk.Frame(self.root, bg='#1e272e')
        self.button_frame.pack(pady=10, fill='x')
        self.download_btn = RoundedButton(self.button_frame, text="🎧 Start Download",
                                          command=self.start_download, font=("Segoe UI", 12, "bold"),
                                          color='#0abde3', active_color='#0984e3', width=200, height=50)
        self.download_btn.pack(anchor='center', pady=10)

    def on_resize(self, event):
        """Adjusts UI on window resize."""
        new_width = event.width
        self.progress_bar.config(length=new_width - 60)
        self.url_entry.config(width=new_width // 10)

    def start_download(self):
        url = self.url_var.get().strip()
        quality = self.quality_var.get()
        
        if not url:
            messagebox.showwarning("Warning", "Please enter a YouTube URL!")
            return
        
        save_path = filedialog.askdirectory(title="Choose Save Location")
        if not save_path:
            return
        
        self.status_var.set("Downloading...")
        threading.Thread(target=self.download_audio, args=(url, save_path, quality), daemon=True).start()

    def download_audio(self, url, save_path, quality):
        command = [
            self.YTDLP_PATH, "-x", "--audio-format", "mp3",
            "--audio-quality", quality, "-o", os.path.join(save_path, "%(title)s.%(ext)s"), url
        ]
        subprocess.run(command, check=True)
        self.status_var.set("✅ Download Completed!")
        messagebox.showinfo("Success", "✅ Audio downloaded successfully!")

    def run(self):
        self.root.mainloop()


# ---------- Start Application ----------
if __name__ == "__main__":
    app = YouTubeConverter()
    app.run()
