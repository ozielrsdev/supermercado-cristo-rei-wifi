from cx_Freeze import setup, Executable

build_exe_options = {
  "packages": ["pyautogui", "time", "selenium"],
  "include_files": ["qr_codes/"]
}

executables = [
  Executable("main.py", base="Win32GUI")
]


setup(
  name="Wifi Pass Changer",
  version="1.1",
  description="Programa para realizar a troca de senha de Wi-fi",
  options={"build.exe": build_exe_options},
  executables=executables
)
