from selenium import webdriver #line:1
from selenium .webdriver .common .by import By #line:2
from selenium .webdriver .common .keys import Keys #line:3
from selenium .webdriver .support .ui import WebDriverWait #line:4
from selenium .webdriver .support import expected_conditions as EC #line:5
from selenium .webdriver .common .action_chains import ActionChains #line:6
import pyperclip #line:7
import time #line:8
import tkinter as tk #line:9
from tkinter import ttk ,messagebox #line:10
import json #line:11
import threading #line:12
import os #line:13
import requests #line:14
SETTINGS_FILE ="discord_settings.json"#line:17
def load_settings ():#line:20
    O00OOO00O0000OO0O ={"email":"ethicaljohndoe@gmail.com","password":"Lha@@19101978","channel_url":"https://discord.com/channels/1330294383874019370/1357909599621222460"}#line:25
    if os .path .exists (SETTINGS_FILE ):#line:26
        try :#line:27
            with open (SETTINGS_FILE ,'r')as OOO000O0O0000O0OO :#line:28
                return json .load (OOO000O0O0000O0OO )#line:29
        except :#line:30
            pass #line:31
    return O00OOO00O0000OO0O #line:32
def save_settings (O00O0O0O0OO00000O ,OO0OO00OOOOOOO00O ,OOOOOOO0000O0OOO0 ):#line:35
    O0OO00OOOO00O0OOO ={"email":O00O0O0O0OO00000O ,"password":OO0OO00OOOOOOO00O ,"channel_url":OOOOOOO0000O0OOO0 }#line:40
    with open (SETTINGS_FILE ,'w')as O0O0O0O00O0OOO00O :#line:41
        json .dump (O0OO00OOOO00O0OOO ,O0O0O0O00O0OOO00O )#line:42
def fetch_credentials ():#line:45
    try :#line:46
        O00OO0OOO00000O0O =requests .get ("https://pastebin.com/raw/3BuarSay")#line:47
        O00OO0OOO00000O0O .raise_for_status ()#line:48
        O000000OO00OOOOO0 ={}#line:49
        for O00O0OOO0O000O0OO in O00OO0OOO00000O0O .text .strip ().split ('\n'):#line:50
            O0OOOO0000000O00O ,OOOO00000OO00OOO0 =O00O0OOO0O000O0OO .split (',')#line:51
            O000000OO00OOOOO0 [O0OOOO0000000O00O .strip ()]=OOOO00000OO00OOO0 .strip ()#line:52
        return O000000OO00OOOOO0 #line:53
    except Exception as OO0OO0OO00O0O0OO0 :#line:54
        messagebox .showerror ("Error",f"Failed to fetch credentials: {OO0OO0OO00O0O0OO0}")#line:55
        return {}#line:56
settings =load_settings ()#line:59
EMAIL =settings ["email"]#line:60
PASSWORD =settings ["password"]#line:61
CHANNEL_URL =settings ["channel_url"]#line:62
BASE_LINE ="This server is vulnerable against BotNet attacks | Contact me and let's fix it: guns.lol/hackerone"#line:65
MESSAGE ="////\n"+"\n".join ([BASE_LINE ]*31 )+"\n////"#line:66
if len (MESSAGE )>2000 :#line:67
    MESSAGE =MESSAGE [:2000 ]#line:68
class DiscordBotGUI :#line:71
    def __init__ (O00O000O00OO000O0 ,OO0000000OO000O00 ):#line:72
        O00O000O00OO000O0 .root =OO0000000OO000O00 #line:73
        O00O000O00OO000O0 .root .title ("Discord Automation Bot")#line:74
        O00O000O00OO000O0 .root .geometry ("400x300")#line:75
        O00O000O00OO000O0 .root .resizable (False ,False )#line:76
        O00O000O00OO000O0 .is_running =False #line:77
        O00O000O00OO000O0 .driver =None #line:78
        O00O000O00OO000O0 .thread =None #line:79
        O00O000O00OO000O0 .root .configure (bg ="#2C2F33")#line:82
        O00OO0O0000O0OOOO =ttk .Style ()#line:83
        O00OO0O0000O0OOOO .configure ("TButton",font =("Helvetica",10 ),padding =10 )#line:84
        O00OO0O0000O0OOOO .configure ("TLabel",background ="#2C2F33",foreground ="#FFFFFF",font =("Helvetica",10 ))#line:85
        O00OO0O0000O0OOOO .configure ("TEntry",fieldbackground ="#23272A",foreground ="#FFFFFF")#line:86
        O00O000O00OO000O0 .main_frame =ttk .Frame (O00O000O00OO000O0 .root ,padding ="10")#line:89
        O00O000O00OO000O0 .main_frame .grid (row =0 ,column =0 ,sticky ="nsew")#line:90
        O00O000O00OO000O0 .status_var =tk .StringVar (value ="Status: Idle")#line:93
        O00O000O00OO000O0 .status_label =ttk .Label (O00O000O00OO000O0 .main_frame ,textvariable =O00O000O00OO000O0 .status_var )#line:94
        O00O000O00OO000O0 .status_label .grid (row =0 ,column =0 ,columnspan =2 ,pady =10 )#line:95
        O00O000O00OO000O0 .start_stop_button =ttk .Button (O00O000O00OO000O0 .main_frame ,text ="Start Bot",command =O00O000O00OO000O0 .toggle_bot )#line:98
        O00O000O00OO000O0 .start_stop_button .grid (row =1 ,column =0 ,columnspan =2 ,pady =10 )#line:99
        O00O000O00OO000O0 .settings_button =ttk .Button (O00O000O00OO000O0 .main_frame ,text ="Settings",command =O00O000O00OO000O0 .open_settings )#line:102
        O00O000O00OO000O0 .settings_button .grid (row =2 ,column =0 ,columnspan =2 ,pady =10 )#line:103
        O00O000O00OO000O0 .log_text =tk .Text (O00O000O00OO000O0 .main_frame ,height =8 ,width =40 ,bg ="#23272A",fg ="#FFFFFF",font =("Helvetica",9 ))#line:106
        O00O000O00OO000O0 .log_text .grid (row =3 ,column =0 ,columnspan =2 ,pady =10 )#line:107
        O00O000O00OO000O0 .log_text .config (state ='disabled')#line:108
    def log (OO0OO0O000OO00O00 ,O000OO0O0OOOOO00O ):#line:110
        OO0OO0O000OO00O00 .log_text .config (state ='normal')#line:111
        OO0OO0O000OO00O00 .log_text .insert (tk .END ,O000OO0O0OOOOO00O +"\n")#line:112
        OO0OO0O000OO00O00 .log_text .see (tk .END )#line:113
        OO0OO0O000OO00O00 .log_text .config (state ='disabled')#line:114
    def toggle_bot (O000000O0O00OOOOO ):#line:116
        if not O000000O0O00OOOOO .is_running :#line:117
            O000000O0O00OOOOO .is_running =True #line:118
            O000000O0O00OOOOO .start_stop_button .configure (text ="Stop Bot")#line:119
            O000000O0O00OOOOO .status_var .set ("Status: Running")#line:120
            O000000O0O00OOOOO .log ("Starting bot...")#line:121
            O000000O0O00OOOOO .thread =threading .Thread (target =O000000O0O00OOOOO .run_bot )#line:122
            O000000O0O00OOOOO .thread .start ()#line:123
        else :#line:124
            O000000O0O00OOOOO .is_running =False #line:125
            O000000O0O00OOOOO .start_stop_button .configure (text ="Start Bot")#line:126
            O000000O0O00OOOOO .status_var .set ("Status: Stopping...")#line:127
            O000000O0O00OOOOO .log ("Stopping bot...")#line:128
            if O000000O0O00OOOOO .driver :#line:129
                O000000O0O00OOOOO .driver .quit ()#line:130
    def open_settings (OOOO000000000O0O0 ):#line:132
        OOOOOOO0OOO0O0OO0 =tk .Toplevel (OOOO000000000O0O0 .root )#line:133
        OOOOOOO0OOO0O0OO0 .title ("Settings")#line:134
        OOOOOOO0OOO0O0OO0 .geometry ("300x200")#line:135
        OOOOOOO0OOO0O0OO0 .configure (bg ="#2C2F33")#line:136
        OOOOOOO0OOO0O0OO0 .resizable (False ,False )#line:137
        OO000O00O0OOOO0O0 =ttk .Frame (OOOOOOO0OOO0O0OO0 ,padding ="10")#line:140
        OO000O00O0OOOO0O0 .grid (row =0 ,column =0 ,sticky ="nsew")#line:141
        ttk .Label (OO000O00O0OOOO0O0 ,text ="Email:").grid (row =0 ,column =0 ,sticky ="w",pady =5 )#line:144
        OO0000000OOO0OOO0 =tk .StringVar (value =EMAIL )#line:145
        O00OOOOO0O0000000 =ttk .Entry (OO000O00O0OOOO0O0 ,textvariable =OO0000000OOO0OOO0 ,width =30 )#line:146
        O00OOOOO0O0000000 .grid (row =0 ,column =1 ,pady =5 )#line:147
        ttk .Label (OO000O00O0OOOO0O0 ,text ="Password:").grid (row =1 ,column =0 ,sticky ="w",pady =5 )#line:150
        O00O00OO0000O0OOO =tk .StringVar (value =PASSWORD )#line:151
        OOOO0OOOO00OOOO0O =ttk .Entry (OO000O00O0OOOO0O0 ,textvariable =O00O00OO0000O0OOO ,width =30 ,show ="*")#line:152
        OOOO0OOOO00OOOO0O .grid (row =1 ,column =1 ,pady =5 )#line:153
        ttk .Label (OO000O00O0OOOO0O0 ,text ="Channel URL:").grid (row =2 ,column =0 ,sticky ="w",pady =5 )#line:156
        OO000OOO0O0OOOO00 =tk .StringVar (value =CHANNEL_URL )#line:157
        OO000O000O0OO00O0 =ttk .Entry (OO000O00O0OOOO0O0 ,textvariable =OO000OOO0O0OOOO00 ,width =30 )#line:158
        OO000O000O0OO00O0 .grid (row =2 ,column =1 ,pady =5 )#line:159
        def OOOOOO00000000OOO ():#line:162
            global EMAIL ,PASSWORD ,CHANNEL_URL #line:163
            EMAIL =OO0000000OOO0OOO0 .get ()#line:164
            PASSWORD =O00O00OO0000O0OOO .get ()#line:165
            CHANNEL_URL =OO000OOO0O0OOOO00 .get ()#line:166
            save_settings (EMAIL ,PASSWORD ,CHANNEL_URL )#line:167
            OOOO000000000O0O0 .log ("Settings saved.")#line:168
            OOOOOOO0OOO0O0OO0 .destroy ()#line:169
        ttk .Button (OO000O00O0OOOO0O0 ,text ="Save",command =OOOOOO00000000OOO ).grid (row =3 ,column =0 ,columnspan =2 ,pady =10 )#line:171
    def run_bot (O0OOO00000OO000OO ):#line:173
        try :#line:174
            OO00000OO00O000OO =webdriver .ChromeOptions ()#line:175
            OO00000OO00O000OO .add_argument ("--start-maximized")#line:176
            O0OOO00000OO000OO .driver =webdriver .Chrome (options =OO00000OO00O000OO )#line:177
            O0OOO00000OO000OO .log (f"Message length: {len(MESSAGE)} characters")#line:178
            login_discord (O0OOO00000OO000OO .driver )#line:179
            WebDriverWait (O0OOO00000OO000OO .driver ,20 ).until (EC .url_contains ("channels"))#line:180
            O0OOO00000OO000OO .log ("Logged in successfully")#line:181
            send_message (O0OOO00000OO000OO .driver ,num_messages =100 ,batch_size =7 ,batch_delay =3 )#line:182
        except Exception as O00000OO0O000OO0O :#line:183
            O0OOO00000OO000OO .log (f"An error occurred: {O00000OO0O000OO0O}")#line:184
        finally :#line:185
            if O0OOO00000OO000OO .driver :#line:186
                O0OOO00000OO000OO .driver .quit ()#line:187
            O0OOO00000OO000OO .is_running =False #line:188
            O0OOO00000OO000OO .start_stop_button .configure (text ="Start Bot")#line:189
            O0OOO00000OO000OO .status_var .set ("Status: Idle")#line:190
            O0OOO00000OO000OO .log ("Bot stopped")#line:191
def login_discord (OOOO0OOO0OO0O000O ):#line:194
    OOOO0OOO0OO0O000O .get ("https://discord.com/login")#line:195
    OO0O0OOOOOOOOO0OO =WebDriverWait (OOOO0OOO0OO0O000O ,10 ).until (EC .presence_of_element_located ((By .NAME ,"email")))#line:198
    OO0O0OOOOOOOOO0OO .send_keys (EMAIL )#line:199
    OOOOO0OOOO0OOOOO0 =OOOO0OOO0OO0O000O .find_element (By .NAME ,"password")#line:200
    OOOOO0OOOO0OOOOO0 .send_keys (PASSWORD )#line:201
    O0O00OOOOOO0OOO0O =OOOO0OOO0OO0O000O .find_element (By .XPATH ,"//button[@type='submit']")#line:202
    O0O00OOOOOO0OOO0O .click ()#line:203
def toggle_dev_tools (O000OO0OOOO0O000O ):#line:205
    try :#line:206
        O00OOOO000O00OO0O =ActionChains (O000OO0OOOO0O000O )#line:207
        O0OOOO000O0000OOO =Keys .COMMAND if O000OO0OOOO0O000O .capabilities ['platformName'].lower ()=='mac'else Keys .CONTROL #line:208
        O00OOOO000O00OO0O .key_down (O0OOOO000O0000OOO ).key_down (Keys .SHIFT ).send_keys ('i').key_up (Keys .SHIFT ).key_up (O0OOOO000O0000OOO ).perform ()#line:209
        O00OOOO000O00OO0O .key_down (O0OOOO000O0000OOO ).key_down (Keys .SHIFT ).send_keys ('i').key_up (Keys .SHIFT ).key_up (O0OOOO000O0000OOO ).perform ()#line:210
        gui .log ("Toggled developer tools to dismiss anti-spam popup")#line:211
        return True #line:212
    except Exception as OO0000000000OO000 :#line:213
        gui .log (f"Failed to toggle dev tools: {OO0000000000OO000}")#line:214
        return False #line:215
def click_chill_zone (OOO0O0OO0000OO000 ):#line:217
    try :#line:218
        OO0OO0000OOOO00O0 =WebDriverWait (OOO0O0OO0000OO000 ,1 ).until (EC .element_to_be_clickable ((By .XPATH ,"//button[.//div[contains(text(), 'Enter the chill zone')]]")))#line:223
        OO0OO0000OOOO00O0 .click ()#line:224
        gui .log ("Clicked 'Enter The Chill Zone' button")#line:225
        return True #line:226
    except :#line:227
        return False #line:228
def handle_anti_spam (O0OOO000OO00OO00O ):#line:230
    return toggle_dev_tools (O0OOO000OO00OO00O )or click_chill_zone (O0OOO000OO00OO00O )#line:231
def send_message (O0OO00000O0000O00 ,num_messages =100 ,batch_size =7 ,batch_delay =3 ):#line:233
    O0OO00000O0000O00 .get (CHANNEL_URL )#line:234
    OO0OO0OO0O00O0OO0 =WebDriverWait (O0OO00000O0000O00 ,20 ).until (EC .presence_of_element_located ((By .CSS_SELECTOR ,"div[role='textbox'][class*='slateTextArea']")))#line:237
    WebDriverWait (O0OO00000O0000O00 ,20 ).until (EC .element_to_be_clickable ((By .CSS_SELECTOR ,"div[role='textbox'][class*='slateTextArea']")))#line:240
    gui .log ("Message box found, starting to send messages...")#line:241
    O00O00O0OOOO0OO00 =0 #line:243
    while O00O00O0OOOO0OO00 <num_messages and gui .is_running :#line:244
        O000O0O0OOO00OOO0 =min (batch_size ,num_messages -O00O00O0OOOO0OO00 )#line:245
        for _OOO00O00O0O000000 in range (O000O0O0OOO00OOO0 ):#line:246
            try :#line:247
                handle_anti_spam (O0OO00000O0000O00 )#line:248
                pyperclip .copy (MESSAGE )#line:249
                OO0OO0OO0O00O0OO0 .click ()#line:250
                O00OO0O00O00O00O0 =Keys .COMMAND if O0OO00000O0000O00 .capabilities ['platformName'].lower ()=='mac'else Keys .CONTROL #line:251
                ActionChains (O0OO00000O0000O00 ).key_down (O00OO0O00O00O00O0 ).send_keys ('v').key_up (O00OO0O00O00O00O0 ).perform ()#line:252
                O0O00OO00O0OOOOOO =OO0OO0OO0O00O0OO0 .get_attribute ("innerText")#line:253
                if len (O0O00OO00O0OOOOOO )<len (MESSAGE )-100 :#line:254
                    gui .log (f"Warning: Message {O00O00O0OOOO0OO00 + 1} truncated in textbox")#line:255
                OO0OO0OO0O00O0OO0 .send_keys (Keys .RETURN )#line:256
                O00O00O0OOOO0OO00 +=1 #line:257
                gui .log (f"Sent message {O00O00O0OOOO0OO00}/{num_messages}")#line:258
                OO0OO0OO0O00O0OO0 =WebDriverWait (O0OO00000O0000O00 ,5 ).until (EC .element_to_be_clickable ((By .CSS_SELECTOR ,"div[role='textbox'][class*='slateTextArea']")))#line:261
            except Exception as OOOOO00O0000OOO0O :#line:262
                gui .log (f"Error sending message {O00O00O0OOOO0OO00 + 1}: {OOOOO00O0000OOO0O}")#line:263
                handle_anti_spam (O0OO00000O0000O00 )#line:264
                OO0OO0OO0O00O0OO0 =WebDriverWait (O0OO00000O0000O00 ,5 ).until (EC .element_to_be_clickable ((By .CSS_SELECTOR ,"div[role='textbox'][class*='slateTextArea']")))#line:267
        if O00O00O0OOOO0OO00 <num_messages and gui .is_running :#line:268
            gui .log (f"Waiting {batch_delay} seconds before next batch...")#line:269
            time .sleep (batch_delay )#line:270
def show_login_window ():#line:272
    O0000OOOO00OOOOOO =tk .Tk ()#line:273
    O0000OOOO00OOOOOO .title ("Login")#line:274
    O0000OOOO00OOOOOO .geometry ("300x150")#line:275
    O0000OOOO00OOOOOO .configure (bg ="#2C2F33")#line:276
    O0000OOOO00OOOOOO .resizable (False ,False )#line:277
    O00OO0O0O000OO0OO =ttk .Frame (O0000OOOO00OOOOOO ,padding ="10")#line:280
    O00OO0O0O000OO0OO .grid (row =0 ,column =0 ,sticky ="nsew")#line:281
    ttk .Label (O00OO0O0O000OO0OO ,text ="Username:").grid (row =0 ,column =0 ,sticky ="w",pady =5 )#line:284
    O0O0OOOOO000O00OO =tk .StringVar ()#line:285
    OO00OO00OOOOO000O =ttk .Entry (O00OO0O0O000OO0OO ,textvariable =O0O0OOOOO000O00OO ,width =25 )#line:286
    OO00OO00OOOOO000O .grid (row =0 ,column =1 ,pady =5 )#line:287
    ttk .Label (O00OO0O0O000OO0OO ,text ="Password:").grid (row =1 ,column =0 ,sticky ="w",pady =5 )#line:290
    O0O0000O0OO00000O =tk .StringVar ()#line:291
    O000000O00O0O0O00 =ttk .Entry (O00OO0O0O000OO0OO ,textvariable =O0O0000O0OO00000O ,width =25 ,show ="*")#line:292
    O000000O00O0O0O00 .grid (row =1 ,column =1 ,pady =5 )#line:293
    def O0OOOOO000O00O0O0 ():#line:296
        OO0000OO0OOOO00O0 =fetch_credentials ()#line:297
        OO00OO0000OO0O0OO =O0O0OOOOO000O00OO .get ().strip ()#line:298
        OO0OOO000O0OO00OO =O0O0000O0OO00000O .get ().strip ()#line:299
        if OO00OO0000OO0O0OO in OO0000OO0OOOO00O0 and OO0000OO0OOOO00O0 [OO00OO0000OO0O0OO ]==OO0OOO000O0OO00OO :#line:300
            O0000OOOO00OOOOOO .destroy ()#line:301
            main ()#line:302
        else :#line:303
            messagebox .showerror ("Login Failed","Invalid username or password")#line:304
    ttk .Button (O00OO0O0O000OO0OO ,text ="Login",command =O0OOOOO000O00O0O0 ).grid (row =2 ,column =0 ,columnspan =2 ,pady =10 )#line:306
    O0000OOOO00OOOOOO .mainloop ()#line:308
def main ():#line:310
    global gui #line:311
    OOOO0O0OO0O0O000O =tk .Tk ()#line:312
    gui =DiscordBotGUI (OOOO0O0OO0O0O000O )#line:313
    OOOO0O0OO0O0O000O .mainloop ()#line:314
if __name__ =="__main__":#line:316
    show_login_window ()