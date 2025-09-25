import os
import shutil
import subprocess
import sys
import time
import urllib.request
import zipfile

# ANSI colors
RESET = "\033[0m"
BOLD = "\033[1m"

# Standard colors
BLACK = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"

# Bright colors (like your examples)
BRIGHT_BLACK = "\033[90m"
BRIGHT_RED = "\033[91m"
BRIGHT_GREEN = "\033[92m"
BRIGHT_YELLOW = "\033[93m"
BRIGHT_BLUE = "\033[94m"
BRIGHT_MAGENTA = "\033[95m"
BRIGHT_CYAN = "\033[96m"
BRIGHT_WHITE = "\033[97m"

# ANSI background colors
BG_BLACK = "\033[40m"
BG_RED = "\033[41m"
BG_GREEN = "\033[42m"
BG_YELLOW = "\033[43m"
BG_BLUE = "\033[44m"
BG_MAGENTA = "\033[45m"
BG_CYAN = "\033[46m"
BG_WHITE = "\033[47m"


Sub_APP_NAME = "Comprehensive Library of AI"
VERSION_APP = "📦 VERSION APP : 0.1.1 09 2025"
Application_security_APP = "🔒 Application Security : DefenDash DD - (Shahem Algorithms)"

APP_NAME = f"👽 {RED}LMMH{RESET}{BOLD}{BLUE} Library - {Sub_APP_NAME}"


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


folder = ["👽 LMMH"]

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




def print_box(messages=None, progress=0):
    """Full-width modern box with green progress bar."""
    columns, _ = shutil.get_terminal_size()
    box_width = columns - 2
    horizontal = "─" * (box_width - 2)

    clear_screen()


    print(f"╭{horizontal}╮")

    # App Name centered
    name_padding = (box_width - 2 - len(APP_NAME)) // 2
    print(f"│{' ' * name_padding}{BOLD}{CYAN}{APP_NAME}{RESET}{' ' * (box_width + 15 - len(APP_NAME) - name_padding)}│")


    # App VERSION_APP centered
    print(f"├{horizontal}┤")
    version_padding = (box_width - 2 - len(Application_security_APP)) // 2
    print(f"│{' '}{BOLD}{GREEN}{Application_security_APP}{RESET}{' ' * (box_width - 4 - len(Application_security_APP))}│")



    # App VERSION_APP centered
    print(f"├{horizontal}┤")
    version_padding = (box_width - 2 - len(VERSION_APP)) // 2
    print(f"│{' '}{BOLD}{BRIGHT_YELLOW}{VERSION_APP}{RESET}{' ' * (box_width - 4 - len(VERSION_APP))}│")


    print(f"├{horizontal}┤")

    # Messages
    if messages:
        start = 0 
        for msg in messages:
            if(start == 0):
                start = 1
                msg_padding = (box_width - 2 - len(msg)) // 2
                print(f"│{' ' * msg_padding}{msg}{' ' * (box_width - 4 - len(msg) - msg_padding)}│")
            else:
                print(f"│{' '}{msg}{' ' * (box_width - 2 - len(msg))}│")
    else:
        print(f"│{' ' * (box_width - 2)}│")

    

    if(progress != 0) :
        print(f"├{horizontal}┤")
        bar_length = box_width - 4
        filled_length = int(bar_length * progress)
        empty_length = bar_length - filled_length
        bar = f"{GREEN}{'█' * filled_length}{RESET}{WHITE}{'█' * empty_length}{RESET}"
        print(f"│ {bar} │")



    print(f"╰{horizontal}╯")


def download_file(url, dest):
    """Download file from URL to destination."""
    folder = os.path.dirname(dest)
    if folder and not os.path.exists(folder):
        os.makedirs(folder, exist_ok=True)
    urllib.request.urlretrieve(url, dest)


def create_folders(folders):
    """Create required folders with progress display."""
    total = len(folders)
    for i, folder in enumerate(folders):
        os.makedirs(folder, exist_ok=True)
        progress = (i + 1) / total
        print_box([f"📁 Creating folder: {folder}"], progress)
        time.sleep(0.5)

def create_files(files):
    # Step 2: Create files
    for i, (filepath, content) in enumerate(files.items()):
        folder = os.path.dirname(filepath)
        if folder and not os.path.exists(folder):
            os.makedirs(folder, exist_ok=True)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print_box([f"📝 Creating file: {filepath}"], (i+1)/len(files))
        time.sleep(0.5)



# Files to download (URL -> local path)
downloads = {
    f"https://github.com/LaithALhaware/LMMH/blob/main/README.md": f"{folder[0]}/README.md",
    f"https://github.com/LaithALhaware/LMMH/blob/main/LICENSE": f"{folder[0]}/LICENSE",
    f"https://github.com/LaithALhaware/LMMH/blob/main/requirements.txt": f"{folder[0]}/requirements.txt"
}
def Download_files_internet(downloads):
    # Step 3: Download files
    for i, (url, dest) in enumerate(downloads.items()):
        print_box([f"🌐 Downloading: {os.path.basename(dest)}"], (i+1)/len(downloads))
        download_file(url, dest)
        time.sleep(0.5)



def download_repo_files(REPO_URL, target_folder):
    """Download GitHub repo as ZIP and move all files to the target folder."""

    zip_url = REPO_URL.replace(".git", "/archive/refs/heads/main.zip")
    zip_path = "repo.zip"

    # Ensure target folder exists
    os.makedirs(target_folder, exist_ok=True)

    # Download ZIP
    urllib.request.urlretrieve(zip_url, zip_path)

    # Extract to temp folder
    temp_folder = "temp_repo"
    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(temp_folder)
    os.remove(zip_path)

    # Move all files from extracted folder to target_folder
    extracted_folder = os.path.join(temp_folder, os.listdir(temp_folder)[0])
    for item in os.listdir(extracted_folder):
        src_path = os.path.join(extracted_folder, item)
        dest_path = os.path.join(target_folder, item)
        if os.path.exists(dest_path):
            if os.path.isdir(dest_path):
                shutil.rmtree(dest_path)
            else:
                os.remove(dest_path)
        shutil.move(src_path, dest_path)

    # Remove temp folder
    shutil.rmtree(temp_folder)



def main():
    clear_screen()

    print_box([
        f"🎉 Welcome to {folder[0]} - {Sub_APP_NAME}",
    ])
    time.sleep(2)

    create_folders(folder);

    download_repo_files("https://github.com/LaithALhaware/LMMH.git", folder[0]);

    # Step 4: Create virtual environment
    venv_path = f"{folder[0]}/LMMH_env"
    if not os.path.exists(venv_path):
        print_box(["🐍 Creating Virtual Environment LMMH_env 🐍"], 0)
        subprocess.run([sys.executable, "-m", "venv", venv_path])
        time.sleep(0.5)
    else:
        print_box(["🐍 Virtual Environment Already Exists (LMMH_env) 🐍"], 1)
        time.sleep(0.5)

    # Determine python executable inside venv
    python_exec = os.path.join(venv_path, "bin", "python") if os.name != "nt" else os.path.join(venv_path, "Scripts", "python.exe")

    # Step 5: Install requirements
    total_steps = 5
    for i in range(total_steps):
        progress = (i + 1) / total_steps
        print_box(["📦 Installing Python Requirements 📦"], progress)
        if i == 0:
            subprocess.run([python_exec, "-m", "pip", "install", "--upgrade", "pip"])
            subprocess.run([python_exec, "-m", "pip", "install", "-r", "requirements.txt"])
        time.sleep(0.2)

        



    Projects = [
    ["🗨️  AI Chatbot (Language Models)", [
        "💬 Intent Recognition",
        "🧠 Dialogue Management",
        "✍️ Response Generation",
        "😊 Sentiment Analysis",
        "📚 Knowledge Base Integration",
        "🌐 Multi-language Support",
        "🎙️ Voice Integration",
        "🧪 Testing & Evaluation",
        "💻 Code Agent",
        "📧 Write Email Assistant",
        "📂 File Analysis",
        "❓ Ask About Your Uploaded File"
    ]],
    ["👁️  Vision AI Processing", [
        "🖼️  Image Classification",
        "🔍 Object Detection",
        "😃 Face Recognition",
        "📝 OCR Processing",
        "🎥 Video Analysis",
        "🎨 GAN Image Generation",
        "🧩 Image Segmentation",
        "🚗 Plate Number Detection",
        "🧍 Human Detection",
        "🚘 Car Detection",
        "🏷️ Car Brand Detection",
        "🔖 Car Sub-brand Detection",
        "❓ Ask Any Question About Any Image"
    ]]
    ]

    # Format nodes with index
    root_nodes_with_index = [f"{i}: {node[0]}" for i, node in enumerate(Projects)]

    # Print inside your box
    print_box(["📦 Select Type of Project : 📦"] + root_nodes_with_index)


    while True:
        try:
            Type_of_Project = int(input("📊 Enter the Number of Projects You Want to Add: "))
            if Type_of_Project < 0:
                print("⚠️  Number Cannot be Negative. Try Again.")
            else:
                break  # valid input, exit loop
        except ValueError:
            print("❌  Invalid Input. Please Enter a Number.")

    
    
    
    # Format nodes with index
    root_nodes_with_Project = [f"{i}: {child}" for i, child in enumerate(Projects[Type_of_Project][1])]
    print_box([f"{Projects[Type_of_Project][0]} |  📦 Select Project : "] + root_nodes_with_Project)


    while True:
        try:
            Select_Project = int(input("📊 Enter the Number of Projects You Want to Add: "))
            if Select_Project < 0:
                print("⚠️  Number Cannot be Negative. Try Again.")
            else:
                break  # valid input, exit loop
        except ValueError:
            print("❌  Invalid Input. Please Enter a Number.")





    time.sleep(5)

    print_box([f" 🎉 Project Setup Complete 🎉 "])
    print("\n")


if __name__ == "__main__":
    main()
