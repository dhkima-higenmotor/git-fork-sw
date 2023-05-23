import PySimpleGUI as sg
import os
import time
import shutil
import webbrowser

BASE_PATH = "D:\github"
ORGAN = "mech-higenmotor"
repo = sg.popup_get_text('Enter new repository name:', title="New repo")
REPO_PATH = f"{BASE_PATH}\\{repo}"

if os.path.isdir(REPO_PATH):
    sg.popup(f"Alreadyt exist : {REPO_PATH}")
else:
    #print ("New repository : ", f"{BASE_PATH}\\{repo}")
    os.system(f"gh repo create --internal {ORGAN}/{repo}")
    #print((f"gh repo create --internal {ORGAN}/{repo}"))
    time.sleep(10)
    os.chdir(f"{BASE_PATH}")
    os.system(f"gh repo clone https://github.com/{ORGAN}/{repo}.git {REPO_PATH}")
    #os.system(f"git clone https://github.com/{ORGAN}/{repo} {REPO_PATH}")
    #print((f"git clone https://github.com/{ORGAN}/{repo}.git {REPO_PATH}"))
    os.chdir(f"{REPO_PATH}")
    os.system(f"git lfs install --local")
    DOTFILE_PATH = f"{BASE_PATH}\git-fork-sw\Dotfiles"
    shutil.copy(f"{DOTFILE_PATH}\_gitattributes", f"{REPO_PATH}\.gitattributes")
    shutil.copy(f"{DOTFILE_PATH}\_gitignore", f"{REPO_PATH}\.gitignore")
    os.system(f"echo # {repo} > {REPO_PATH}\README.md")
    os.system(f"mkdir {REPO_PATH}\\3D")
    os.system(f"echo # {repo} > {REPO_PATH}\\3D\README.md")
    os.system(f"git add --all")
    os.system(f"git commit -m 'Init'")
    #os.system(f"gh repo sync")
    os.system(f"git push --set-upstream origin HEAD")
    webbrowser.open(f"https://github.com/{ORGAN}/{repo}/settings")
