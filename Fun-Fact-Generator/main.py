import json
import requests
from pywebio import start_server
from pywebio.input import *
from pywebio.output import *
from pywebio.session import *

def get_fun_fact(_):
    # Clear above screen
    clear()
    
    put_html("<p align='left'><h2>Fun Facts :)</h2></p>")
    
    # URL from where we fetch the data
    url = "https://uselessfacts.jsph.pl/random.json?language=en"
    
    # Use GET request
    response = requests.request("GET", url)
    
    # Load the request in json file
    data = json.loads(response.text)
    
    # we will need 'text' from the list, so
    # pass 'text' in the list
    useless_fact = data['text']
    
    # Put the facts in the blue color
    # Put the click me button
    style(put_text(useless_fact), 'color:#1a1a1a; font-size: 30px')
    put_buttons(
        [dict(label='Click me', value='outline-success', 
              color='outline-success')], onclick=get_fun_fact)

def main():
    # Put a heading "Fun Fact Generator"
    put_html("<p align='center'><h2>Fun Facts :)</h2></p>")
    
    put_html("<title>Fun Facts :) </title>")
    # hold the session for long time
    # Put a Click me button
    put_buttons(
        [dict(label='Click me', value='outline-success', 
             color='outline-success')], onclick=get_fun_fact)
    hold()

if __name__ == '__main__':
    start_server(main, port=8080, debug=True)
