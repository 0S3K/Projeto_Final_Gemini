import os
import win32com.client
import google.generativeai as genai
import pyautogui
import pyttsx3
import time
import speech_recognition as sr

def audio_para_texto():
    rec = sr.Recognizer()

    texto = ''
    with sr.Microphone(1) as mic:
        rec.adjust_for_ambient_noise(mic)
        texto_para_audio('Fale o comando')
        audio = rec.listen(mic)
        texto = rec.recognize_google(audio, language='pt-BR')

    return texto

def texto_para_audio(texto):
    speaker = pyttsx3.init()

    voices = speaker.getProperty('voices')
    speaker.setProperty('voice', voices[0].id)
    rate = speaker.getProperty('rate')
    speaker.setProperty('rate', 250)

    speaker.say(texto)
    speaker.runAndWait()

GOOGLE_API_KEY = "AIzaSyAF1esA_hITkZRN7DKI2oNc1bboa9bv2Uc"
genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-pro')

def upload_to_gemini(path, mime_type=None):
    file = genai.upload_file(path, mime_type=mime_type)
    print(f"Uploaded file '{file.display_name}' as: {file.uri}")
    return file

generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}
safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
]

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash-latest",
    safety_settings=safety_settings,
    generation_config=generation_config,
)

def entrada_saida():
    tirar_print_da_tela('teste_gemini.png')  # Capture a screenshot first

    image_drive0 = upload_to_gemini("teste_gemini.png", mime_type="image/png")
    image_drive1 = upload_to_gemini("teste_gemini.png", mime_type="image/png")

    chat_session = model.start_chat(
        history=[
            {
                "role": "user",
                "parts": [
                    "Você deve observar na imagem qual o nome correspondente ao atalho da aplicação desejada\nInput:Abra o Google Chrome\nOutput: Google Chrome\nInput:Abre o Chrome\nOutput:Google Chrome",
                    image_drive0,
                ],
            },
            {
                "role": "model",
                "parts": [
                    "Google Chrome",
                ],
            },
            {
                "role": "user",
                "parts": [
                    "Abra o Edge",
                    image_drive1,
                ],
            },
            {
                "role": "model",
                "parts": [
                    "Microsoft Edge \n",
                ],
            },
        ]
    )
    
    pergunta = audio_para_texto()

    # Verifique se a pergunta não está vazia antes de enviar
    if pergunta:
        resposta = chat_session.send_message(pergunta)
        nome_do_atalho = resposta.text

        pasta_dos_atalhos = r"C:\Users\Public\Desktop"
        nome_do_atalho = nome_do_atalho.strip()
        caminho_do_arquivo = encontrar_atalho_por_nome(pasta_dos_atalhos, str(nome_do_atalho))
        return caminho_do_arquivo
    else:
        print("Pergunta vazia. Não foi possível enviar a mensagem.")
        return None

def obter_caminho_do_arquivo_do_atalho(caminho_do_atalho):
    shell = win32com.client.Dispatch("WScript.Shell")
    atalho = shell.CreateShortcut(caminho_do_atalho)
    return atalho.TargetPath

def encontrar_atalho_por_nome(pasta, nome_do_atalho):
    for arquivo in os.listdir(pasta):
        if arquivo.endswith(".lnk") and nome_do_atalho in arquivo:
            caminho_do_atalho = os.path.join(pasta, arquivo)
            try:
                caminho_do_arquivo = obter_caminho_do_arquivo_do_atalho(caminho_do_atalho)
                return caminho_do_arquivo
            except Exception as e:
                print(f"Erro ao processar o atalho {caminho_do_atalho}: {e}")
    return None

def tirar_print_da_tela(nome_arquivo):
    screenshot = pyautogui.screenshot()
    screenshot.save(nome_arquivo)
    
caminho_do_arquivo = entrada_saida()
if caminho_do_arquivo:
    os.startfile(str(caminho_do_arquivo))
    time.sleep(5)
    tirar_print_da_tela('teste_gemini.png')

    image_drive2 = upload_to_gemini("teste_gemini.png", mime_type="image/png")
