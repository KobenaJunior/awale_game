from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.screenmanager import SwapTransition
from kivy.core.window import Window
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.toast import toast
from kivy.uix.popup import Popup
from kivymd.uix.label import MDLabel
from kivy.clock import Clock

from kv_file import *
from moteur import *

from Negamax import *

import os,json,random,time



Window.size = (1100, 660)

sm = ScreenManager()

# fin du jeu
class HomeScreen(Screen):
    def color(self):
        on=(1,1,1,1)
        off=(0,0,0,1)
        self.joueurA.color=on if self.tour%2==0 else off
        self.joueurB.color=on if self.tour%2==1 else off

    def game_over(self):
        msg=f"[b][color=#00FF00]Egalité![/color][/b]"
        title="Egalité"
        if(self.pointA>self.pointB):
            title="Gagnant: Ordinateur"
            msg=f"[b][color=#0000FF]Ordinateur: {self.pointA}[/color][/b]"+"\n\n"+f"[b][color=#FF0000]Vous B: {self.pointB}[/color][/b]"
        elif(self.pointA<self.pointB):
            title="Gagnant: Vous B"
            msg=f"[b][color=#0000FF]Vous: {self.pointB}[/color][/b]"+"\n\n"+f"[b][color=#FF0000]Ordinateur: {self.pointA}[/color][/b]"
        self.content=MDBoxLayout(md_bg_color=(1,1,1,.9),line_color=(0,0,1,1),radius=[34,],orientation="vertical",pos_hint={'center_x':.5,'center_y':.5},padding=12)
        self.content.add_widget(MDLabel(text=msg,font_style="H5",bold=True,halign="center",markup=True))

        self.popup=Popup(title=title,size_hint=(.4,.8),background_color=(1,1,1,0),separator_color=(1,1,1,0),pos_hint={"center_x":.5,'center_y':.5},content=self.content,title_align='center')
        self.popup.open()

    def first_play(self):
        r=random.choice([0,1])
        if(r==0):
            self.tour=0
            toast("c'est A qui commence")
            self.color()
            
            Clock.schedule_once(self.naive_player,2.2)
        else:
            self.tour=1
            toast("c'est vous qui commencez") #le plateau face a soit correspond au joueur B donc a vous
            self.color()

    def on_grid_touch(self,instance, touch):
        if instance.collide_point(*touch.pos):
            # instance.clear_widgets()
            # print("depart: ",instance)
            # size=len(instance.children)
            try:
                ids=int(instance.id[-2:])
            except:
                ids=int(instance.id[-1])
            
            # if size<=0:return
            if(ids in range(6,12)):
                self.play(ids)
            # PLAY
            return True

    def distribute(self):
        i=0
        for hole in self.grid_table:
            hole.clear_widgets()
            hole.line_color=(0,0,0,.4)
            for pion in range(self.plateau[i]):
                hole.add_widget(
                    MDBoxLayout(
                        size_hint=(1,1),size=(12,12),
                        md_bg_color=(.8,.8,.8,1),radius=50
                    )
                )
            i+=1

        self.color()
    def color_hole_start_end(self,start,end):
        self.grid_table[end].line_color=(.6,.6,.8,1) #bleu couleur du trou d'arrivee
        self.grid_table[start].line_color=(0,.8,0,.8) #vert couleur du trou de depart
    def play(self,ids):
        # while self.playing:
        index=ids
        if(not self.ing):
            self.playing=True
            try:
                table,pointA,pointB,index=MoteurAwale().jeu(self.plateau,self.tour,self.pointA,self.pointB,index)
                if(table is None):
                    # print("non c'est pas ton tour")
                    # toast("Ce n'est pas ton tour")
                    return 0
                
                self.plateau,self.pointA,self.pointB,index_=table,pointA,pointB,index
                # print(f"table:{self.grid_table}, pointA:{self.pointA}, ppointB:{self.pointB}")
                self.tour+=1
                self.distribute()
                self.color_hole_start_end(ids,index_)
                
                self.id_pointA.text=f"pointA: {self.pointA}"
                self.id_pointB.text=f"pointB: {self.pointB}"
                self.pions_restant=sum(self.plateau)
                self.id_pions_restant.text=f"Pions restant: {self.pions_restant}"
            
                if(self.tour%2==0):
                    if(sum(self.plateau[0:6])==0):
                        self.pointB+=sum(self.plateau[6:12])
                        self.game_over()
                    else:
                        Clock.schedule_once(self.naive_player,1.0)
                elif(self.tour%2==1):
                    if(sum(self.plateau[6:12])==0):
                        self.pointA+=sum(self.plateau[0:6])
                        self.game_over()
                    else:
                        pass
            except Exception as e:
                print(f"\n\nerreur {e}\n\n")
            finally:
                self.ing=False
        else:
            print("y'a un boug qui joue actuellement")
    def naive_player(self,dt):
        try:
            moteur=MoteurAwale()
            #profondeur defini le niveau de "reflexion" ici on prends une profondeur de 8 , un compromis entre performance, efficacité et rapidité
            choix=meilleur_coup(moteur, self.plateau, self.tour, self.pointA, self.pointB, 8)
            print(f"\n\n Le choix pour l'algo est: {choix}\n\n")
            self.play(choix)
        except:
            print("\n\nerreur dans l'execution du Negamax\n\n")

    def init_game(self):

        # rayon des pions
        radius=(100,100)

        # initialisation de l'interface en ajoutant des details au plateau
        self.id_pions_restant=self.ids.pions_restant
        self.ids.pions_restant.text=f"Pions restant: 48"
        self.title_game=self.ids.title_game
        self.title_game.text="Awale~IA"

        self.title_game.md_bg_color=[0,0,0,0] #ici normalement on reinitialise le fond à un fond transparent mais cela ne se fait pas
        self.title_game.color=(0,0,0,1)
        self.joueurA=self.ids.joueurA 
        self.joueurB=self.ids.joueurB
        self.joueurA.color=(0,0,0,1)
        self.joueurB.color=(0,0,0,1)
        self.id_pointA=self.ids.pointA
        self.id_pointB=self.ids.pointB
        self.id_pointA.text=f"pointA: {0}"
        self.id_pointB.text=f"pointB; {0}"

        #Données de Jeux 
        self.grid_tab=[]
        self.tour=0 #definis qui joue, A si c'est un nbre paire, B sinon
        self.pointA=0 #les points de A
        self.pointB=0 #les points de B
        self.playing=True #etat du jeu, vrai tant que personne n'a gagné
        self.plateau=[4 for i in range(12)] #le plateau de depart

        self.ing=False#indique l'etat du jeu, si un joueur est en train de jouer ou non!

        self.indice_tab=[0,1,2,3,4,5,11,10,9,8,7,6] # l'ordre des indices et d'ajout des holes
        
        # Attention, le total pions dois prefferenciellement être un multiple de 12 et de 4
        cpt=0 #iterateur pour ajouter l'id au bon widget en locurence au self.grid_child
        total_pions=48 #total de pions sur le plateau
        nbre_line=total_pions//24
        nbre_trou_par_camp=total_pions//8
        nbre_pion_par_trou=total_pions//(nbre_line*nbre_trou_par_camp) #2

        # self.pions=

        for ind in range(nbre_line):
            self.box_1_2=MDBoxLayout(id=f'id_{ind}',orientation="horizontal",halign="center",
                pos_hint={"center_x":.5,"center_y":.5},spacing=10,padding=6,
                radius=24
                )
            for im in range(nbre_trou_par_camp):
                self.box_child=MDBoxLayout(
                    id=f'box{self.indice_tab[cpt]}',
                    orientation="horizontal",
                    halign="center",
                    pos_hint={"center_x":.5,"center_y":.5},
                    md_bg_color=(0,0,0,.8),
                    radius=radius,
                    size_hint=(1,.8),
                )
                self.grid_child=MDGridLayout(
                    id=f'{self.indice_tab[cpt]}',
                    pos_hint={"center_x":.5,"center_y":.5},
                    spacing=(6,6),
                    cols=2,
                    size_hint=(1,1),
                    radius=radius,
                    padding=22,
                    line_color=(0,0,0,.4),
                    line_width=3,
                    )
                cpt+=1
                self.grid_tab.append(self.grid_child)
                self.grid_child.bind(on_touch_down=self.on_grid_touch)
                self.box_child.add_widget(self.grid_child)
                self.box_1_2.add_widget(self.box_child)
            self.ids.box_parent.add_widget(self.box_1_2)

        self.grid_table=[]
        self.grid_table=[ self.grid_tab[indice] for indice in self.indice_tab]
        
        # self.grid_tab=[self.grid_tab[0],self.grid_tab[1],self.grid_tab[2],self.grid_tab[3],self.grid_tab[4],self.grid_tab[5],self.grid_tab[11],self.grid_tab[10],self.grid_tab[9],self.grid_tab[8],self.grid_tab[7],self.grid_tab[6]]
        

        self.distribute()
        self.first_play()
        

    def start(self):
        # self.init_game()
        if(self.ids.button_start.text=='demarer'):
            self.init_game()
            self.ids.button_start.text='recommencer'
        else:
            self.ids.box_parent.clear_widgets()
            self.ids.button_start.text='demarer'
            self.start()
    def update_point(self):
        pass
class SettingScreen(Screen):
    pass

sm = ScreenManager(transition=SwapTransition())
sm.add_widget(SettingScreen(name='setting'))
sm.add_widget(HomeScreen(name='home'))

class DemoApp(MDApp):
    def build(self):
        name='Awale-IA'
        self.theme_cls.material_style = "M3"
        self.theme_cls.theme_style = "Light"
        screen = Builder.load_string(screen_helper)

        return screen

    def on_start(self):
        pass

    

DemoApp().run()

