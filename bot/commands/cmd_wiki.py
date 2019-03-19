from bs4 import BeautifulSoup
import requests as re

import pandas as pd
import _thread

#import os.path

# credits to:
# Southclaws - general assistance
# iAmir - general assistance
# _SyS_ - helping with the scraping

url = "https://wiki.sa-mp.com/wiki/"

def cmd_wiki(bot, update, args):
    _thread.start_new_thread(cmd_wiki_thread(bot, update, args))

def cmd_wiki_thread(bot, update, args):
    try:
        arg_check = args[0]
    except:
        return update.message.reply_text('You must specify what you would like to search in the wiki!')
        
    wiki_func = args[0]
    wiki_url = url + wiki_func

    #if os.path.isfile(f'bot/wiki-cache/{wiki_func}.cache') is True:
        #with open(f'bot/wiki-cache/{wiki_func}.cache', 'r') as f:
            #return update.message.reply_markdown(f.read())

    response = re.get(wiki_url)
    soup = BeautifulSoup(response.content, "lxml")

    try:
        description = soup.select_one('.description').text
    except:
        return update.message.reply_text(f'SA-MP Wiki | {wiki_func}\n- This article does not exist!')

    #initial_parameters = soup.select('.parameters, .param')
    #final_parameters = [parameter.text for parameter in initial_parameters]

    initial_parameters = soup.select('.param')

    final_parameters = ""
    for nodes in initial_parameters:
        final_parameters += nodes.find('td').text + ' - '+ nodes.find('td').find_next().text +"\n"

    returnValues = soup.select_one('#bodyContent > .param + p + div').text
    exampleUsage = soup.select_one('.pawn').text

    results = [description, returnValues, exampleUsage]

    output = f'SA-MP Wiki | {wiki_func}\n'
    output += f'{wiki_url}\n\n'

    output += f'*Description:*\n'
    output += f'  {results[0]}\n\n'

    output += f'*Parameters:*\n'
    output += f'{final_parameters}\n'

    output += f'*Return Values:*\n'
    output += f'  {results[1]}\n\n'

    output += f'*Example Usage:*\n'
    output += f'```\n{results[2]}```\n\n'

    update.message.reply_markdown(output)

    #with open(f'bot/wiki-cache/{wiki_func}.cache', 'w') as f:
        #f.write(output)