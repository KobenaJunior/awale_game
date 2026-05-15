#INTERFACE GRAPHIQUE DU JEU AWALE

screen_helper = """


ScreenManager:
    HomeScreen:
    SettingScreen:
    
<HomeScreen>:
    name: 'home'
    FitImage:
        id:fond
        source:'assets/one.jpg'
        size_hint:1,1
        pos_hint: {"center_x": .5, "center_y": .5}
    MDLabel:
        id:title_game
        text: "Awale~IA"
        color:(0,0,0,1)
        font_style: "H5"
        bold: True
        size_hint:None,None
        halign:'center'
        size:250,40
        pos_hint: {"center_x": .48, "center_y": .94}
    MDBoxLayout:
        size_hint:None,None
        size:200,60
        padding:4
        orientation:'horizontal'
        pos_hint:{'center_x':.5,'center_y':.08}
        md_bg_color:(0,0,0,.4)
        radius:[16]
        halign:'center'
        MDLabel:
            text:'Depart'
            color:(0,.8,0,.8)
            halign:'center'
            bold:True
        MDLabel:
            text:"Arrivé"
            color:(.6,.6,.8,1)
            halign:'center'
            bold:True
    MDLabel:
        text: " Par Kobena Junior K."
        size_hint:None,None
        size:250,40
        pos_hint: {"center_x": .9, "center_y": .05}

    MDBoxLayout:
        orientation:'vertical'
        spacing:2
        padding:10,4
        halign:'center'
        size_hint:None,None
        size:220,80
        radius:12
        # md_bg_color:0,0,0,.3
        pos_hint:{'center_x':.12,'center_y':.06}
        MDLabel:
            id:pions_restant
            text:"Pions restant: 48"
        MDLabel:
            id:pointA
            text:'pointA:...'
        MDLabel:
            id:pointB
            text:'pointB:...'
    MDIcon:
        icon:'arrow-down-thick'
        pos_hint:{'center_y':.5,'center_x':.97}
        font_size:'50sp'
    MDIcon:
        icon:'arrow-up-thick'
        pos_hint:{'center_y':.5,'center_x':.03}
        font_size:'50sp'
    MDFlatButton:
        id:button_start
        text:'demarer'
        pos_hint:{'center_x':.06,'center_y':.96}
        md_bg_color:0,0,0,1
        theme_text_color:'Custom'
        text_color:1,1,1,1
        on_press:root.start()

    MDBoxLayout:
        orientation:'vertical'
        halign:'center'
        size_hint:None,None
        size:950,400
        pos_hint:{'center_x':.5,'center_y':.5}
        md_bg_color:0,0,0,.1
        spacing:6
        padding:14
        radius:[24,]
        MDBoxLayout:
            size_hint:1,None
            size:22,12
            spacing:8
            padding:25,6,25,6
            MDLabel:
                text:'1'
                halign:'center'
            MDLabel:
                text:'2'
                halign:'center'
            MDLabel:
                text:'3'
                halign:'center'
            MDLabel:
                text:'4'
                halign:'center'
            MDLabel:
                text:'5'
                halign:'center'
            MDLabel:
                text:'6'
                halign:'center'
        MDBoxLayout:
            orientation:'horizontal'
            size_hint:1,1
            # md_bg_color:1,0,0,.2
            spacing:10
            MDBoxLayout:
                size_hint:None,1
                size:18,12
                spacing:8
                orientation:'vertical'
                padding:2
                halign:'center'
                # md_bg_color:1,0,1,.2
                MDLabel:
                    id:joueurA
                    font_style:'H6'
                    text:'A'
                    halign:'center'
                    bold:True
                MDLabel:
                    id:joueurB
                    font_style:'H6'
                    text:'B'
                    halign:'center'
                    bold:True
            MDBoxLayout:
                id:box_parent
                orientation:"vertical"
                halign:"center"
                size_hint:1,1
                size:900,400
                pos_hint:{"center_x":.5,"center_y":.5}
                md_bg_color:0,0,0,.3
                spacing:8
                padding:6
                radius:[24,]
        MDBoxLayout:
            size_hint:1,None
            size:22,12
            spacing:8
            padding:25,6,25,6
            MDLabel:
                text:'12'
                halign:'center'
            MDLabel:
                text:'11'
                halign:'center'
            MDLabel:
                text:'10'
                halign:'center'
            MDLabel:
                text:'9'
                halign:'center'
            MDLabel:
                text:'8'
                halign:'center'
            MDLabel:
                text:'7'
                halign:'center'

<SettingScreen>:
    name:'setting'
"""
