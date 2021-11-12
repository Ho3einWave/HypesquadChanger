import requests,json,tabulate

print('''
        .--.       .--.
    _  `    \     /    `  _
     `\.===. \.^./ .===./`
            \/`"`\/
         ,  |     |  ,
        / `\|;-.-'|/` \\
       /    |::\  |    \\
    .-' ,-'`|:::; |`'-, '-.
        |   |::::\|   | 
        |   |::::;|   |
        |   \:::://   |
        |    `.://'   |
       .'             `.
    _,'                 `,_
 + Hypesquad Changer Script +
       - By Ho3einWave -
      ''')

config = ''
token = ''
try:
    with open('config.json', 'r') as file:
        jsonfile = file.read()
        try:
            config = json.loads(jsonfile)
        except json.decoder.JSONDecodeError as error:
            print('Token String in config.json is not valid enter the token again!')
            token = input('Enter Token: ')
            config = {'token': token}
            with open('config.json', 'w') as file:
                file.write(json.dumps(config))
except FileNotFoundError as error:
    token = input('Enter Token: ')
    config = {'token': token}
    with open('config.json', 'w') as file:
        file.write(json.dumps(config))



hypeSquad = int(input('With Type Of Hype Squad You Want? [3:Balance, 2:Bravery, 1:Brilliance] : '))

headers = {
    'authorization': config['token']
}

body = {
    'house_id': hypeSquad
}
meResponse = requests.get(
    'https://canary.discordapp.com/api/v6/users/@me', headers=headers)
if meResponse.status_code == 401:
    print('Token is Invalid! Exiting...')
    with open('config.json', 'w') as file:
        file.write('')
    exit()
userinfo = meResponse.json()
print('[+] USER ACCOUNT INFO ')
table = [
        ['Username', userinfo['username']],
        ['Tag', userinfo['discriminator']],
        ['UserID', userinfo['id']],
        ['Email', userinfo['email']],
        ['Phone', userinfo['phone']]

]

print(tabulate.tabulate(table,tablefmt='pretty'))

response = requests.post(
    'https://discord.com/api/v9/hypesquad/online', headers=headers, json=body)
if response.status_code == 204:
    print('Hypesquad Changed Successfuly!')
elif response.status_code == 401:
    print('Token is invalid or expire!')
elif response.status_code == 429:
    print('Too many requests please try after 5 mins!')
