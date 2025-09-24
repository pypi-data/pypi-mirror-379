# app.py
import os
import shutil
import subprocess
import sys
import time

# ANSI colors
RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
WHITE = "\033[97m"



Sub_APP_NAME = "Text Model Training"
VERSION_APP = "VERSION APP : 1.0.01 09 2025"

APP_NAME = f"👽 LMMH Library - {Sub_APP_NAME}"

folders = ["tokenizer", "training", "generation"]

files = {
    "requirements.txt": """torch
transformers
sentencepiece
datasets
accelerate
deepspeed
""",
    "tokenizer/train_tokenizer.py": "# Tokenizer training script placeholder\n",
    "training/train_gpt.py": "# GPT training script placeholder\n",
    "generation/generate_text.py": "# Text generation script placeholder\n"
}

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_box(messages=None, progress=0, step_name="", status_msg=""):
    """Full-width modern box with green progress bar."""
    columns, _ = shutil.get_terminal_size()
    box_width = columns - 2
    horizontal = "─" * (box_width - 2)

    clear_screen()
    # Top border
    print(f"╭{horizontal}╮")

    # App Name centered
    name_padding = (box_width - 2 - len(APP_NAME)) // 2
    print(f"│{' ' * name_padding}{BOLD}{CYAN}{APP_NAME}{RESET}{' ' * (box_width - 3 - len(APP_NAME) - name_padding)}│")
    
    # App VERSION_APP centered
    VERSION_APP_padding = (box_width - 2 - len(VERSION_APP)) // 2
    print(f"│{' ' * VERSION_APP_padding}{BOLD}{CYAN}{VERSION_APP}{RESET}{' ' * (box_width - 2 - len(VERSION_APP) - VERSION_APP_padding)}│")


    # Divider
    print(f"├{horizontal}┤")

    # Messages
    if messages:
        for msg in messages:
            msg_padding = (box_width - 2 - len(msg)) // 2
            print(f"│{' ' * msg_padding}{msg}{' ' * (box_width - 4 - len(msg) - msg_padding)}│")
    else:
        print(f"│{' ' * (box_width - 2)}│")

    # Divider
    print(f"├{horizontal}┤")

    # Step name + percentage above progress bar
    step_info = f"{int(progress*100)}% - {step_name}" if step_name else ""
    if step_info:
        step_padding = (box_width - 2 - len(step_info)) // 2
        print(f"│{' ' * step_padding}{BOLD}{YELLOW}{step_info}{RESET}{' ' * (box_width - 2 - len(step_info) - step_padding)}│")

    # Progress bar (green, no text)
    bar_length = box_width - 4
    filled_length = int(bar_length * progress)
    empty_length = bar_length - filled_length
    bar = f"{GREEN}{'█' * filled_length}{RESET}{WHITE}{'█' * empty_length}{RESET}"

    print(f"│ {bar} │")  # small side padding

    # Status message
    if status_msg:
        if len(status_msg) > box_width - 2:
            status_msg = status_msg[:box_width-2]
        padding = (box_width - 2 - len(status_msg)) // 2
        print(f"│{' ' * padding}{BOLD}{YELLOW}{status_msg}{RESET}{' ' * (box_width - 3 - len(status_msg) - padding)}│")
    else:
        print(f"│{' ' * (box_width - 2)}│")

    # Bottom border
    print(f"╰{horizontal}╯")

def show_welcome():
    messages = [
        f"🎉 Welcome to 👽 LMMH - {Sub_APP_NAME}",
        "🌟 Setting up your project in a modern terminal dashboard 🌟"
    ]
    print_box(messages)
    time.sleep(3)

def step_progress(total, step_name, action_func, status_func):
    for i in range(total):
        progress = (i + 1) / total
        status_msg = status_func(i)
        print_box([], progress, step_name, status_msg)
        action_func(i)
        time.sleep(0.15)

def main():
    clear_screen()
    show_welcome()

    # Step 1: Create folders
    def folder_action(i):
        folder = folders[i]
        os.makedirs(folder, exist_ok=True)
    def folder_status(i):
        return f"📁 Creating folder: {folders[i]}"
    step_progress(len(folders), "Folders", folder_action, folder_status)

    # Step 2: Create files
    def file_action(i):
        filepath, content = list(files.items())[i]
        folder = os.path.dirname(filepath)
        if folder and not os.path.exists(folder):
            os.makedirs(folder, exist_ok=True)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
    def file_status(i):
        return f"📝 Creating file: {list(files.keys())[i]}"
    step_progress(len(files), "Files", file_action, file_status)

    # Step 3: Create virtual environment (blocking)
    venv_path = "TXTAI"
    if not os.path.exists(venv_path):
        print_box([], 0, "Virtual Env", "🐍 Creating virtual environment TXTAI")
        subprocess.run([sys.executable, "-m", "venv", venv_path])
        time.sleep(0.5)
    else:
        print_box([], 1, "Virtual Env", "🐍 Virtual environment already exists")
        time.sleep(0.5)

    # Determine python executable inside venv
    python_exec = os.path.join(venv_path, "bin", "python") if os.name != "nt" else os.path.join(venv_path, "Scripts", "python.exe")

    # Step 4: Install requirements (run once, animate progress)
    total_steps = 5
    for i in range(total_steps):
        progress = (i + 1) / total_steps
        status_msg = "📦 Installing Python requirements..."
        print_box([], progress, "Install", status_msg)
        if i == 0:
            subprocess.run([python_exec, "-m", "pip", "install", "--upgrade", "pip"])
            subprocess.run([python_exec, "-m", "pip", "install", "-r", "requirements.txt"])
        time.sleep(0.2)

    print_box(["✅ Project setup complete! 🎉"])
    print("\n")

if __name__ == "__main__":
    main()


