import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as messagebox
import os
import time
import shutil
import webbrowser
import sys

def create_repo_path():
    base_path = base_path_entry.get()
    organ = organ_entry.get()
    repo = repo_entry.get()
    if not base_path or not organ or not repo:
        messagebox.showerror("Error", "모든 필드를 입력해주세요.")
        return
    repo_path = os.path.join(base_path, repo)
    if os.path.isdir(repo_path):
        messagebox.showinfo("Info", f"Already exist : {repo_path}")
    else:
        os.chdir(f"D:\\github\\git-fork-sw")
        save_mytoken(mytoken) # github 로그인 토큰을 파일로 저장
        os.system(f"gh auth login --with-token < mytoken.txt") # github 로그인
        os.system(f"gh repo create --internal {organ}/{repo}") # github 저장소 생성
        time.sleep(10)
        os.chdir(f"{base_path}") # clone to 로컬 저장소
        os.system(f"gh repo clone https://github.com/{organ}/{repo}.git {repo_path}")
        os.chdir(f"{repo_path}") # 로컬 저장소 기본 설정
        os.system(f"git lfs install --local")
        DOTFILE_PATH = f"{base_path}\\git-fork-sw\\Dotfiles"
        shutil.copy(f"{DOTFILE_PATH}\\_gitattributes", f"{repo_path}\\.gitattributes")
        shutil.copy(f"{DOTFILE_PATH}\\_gitignore", f"{repo_path}\\.gitignore")
        os.system(f"echo # {repo} > {repo_path}\\README.md")
        os.system(f"mkdir {repo_path}\\3D")
        os.system(f"echo # {repo} > {repo_path}\\3D\\README.md")
        os.system(f"git add --all") # 커밋
        os.system(f"git commit -m 'Init'")
        os.system(f"git push --set-upstream origin HEAD") # 푸쉬
        messagebox.showinfo("Info", f"웹브라우저의 setting 에서, Archives 항목의 Include Git LFS objects in archives 를 체크해 주세요.")
        webbrowser.open(f"https://github.com/{organ}/{repo}/settings") # github 사이트에서 저장소 세부 설정

def get_mytoken():
    os.chdir(f"D:\\github\\git-fork-sw")
    token_file_path = "mytoken.txt"
    mytoken = ""  # 기본값으로 빈 문자열 설정
    if os.path.exists(token_file_path):
        try:
            with open(token_file_path, "r") as f:
                mytoken = f.read().strip()  # 파일 내용을 읽고 앞뒤 공백 제거
        except Exception as e:
            print(f"Error reading token file: {e}")
            mytoken = "" # 오류 발생시 빈 문자열로 설정
    else:
        print(f"mytoken.txt not found. mytoken is set to empty string.")
    return mytoken

def save_mytoken(mytoken):
    os.chdir(f"D:\\github\\git-fork-sw")
    token_file_path = "mytoken.txt"
    try:
        with open(token_file_path, "w") as f:
            f.write(mytoken)
        print(f"Token saved to {token_file_path}")
    except Exception as e:
        print(f"Error saving token to file: {e}")

# Tkinter 윈도우 생성
root = tk.Tk()
root.title("기구팀 새로운 github 저장소 생성기")

# 스타일 설정 (선택 사항)
style = ttk.Style()
style.configure("TLabel", font=("맑은 고딕", 12))
style.configure("TButton", font=("맑은 고딕", 12))
style.configure("TEntry", font=("맑은 고딕", 12))

# 레이블 및 입력 필드 생성
token_label = ttk.Label(root, text="github 로그인 토큰 :")
token_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")
token_label = ttk.Entry(root, width=40)
token_label.grid(row=0, column=1, padx=10, pady=10)
mytoken = get_mytoken()
token_label.insert(1,mytoken)

base_path_label = ttk.Label(root, text="로컬 저장 경로 :")
base_path_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")
base_path_entry = ttk.Entry(root, width=40)
base_path_entry.grid(row=1, column=1, padx=10, pady=10)
base_path_entry.insert(1,"D:\\github")

organ_label = ttk.Label(root, text="기구팀 조직명 :")
organ_label.grid(row=2, column=0, padx=10, pady=10, sticky="e")
organ_entry = ttk.Entry(root, width=40)
organ_entry.grid(row=2, column=1, padx=10, pady=10)
organ_entry.insert(1,"mech-higenmotor")

repo_label = ttk.Label(root, text="생성할 저장소 이름 :")
repo_label.grid(row=3, column=0, padx=10, pady=10, sticky="e")
repo_entry = ttk.Entry(root, width=40)
repo_entry.grid(row=3, column=1, padx=10, pady=10)

# 확인 버튼 생성
check_button = ttk.Button(root, text="저장소 생성하기", command=create_repo_path)
check_button.grid(row=4, column=0, columnspan=1, padx=10, pady=20)

# 확인 버튼 생성
exit_button = ttk.Button(root, text="종료하기", command=sys.exit)
exit_button.grid(row=4, column=1, columnspan=1, padx=10, pady=20)

# 윈도우 실행
root.mainloop()
