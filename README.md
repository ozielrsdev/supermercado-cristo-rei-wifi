# 🔐 Automação de troca de senha - Supermercado Cristo Rei

## 📌 Descrição
Projeto desenvolvido em **Python** para automatizar a troca diária da senha do Wi-Fi do **Supermercado Cristo Rei**.  
Além de atualizar a senha, o sistema:
- Gera automaticamente uma **senha aleatória sem padrões**.
- Cria um **QR Code** para facilitar a conexão.
- Envia a senha e o QR Code no **grupo do WhatsApp da empresa**.
- Garante maior segurança da rede, evitando acessos indevidos.

---

## ⚙️ Funcionalidades
- Login automático no roteador via **Selenium**.
- Alteração da senha em redes **2.4 GHz e 5 GHz**.
- Geração de senha aleatória sem padrões previsíveis.
- Criação de **QR Code** da rede.
- Envio automático da nova senha e QR Code no **WhatsApp Web**.
- Empacotamento do programa com **cx_Freeze** para distribuição.
  ![Image](https://github.com/user-attachments/assets/7bc71244-3664-4aae-9fbb-c02886b0bf3e)
  

---

## 🚀 Como executar

### 1. Instale as dependências
```bash
pip install selenium pyautogui pyperclip wifi-qrcode-generator cx_Freeze
```

> Também é necessário ter o **Google Chrome** e o **ChromeDriver** compatível com sua versão.

---

### 2. Configure o script
- Ajuste no código:
  - `[Senha para entrar nas configs do Roteador]`
  - `[Nome da Rede Wifi]`
  - `[Nome do Contato]` (grupo ou contato no WhatsApp)

---

### 3. Execute o script
```bash
python main.py
```

O programa:
1. Gera uma nova senha aleatória.  
2. Faz login no roteador e altera a senha.  
3. Cria um QR Code da rede.  
4. Envia a senha e o QR Code no WhatsApp.  

---

## 📦 Compilação
Para gerar o executável:

```bash
python setup.py build
```

Após a compilação, os arquivos estarão disponíveis na pasta:

```
build/
```

---

## 🖼️ Evidências
- **QR Code gerado** em `qrcodes/wifi_qrcode.jpg`
- **Mensagem automática no WhatsApp** com a senha e QR Code.

---

## 👨‍💻 Autor
Desenvolvido por **Oziel Sousa**
