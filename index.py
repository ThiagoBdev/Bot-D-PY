import discord
import os

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

        #Definições das regras
        
        if message.content.lower() == '?regras':
            await message.channel.send(f'{message.author.name}As regras do servidor são:{os.linesep}1-- Não irrite o adm, pq ele esta frescurento{os.linesep}2-- Não fale a palavra RO, caso contrario é ban{os.linesep}3--Proibido musica da manu gavassi, somos todos Team Prior{os.linesep}4-Sem musica estourada, os ouvidos do adm são sensíveis{os.linesep}--aguarde por mais regras--')
        #mensagem direta
        elif message.content.lower() == '?ajuda':
            await message.author.send('Em que posso te ajudar ?')

        #mensagem de boas-vindas
    async def on_member_join(self,member):
        guild = member.guild

        if guild.system_channel is not None:
            mensagem = f'{member.mention} Bem-vindo ao {guild.name}'
            await guild.system_channel.send(mensagem)


intents = discord.Intents.default()
intents.members= True


client = MyClient(intents=intents)
    #insira o token do bot em "#"
client.run('#')