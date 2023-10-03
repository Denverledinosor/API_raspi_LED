from flask import Flask, request, render_template
from os import listdir 
app = Flask(_name_)
import scriptled
from scriptled import *
import profil1
import profil2
import profil3
import profil4
import profil5

@app.route('/')
def my_form():
    return render_template('index.html')
#Variable pour différencier les commandes d'un script
nbcommande = 0
@app.route('/', methods=['GET','POST'])
#Route par défaut pour le test des programmes n'enregistre pas de profil
def my_form_post():
    input_status = ''
    if request.method == 'POST':
        input_status = request.form['text_box'] #prend les données dans la key text_box
        with open('./file/status.txt',"w") as f:
            f.write(str(input_status))
        with open('./file/status.txt',"r") as f:
            try:
                colors = f.read().strip().split(',')
                if colors[0] =='theaterChase':
                    scriptled.theaterChase(strip, Color(int(colors[1]), int(colors[2]), int(colors[3]), a=int(colors[4]), b=int(colors[5]),c=int(colors[6])))
                elif colors[0] =='smooth':
                    scriptled.theaterChase(strip, Color(int(colors[1]), int(colors[2]), int(colors[3]), a=int(colors[4]), b=int(colors[5]),c=int(colors[6])))
                elif colors[0] =='color_wipe':
                    scriptled.color_wipe(strip, Color(int(colors[1]), int(colors[2]), int(colors[3]), a=int(colors[4]), b=int(colors[5]),c=int(colors[6])))
                elif colors[0] =='scroll_in':
                    scriptled.scriptled.theaterChase(strip, Color(int(colors[1]), int(colors[2]), int(colors[3]), a=int(colors[4]), b=int(colors[5]),c=int(colors[6])))(strip, Color(int(colors[1]), int(colors[2]), int(colors[3]), a=int(colors[4]), b=int(colors[5]),c=int(colors[6])))
                elif colors[0] =='scroll_out':
                    scriptled.scroll_out(strip, Color(int(colors[1]), int(colors[2]), int(colors[3]), a=int(colors[4]), b=int(colors[5]),c=int(colors[6])))
                elif colors[0] =='rainbowCycle':
                    scriptled.rainbowCycle(strip, Color(int(colors[1]), int(colors[2]), int(colors[3]), a=int(colors[4]), b=int(colors[5]),c=int(colors[6])))
                elif colors[0] =='theaterChaseRainbow:
                    scriptled.theaterChaseRainbow(strip, Color(int(colors[1]), int(colors[2]), int(colors[3]), a=int(colors[4]), b=int(colors[5]),c=int(colors[6])))             
                elif colors[0] =='off':
                    scriptled.stop()
                elif colors[0] =='on':
                    scriptled.on()
                elif colors[0] =='zero':
                    scriptled.strip.begin()
                    scriptled.smooth(strip,Color(0,0,0),1,300,255)
                else:
                    scriptled.theaterChase(strip, Color(int(colors[1]), int(colors[2]), int(colors[3]), a=int(colors[4]), b=int(colors[5]),c=int(colors[6])))
            except:
                print("Could not read file, trying again")

    return render_template("index.html")
#Route pour enregister son profil
@app.route('/profil', methods=['GET','POST'])

    