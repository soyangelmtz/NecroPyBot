"""
    <Necrython BOT - Origin V10>
"""

from todo import *
import requests
from urllib.request import urlopen

def licence_check(player):
    if player:
        ping = get_ping()
        if ping != 0 and (not player.getStorageValue("last_ping") or ping != player.getStorageValue("last_ping")):
            player.setStorageValue("last_ping", ping)
            wx.CallAfter(Menus.Main.SetTitle, u"%s BOT - %s | %d ms" % (GAME_TITLE, player.getName(), ping))

def get_ping():
    try:
        ping_response = subprocess.Popen("ping -w 500 -n 1 www.necroxia.com", stdout=subprocess.PIPE).stdout.read()
        return int(lstring.match(ping_response, "Media = (%d+)ms"))
    except:
        return 9999

Signal.startHandler()
Keyboard.thread.start()

if OS_WINDOWS:
    if not SetConsoleCtrlHandler(ctrl_handler, 1):
        Client.speak("Existe un problema con el controlador.")
        print("Unable to add SetConsoleCtrlHandler")
        exit()
else:
    Client.speak("Solo funciono en Windows.")
    print("Only work on Windows!")
    exit()

BOT_PID = os.getpid()

try:
    with open('key.pem', 'r') as pem:
        print("key.pem found!")
except OSError:
    Window_Speak.speak("No se pudo abrir el archivo key pem!")
    print("key.pem not found!")
    g_game.shutdown()

g_licence = Dispatcher(True)

APP = wx.App(False)
Menu = GuiMainMenu()
if Memory.loadGameClient():
    Main.run()
    g_licence.addTask(6, licence_check)
else:
    Menu.Hide()
APP.MainLoop()
