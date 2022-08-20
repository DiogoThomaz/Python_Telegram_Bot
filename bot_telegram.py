from turtle import update
import telebot
import requests
import time
import json
import os
import config_bot

class TelegramBot:
    def __init__(self):
        config_bot.CHAVE_API
        self.url_base = f'https://api.telegram.org/bot{config_bot.CHAVE_API}/'
    #INCIAR BOT
    def Iniciar(self):
        update_id = None
        while True:
            atualizacao = self.obter_mensagens(update_id)
            mensagens = atualizacao['result']
            if mensagens:
                for mensagem in mensagens:
                    update_id = mensagem['update_id']
                    chat_id = mensagem['message']['from']['id']
                    eh_primeira_mensagem = mensagem['message']['message_id'] == 1
                    resposta = self.criar_resposta(mensagem, eh_primeira_mensagem)
                    self.responder(resposta,chat_id)
    #OBTER MENSAGEM
    def obter_mensagens(self, update_id):
        link_requisicao = f'{self.url_base}getUpdates?timeout=100'
        if update_id:
            link_requisicao = f'{link_requisicao}&offset={update_id + 1}'
        resultado = requests.get(link_requisicao)
        return json.loads(resultado.content)
    #CRIAR RESPOSTA
    def criar_resposta(self, mensagem, eh_primeira_mensagem):
        mensagem = mensagem['message']['text']
        #ENVIAR
        if eh_primeira_mensagem == True or mensagem.lower() == 'opções':
            return f'''Olá! seja bem vindo ao bot de ofertas. 
            {os.linesep}Digite o número da oferta que quer receber
            {os.linesep}1 - Celulares
            {os.linesep}2 - Notebook
            {os.linesep}3 - Televisão
             '''
        if mensagem == '1' :
            return f''' Você recebera as melhores ofertas de celulares em breve
            {os.linesep}Confirmar(s/n) '''
        if mensagem == '2' :
            return f''' Você recebera as melhores ofertas de notebook em breve
            {os.linesep}Confirmar(s/n) '''
        if mensagem == '3' :
            return f''' Você recebera as melhores ofertas de televisão em breve
            {os.linesep}Confirmar(s/n) '''
        if mensagem == 'guta' :
            return f''' Mensagem secreta para você!
            {os.linesep} Te amo muito! Linda! '''
        
        if mensagem.lower() in ('s', 'sim'):
            return 'Recebimento de ofertas confirmado!'
        else:
            return 'Gostaria de ver as opções? Digite "opçoes"'

        

        
    #RESPONDER
    def responder(self, resposta, chat_id):
        #enviar
        link_de_envio = f'{self.url_base}sendMessage?chat_id={chat_id}&text={resposta}'
        requests.get(link_de_envio)


bot = TelegramBot()
bot.Iniciar()









