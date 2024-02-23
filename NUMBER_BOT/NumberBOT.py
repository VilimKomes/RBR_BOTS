import discord
import pandas as pd
from pathlib import Path
import re

def UserInput(user_input):
	flag=0
	info=user_input.split("!choose ",1)[1]
	chosen_number=info.split(" ")[0]
	if int(chosen_number)<1 or int(chosen_number)>NumberOfDrivers():
		flag=2
	if NumberExists(chosen_number):
		flag=1
	if flag==0:
		WriteDrivers(info)
	return flag, chosen_number

def DriverName(n):
	df=pd.read_csv('Register.csv')
	row=df[df['Number']==int(n)]['Name'].index
	return df['Name'].values[row][0]

def NumberExists(cN):
	df=pd.read_csv('Register.csv')
	return int(cN) in df['Number'].values

def NumberOfDrivers():
	df=pd.read_csv('Drivers.csv')
	N=len(df)-4
	return N

def WriteDrivers(info):
    info=info.split(" ")
    df=pd.DataFrame({'Name':[" ".join(info[1:4])],'Number':info[0]})
    df.to_csv('Register.csv', mode='a', header=False,index=False)

def printNumbers():
    df=pd.read_csv('Register.csv',index_col=0)
    df_sorted=df.sort_values(by=['Number'])
    df_sorted=df_sorted.to_string().strip()[11:].strip()
    return re.sub(' +',' ',df_sorted)

def main():
    Int = discord.Intents.default()
    Int.message_content = True
    client=discord.Client(intents=Int)
    # Number Bot Token
    #TOKEN='MTE5NzkyNDI0MTI3MDY0NTAxOA.GUcQSJ.uQYKwiD3cX_bpyxII-LAVLBYrpYHhUH7z5MKqk'

    @client.event
    async def on_ready():
        print('We have logged in as {0.user}'.format(client))

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        if message.content.startswith('!Numbers'):
            await message.channel.send(printNumbers())
        if message.content.startswith('!Drivers'):
            await message.channel.send('Number of drivers in GARC '+str(NumberOfDrivers()))
        if message.content.startswith('!choose'):
            user_input=str(message.content)
            flag,cN=UserInput(user_input)
            if flag==0:
                await message.channel.send('You have chosen '+str(cN))
            elif flag==1:
                await message.channel.send(str(DriverName(cN))+' has chosen that number')
            elif flag==2:
                await message.channel.send('Wrong input')
            else:
                await message.channel.send('How did this happen')

    client.run(TOKEN)

if __name__=='__main__':
	main()
