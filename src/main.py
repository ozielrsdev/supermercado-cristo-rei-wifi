import os
import sys
import pyautogui
import random
import time
import pyperclip
from pathlib import Path
from wifi_qrcode_generator import generator
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


user_folder = Path.home()


if getattr(sys, 'frozen', False):
    base_path = os.path.dirname(sys.executable)
else:
    base_path = os.path.dirname(os.path.abspath(__file__))


output_folder = os.path.join(base_path, "qrcodes")
os.makedirs(output_folder, exist_ok=True)

qr_path = os.path.join(output_folder, "wifi_qrcode.jpg")


options = Options()


chrome_profile_path = os.path.join(
    user_folder, "OneDrive", "Documentos", "ChromeProfileSelenium"
)

options.add_argument(fr"user-data-dir={chrome_profile_path}")
options.add_argument("profile-directory=Default")
options.add_experimental_option('useAutomationExtension', False)
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--start-maximized")


firstNum = random.choice('123456789')
randomNum = ''.join(random.choices('0123456789', k=8))
password = firstNum + randomNum
print(f"🔑 Nova senha gerada: {password}")


print("🚀 Iniciando navegador...")
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver=driver, timeout=60)

media = qr_path


def changePassword():
    try:
        print("🔧 Alterando senha do roteador...")
        driver.get("http://192.168.1.1")

        inputLogin = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='pc-login-password']")))
        inputLogin.send_keys("[Senha para entrar nas configs do Roteador]")

        loginButton = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@id='pc-login-btn']")))
        loginButton.click()

        wirelessBtn = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@url='wirelessBasic.htm']")))
        wirelessBtn.click()

        passwordInput2g = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='wpa2PersonalPwd_2g']")))
        passwordInput2g.clear()
        passwordInput2g.send_keys(password)

        passwordInput5g = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='wpa2PersonalPwd_5g']")))
        passwordInput5g.clear()
        passwordInput5g.send_keys(password)

        buttonSave = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@id='save']")))
        buttonSave.click()

        time.sleep(20)
        print("✅ Senha alterada com sucesso!")

    except Exception as e:
        print(f"❌ Erro ao alterar a senha: {e}")


message = (
    "👋 *Bom dia!\n"
    "📶 *Informações da rede Wi-Fi:*\n"
    "🔸 *Senha disponível para:*\n"
    f"➡️ *Rede 2.4 GHz: {password}*\n"
    f"➡️ *Rede 5 GHz: {password}*\n\n"
    "📲 *O QR Code conecta na rede 2.4 GHz.*\n"
    "⚠️ Para a 5 GHz, insira manualmente a senha.\n\n"

    "━━━━━━━━━━━━━━━\n"
    "👨‍💻 *Desenvolvido por @Oziel Sousa*"
)

pyperclip.copy(message)


def sendCode():
    try:
        print("📱 Abrindo WhatsApp Web...")
        driver.get("https://web.whatsapp.com")

        print("🖨️ Gerando QR Code...")
        wifi_qr_code = generator.wifi_qrcode(
            ssid="[Nome da Rede Wifi]",
            hidden=False,
            authentication_type="WPA",
            password=password
        )
        wifi_qr_code.make_image().save(qr_path)

        print("🔍 Buscando contato...")
        contactSearch = wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//p[@class='selectable-text copyable-text x15bjb6t x1n2onr6']")
        ))
        time.sleep(0.3)
        contactSearch.click()
        time.sleep(0.3)
        contactSearch.send_keys("[Nome do Contato]")
        time.sleep(0.3)
        contactSearch.send_keys(Keys.ENTER)
        time.sleep(1)

        print("📎 Anexando imagem...")
        attachButton = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[@data-icon='plus-rounded']")))
        time.sleep(0.3)
        attachButton.click()
        time.sleep(0.3)

        photoAttatch = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Fotos e vídeos']")))
        time.sleep(0.3)
        photoAttatch.click()
        time.sleep(2)

        pyautogui.write(media)
        time.sleep(0.3)
        pyautogui.press("enter")
        time.sleep(3)

        print("💬 Enviando mensagem...")
        messageField = wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//div[@contenteditable='true'][@aria-label='Adicione uma legenda']")
        ))
        time.sleep(0.3)
        messageField.send_keys(Keys.CONTROL, "v")
        time.sleep(0.3)

        sendButton = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[@data-icon='wds-ic-send-filled']")))
        time.sleep(0.3)
        sendButton.click()
        time.sleep(8)

        driver.quit()
        print("✅ QR Code e senha enviados com sucesso!")

    except Exception as e:
        print(f"❌ Não foi possível enviar a mensagem no WhatsApp: {e}")


changePassword()
sendCode()
