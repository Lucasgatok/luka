import pywhatkit
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
from tkinter import *
import webbrowser
import os

audio = sr.Recognizer()
maquina = pyttsx3.init()
now = datetime.datetime.now()


def executa_comando():
    try:
        with sr.Microphone(1) as mic:
            audio.adjust_for_ambient_noise(mic)
            ouvindo = 'Ouvindo...'
            print(ouvindo)
            voz = audio.listen(mic)
            comando = audio.recognize_google(voz, language='pt-BR')
            comando = comando.lower()

            if 'luca' in comando:
                comando = comando.replace('luca', '')


    except sr.UnknownValueError:
        erro = 'O Microfone não está ok, tente de novo'
        texto_luka['text'] = erro
        print(erro)

    return comando


def comando_voz_usuario():
    comando = executa_comando()

    if 'horas' in comando:
        hora = datetime.datetime.now().strftime('%H:%M')

        maquina.say('Agora são {} e {} '.format(now.hour, now.minute))

        maquina.runAndWait()
        texto_luka['text'] = hora
    elif 'procure por' in comando:
        procurar = comando.replace('procure por', '')
        wikipedia.set_lang('pt')
        resultado = wikipedia.summary(procurar, 2)
        print(resultado)
        maquina.say(resultado)
        maquina.runAndWait()
        texto_luka['text'] = resultado
    elif 'toque' in comando:
        musica = comando.replace('toque', '')
        res = pywhatkit.playonyt(musica)
        texto_luka['text'] = res
        maquina.say('Tocando música')
        maquina.runAndWait()
    elif 'dia' in comando:
        dia = datetime.datetime.now().strftime('%d')
        mes = datetime.datetime.now().strftime('%m')
        ano = datetime.datetime.now().strftime('%Y')
        texto_luka['text'] = (dia + '/' + mes + '/' + ano)
        maquina.say('hoje é dia:' + dia + 'do mês:' + mes + 'de:' + ano)
        maquina.runAndWait()
    elif 'pesquisar' in comando:
        search = comando.replace('pesquisar', '')
        webbrowser.open(f'https://www.google.com/search?q= {search}')
        maquina.say(f'Pesquisando {search}')
        maquina.runAndWait()
    elif 'youtube' in comando:
        webbrowser.open('https://www.youtube.com/')
        maquina.say('Abrindo o youtube')
        maquina.runAndWait()
    elif 'bloco de notas' in comando:
        os.startfile('notepad.exe')
        maquina.say('Abrindo bloco de notas')
        maquina.runAndWait()
    elif 'lol' in comando:
        os.startfile('C:/Riot Games/Riot Client/RiotClientServices.exe')
        maquina.say('Abrindo o lol')
        maquina.runAndWait()
    elif 'netbeans' in comando:
        os.startfile('C:/Program Files/NetBeans-14/netbeans/bin/netbeans64.exe')
        maquina.say('Abrindo o netbeans')
        maquina.runAndWait()
    elif 'hearthstone' in comando:
        os.startfile('"C:/Program Files (x86)/Hearthstone/Hearthstone Beta Launcher.exe"')
        maquina.say('Abrindo o hearthstone')
        maquina.runAndWait()
    elif 'fifa' in comando:
        webbrowser.open('https://www.ea.com/pt-br/fifa/ultimate-team/web-app/')
        maquina.say('Abrindo o fifa')
        maquina.runAndWait()
    elif 'fechar' in comando:
        janela.destroy()
        maquina.say('até a próxima')
        maquina.runAndWait()


janela = Tk()
janela.title('Luka')
texto_base = Label(janela, text='Sua assistente virtual')
janela.geometry('935x400')

texto_base.grid(column=0, row=0, padx=80, pady=10)

texto_comandos = Label(janela, text='COMANDOS\nDiga: "Horas" para saber as horas\nDiga: "Procure por + o que você '
                                    'deseja" para pesquisar algo na wikipedia\nDiga: "Toque + o Título de um vídeo" '
                                    'para tocar algum vídeo no Youtube\nDiga: "Dia" para saber a data de hoje\n Diga: '
                                    '"Pesquisar + o que você quer pesquisar" para fazer uma pesquisa no Google\npara '
                                    'abrir quaisquer dos aplicativos ou sites abaixo apenas diga o nome EX-(diga: '
                                    '"youtube" para abrir o youtube.)\nDisponíveis:(Youtube, Bloco de notas, Lol, '
                                    'Netbeans, Hearthstone, Fifa)\nPara encerrar o programa diga:"Fechar"\n\nClique '
                                    'no botão abaixo e aguarde 1 (UM) segundo para falar')
texto_comandos.grid(column=0, row=1, padx=80, pady=10)

botao = Button(janela, text='Clique para falar', command=comando_voz_usuario)
botao.grid(column=0, row=2, padx=80, pady=10)

texto_luka = Label(janela, text='')
texto_luka.grid(column=0, row=3, padx=80, pady=10)

janela.mainloop()
