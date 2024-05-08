from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.video import Video
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.audio import SoundLoader
from kivy.properties import ObjectProperty
import random

sm = ScreenManager()

class FirstWindow(Screen):
    pass
class SecondWindow(Screen):
    pass

class ThirdWindow(Screen):
   pass

class FourthWindow(Screen):
    pass

class FifthWindow(Screen):
    def on_button_click(self):
        text=self.ids.opt1.text

        if str(text)=='1' or str(text)=='one' or str(text)=='option 1' or str(text)=='Option 1' or str(text)=='option1':
            self.parent.current ='6'
            print("yo")
        elif str(text)=='2' or str(text)=='two' or str(text)=='option 2' or str(text)=='Option 2' or str(text)=='option2':
            self.parent.current = '8'
            print("yo")

class SixthWindow(Screen):
    pass

class SeventhWindow(Screen): #1.Emma\n\n2.Dr.Sinha\n\n3.Winston\n\n4.Alisha
    choice1=''
    def on_button_click(self):
        text=self.ids.opt2.text
        self.choice1 = text
        if str(text) == 'Emma' or str(text) == 'emma' or str(text) == '1':
            self.parent.current = '1211'
        elif str(text) == 'Dr.Sinha' or str(text) == 'Sinha' or str(text) == '2' or str(text) == 'dr.sinha' or str(text) =='dr':
            self.parent.current = '1231'
        elif str(text) == 'Winston' or str(text) == 'winston' or str(text) == '3':
            self.parent.current = '1221'
        elif str(text) == 'Alisha' or str(text) == 'alisha' or str(text) == '4':
            self.parent.current = '1241'



class EightWindow(Screen):
    def on_button_click(self):
        text=self.ids.opt3.text
        if str(text) == 'black' or str(text) == 'Black' or str(text) == '1'or str(text) == 'bla' or str(text) == 'Bla':
            self.parent.current = 'black'
        elif str(text) == 'white' or str(text) == 'White' or str(text) == '2' or str(text) == 'wh' or str(text) == 'Wh':
            self.parent.current = 'white'
        elif str(text) == 'blue' or str(text) == 'Blue' or str(text) == '3' or str(text) == 'Blu' or str(text) == 'blu':
            self.parent.current = '7'

class NinthWindow(Screen):
    pass

class TenthWindow(Screen):
    c=0
    def on_button_click(self):
        if self.c<5:
            text = self.ids.opt4.text
            no=9
            if int(text)==no or int(text) ==no:
                self.parent.current = '7'
                print("correct")

            else:
                self.parent.current = 'white'
                print("incorrect")
                self.c+=1
        else:
            self.parent.current = 'black'


#class EleventhWindow(Screen):
   # pass

class TwelthWindow11(Screen):
    pass

class TwelthWindow12(Screen):
    pass

class TwelthWindow13(Screen):
    f=1
    def on_button_click(self):
        if self.f <= 2:
            guess = self.ids.opt5.text
            if guess.lower()=='sherlock holmes' or guess.lower()=='Sherlock Holmes' or guess.lower()=='sherlock':
                self.parent.current = '1214'
            else:
                print('Something went wrong')

            self.f+= 1
        elif self.f==3:
            self.parent.current = '3rdchance'


class TwelthWindow14(Screen):
    def on_button_click(self):
        text = self.ids.opt6.text
        self.choice1 = text
        if str(text) == 'Dr.Sinha' or str(text) == 'Sinha' or str(text) == '2' or str(text) == 'dr.sinha' or str(text) == 'dr':
            self.parent.current = '1311'
        elif str(text) == 'Winston' or str(text) == 'winston' or str(text) == '3':
            self.parent.current = '1321'
        elif str(text) == 'Alisha' or str(text) == 'alisha' or str(text) == '4':
            self.parent.current = '1361'


class TwelthWindow15(Screen):
    def on_button_click(self):
        guess = self.ids.opt7.text
        if guess.lower() == 'sherlock holmes' or guess.lower() == 'Sherlock Holmes' or guess.lower() == 'sherlock':
            self.parent.current = '1214'
        else:
            self.parent.current='1216'

class TwelthWindow16(Screen):
    pass

class TwelthWindow21(Screen):
    pass

class TwelthWindow22(Screen):
    pass

class TwelthWindow23(Screen):
    def on_button_click(self):
        opt= self.ids.opt8.text
        if opt == '1' or opt == 'one' or opt == 'option 1':
            self.parent.current = '1224'
        else:
            self.parent.current = '1226'

class TwelthWindow24(Screen):
    def on_button_click(self):
        opt=self.ids.opt9.text
        if opt == '1' or opt == 'one' or opt == 'option 1':
            self.parent.current = '1227'
        else:
            self.parent.current = '1226'


class TwelthWindow26(Screen):
    g = 1
    def on_button_click(self):
        if self.g <= 2:
            guess = self.ids.opt10.text
            if guess.lower() == 'sherlock holmes' or guess.lower() == 'Sherlock Holmes' or guess.lower() == 'sherlock':
                self.parent.current = '1228'
            else:
                print('Something went wrong')

            self.g += 1
        elif self.g == 3:
            self.parent.current = '1229'

class TwelthWindow27(Screen):
    def on_button_click(self):
        text=self.ids.opt11.text
        self.choice1 = text
        if str(text) == 'Emma' or str(text) == 'emma' or str(text) == '1':
            self.parent.current = '1321'
        elif str(text) == 'sinha' or str(text) == 'Sinha' or str(text) == '2' or str(text) == 'dr.sinha' or str(text) =='dr':
            self.parent.current = '1331'
        elif str(text) == 'Alisha' or str(text) == 'alisha' or str(text) == '4':
            self.parent.current='1341'


class TwelthWindow28(Screen):
    def on_button_click(self):
        text=self.ids.opt12.text
        self.choice1 = text
        if str(text) == 'Emma' or str(text) == 'emma' or str(text) == '1':
            self.parent.current = '1321'
        elif str(text) == 'sinha' or str(text) == 'Sinha' or str(text) == '2' or str(text) == 'dr.sinha' or str(text) =='dr' or str(text)=='sinha':
            self.parent.current = '1331'
        elif str(text) == 'Alisha' or str(text) == 'alisha' or str(text) == '4':
            self.parent.current='1341'


class TwelthWindow29(Screen):
    def on_button_click(self):
        guess = self.ids.opt13.text
        if guess.lower() == 'sherlock holmes' or guess.lower() == 'Sherlock Holmes' or guess.lower() == 'sherlock':
            self.parent.current = '1228'
        else:
            self.parent.current='1216'

class TwelthWindow31(Screen):
    pass

class TwelthWindow32(Screen):
    pass

class TwelthWindow33(Screen):
    h = 1
    def on_button_click(self):
        if self.h <= 2:
            guess = self.ids.opt14.text
            if guess.lower() == 'sherlock holmes' or guess.lower() == 'Sherlock Holmes' or guess.lower() == 'sherlock':
                self.parent.current = '1235'
            else:
                print('Something went wrong')

            self.h += 1
        elif self.h == 3:
            self.parent.current = '1234'

class TwelthWindow34(Screen):
    def on_button_click(self):
        guess = self.ids.opt15.text
        if guess.lower() == 'sherlock holmes' or guess.lower() == 'Sherlock Holmes' or guess.lower() == 'sherlock':
            self.parent.current = '1235'
        else:
            self.parent.current='1216'

class TwelthWindow35(Screen):
    def on_button_click(self):
        text=self.ids.opt16.text
        self.choice1 = text
        if str(text) == 'Emma' or str(text) == 'emma' or str(text) == '1':
            self.parent.current = '1311'
        elif str(text) == 'Winston' or str(text) == 'winston' or str(text) == '3':
            self.parent.current = '1331'
        elif str(text) == 'Alisha' or str(text) == 'alisha' or str(text) == '4':
            self.parent.current='1351'

class TwelthWindow41(Screen):
    pass

class TwelthWindow42(Screen):
    pass
class TwelthWindow43(Screen):
    i = 0

    def on_button_click(self):
        if self.i < 2:
            guess = self.ids.opt17.text
            if guess.lower() == 'sherlock holmes' or guess.lower() == 'Sherlock Holmes' or guess.lower() == 'sherlock':
                self.parent.current = '1245'
            else:
                print('Something went wrong')
                self.i += 1
        else:
            self.parent.current = '1244'


class TwelthWindow44(Screen):
    def on_button_click(self):
        guess = self.ids.opt18.text
        if guess.lower() == 'sherlock holmes' or guess.lower() == 'Sherlock Holmes' or guess.lower() == 'sherlock':
            self.parent.current = '1245'
        else:
            self.parent.current='1216'

class TwelthWindow45(Screen):
    def on_button_click(self):
        text=self.ids.opt19.text
        self.choice1 = text
        if str(text) == 'Emma' or str(text) == 'emma' or str(text) == '1':
            self.parent.current = '1361'
        elif str(text) == 'sinha' or str(text) == 'Sinha' or str(text) == '2' or str(text) == 'dr.sinha' or str(text) =='dr':
            self.parent.current = '1351'
        elif str(text) == 'Winston' or str(text) == 'winston' or str(text) == '3':
            self.parent.current = '1341'

class ThirteenthWindow11(Screen):
    pass
class ThirteenthWindow12(Screen):
    pass
class ThirteenthWindow13(Screen):
    def on_button_click(self):
        text=self.ids.opt20.text
        if str(text) == 'husband' or str(text) == 'Husband' or str(text) == '1':
            self.parent.current = '1314'
        elif str(text) == 'Neighbour' or str(text) == 'neighbour' or str(text) == '2':
            self.parent.current = '1315'
        elif str(text) == 'Maid' or str(text) == 'maid' or str(text) == '3':
            self.parent.current = '1316'


class ThirteenthWindow14(Screen):
    def on_button_click(self):
        text=self.ids.opt21.text
        if str(text) == 'Yes' or str(text) == 'yes' or str(text) == 'y' or str(text) == 'Y':
            self.parent.current = '1313'
        elif str(text) == 'No' or str(text) == 'no' or str(text) == 'n' or str(text) == 'N':
            self.parent.current = '1317'
class ThirteenthWindow15(Screen):
    def on_button_click(self):
        text=self.ids.opt22.text
        if str(text) == 'Yes' or str(text) == 'yes' or str(text) == 'y' or str(text) == 'Y':
            self.parent.current = '1313'
        elif str(text) == 'No' or str(text) == 'no' or str(text) == 'n' or str(text) == 'N':
            self.parent.current = '1317'

class ThirteenthWindow16(Screen):
    def on_button_click(self):
        text=self.ids.opt23.text
        if str(text) == 'Yes' or str(text) == 'yes' or str(text) == 'y' or str(text) == 'Y':
            self.parent.current = '1313'
        elif str(text) == 'No' or str(text) == 'no' or str(text) == 'n' or str(text) == 'N':
            self.parent.current = '1317'
class ThirteenthWindow17(Screen):
    x=0
    def on_button_click(self):
        text=self.ids.opt24.text
        if self.x<2:
            if str(text) == 'husband' or str(text) == 'Husband':
                self.parent.current = '1318'
                self.x+=1
            else:
                self.parent.current = '1317'
                self.x += 1
        else:
                self.parent.current='1319'
class ThirteenthWindow18(Screen):
    def on_button_click(self):
        text=self.ids.opt25.text
        if str(text) == 'Alisha' or str(text) == 'alisha' or str(text) == '1':
            self.parent.current = 'winston'
        elif str(text) == 'Winston' or str(text) == 'winston' or str(text) == '2':
            self.parent.current = 'alisha1'
class ThirteenthWindow19(Screen):
    pass
class ThirteenthWindow21(Screen):
    pass
class ThirteenthWindow22(Screen):
    pass
class ThirteenthWindow23(Screen):
    def on_button_click(self):
        text=self.ids.opt26.text
        if str(text) == 'husband' or str(text) == 'Husband' or str(text) == '1':
            self.parent.current = '1324'
        elif str(text) == 'Neighbour' or str(text) == 'neighbour' or str(text) == '2':
            self.parent.current = '1325'
        elif str(text) == 'Maid' or str(text) == 'maid' or str(text) == '3':
            self.parent.current = '1326'
class ThirteenthWindow24(Screen):
    def on_button_click(self):
        text=self.ids.opt27.text
        if str(text) == 'Yes' or str(text) == 'yes' or str(text) == 'y' or str(text) == 'Y':
            self.parent.current = '1323'
        elif str(text) == 'No' or str(text) == 'no' or str(text) == 'n' or str(text) == 'N':
            self.parent.current = '1327'
class ThirteenthWindow25(Screen):
    def on_button_click(self):
        text=self.ids.opt28.text
        if str(text) == 'Yes' or str(text) == 'yes' or str(text) == 'y' or str(text) == 'Y':
            self.parent.current = '1323'
        elif str(text) == 'No' or str(text) == 'no' or str(text) == 'n' or str(text) == 'N':
            self.parent.current = '1327'
class ThirteenthWindow26(Screen):
    def on_button_click(self):
        text=self.ids.opt29.text
        if str(text) == 'Yes' or str(text) == 'yes' or str(text) == 'y' or str(text) == 'Y':
            self.parent.current = '1323'
        elif str(text) == 'No' or str(text) == 'no' or str(text) == 'n' or str(text) == 'N':
            self.parent.current = '1327'
class ThirteenthWindow27(Screen):
    y = 0
    def on_button_click(self):
        text = self.ids.opt30.text
        if self.y < 2:
            if str(text) == 'husband' or str(text) == 'Husband':
                self.parent.current = '1328'
                self.y+=1
            else:
                self.parent.current = '1327'
                self.y+=1

        else:
            self.parent.current = '1329'

class ThirteenthWindow28(Screen): #id31
    def on_button_click(self):
        text=self.ids.opt31.text
        if str(text) == 'Alisha' or str(text) == 'alisha' or str(text) == '1':
            self.parent.current = 'Sinha'
        elif str(text) == 'Dr.Sinha' or str(text) == 'sinha' or str(text) == '1' or str(text) == 'dr sinha' or str(text) == 'dr':
            self.parent.current = 'alisha1'
class ThirteenthWindow29(Screen):
    pass
class ThirteenthWindow31(Screen):
    pass
class ThirteenthWindow32(Screen):
    pass
class ThirteenthWindow33(Screen):
    def on_button_click(self):
        text=self.ids.opt32.text
        if str(text) == 'husband' or str(text) == 'Husband' or str(text) == '1':
            self.parent.current = '1334'
        elif str(text) == 'Neighbour' or str(text) == 'neighbour' or str(text) == '2':
            self.parent.current = '1335'
        elif str(text) == 'Maid' or str(text) == 'maid' or str(text) == '3':
            self.parent.current = '1336'
class ThirteenthWindow34(Screen):
    def on_button_click(self):
        text=self.ids.opt33.text
        if str(text) == 'Yes' or str(text) == 'yes' or str(text) == 'y' or str(text) == 'Y':
            self.parent.current = '1333'
        elif str(text) == 'No' or str(text) == 'no' or str(text) == 'n' or str(text) == 'N':
            self.parent.current = '1337'
class ThirteenthWindow35(Screen):
    def on_button_click(self):
        text=self.ids.opt34.text
        if str(text) == 'Yes' or str(text) == 'yes' or str(text) == 'y' or str(text) == 'Y':
            self.parent.current = '1333'
        elif str(text) == 'No' or str(text) == 'no' or str(text) == 'n' or str(text) == 'N':
            self.parent.current = '1337'
class ThirteenthWindow36(Screen):
    def on_button_click(self):
        text=self.ids.opt35.text
        if str(text) == 'Yes' or str(text) == 'yes' or str(text) == 'y' or str(text) == 'Y':
            self.parent.current = '1333'
        elif str(text) == 'No' or str(text) == 'no' or str(text) == 'n' or str(text) == 'N':
            self.parent.current = '1337'
class ThirteenthWindow37(Screen):
    z = 0
    def on_button_click(self):
        text = self.ids.opt36.text
        if self.z < 2:
            if str(text) == 'husband' or str(text) == 'Husband':
                self.parent.current = '1338'
                self.z+=1
            else:
                self.z+=1
                self.parent.current = '1337'
        else:
                self.parent.current = '1339'

class ThirteenthWindow38(Screen):#id37
    def on_button_click(self):
        text=self.ids.opt37.text
        if str(text) == 'Alisha' or str(text) == 'alisha' or str(text) == '1':
            self.parent.current = 'emma'
        elif str(text) == 'emma' or str(text) == 'Emma' or str(text) == '2':
            self.parent.current = 'alisha1'

class ThirteenthWindow39(Screen):
    pass
class ThirteenthWindow41(Screen):
    pass
class ThirteenthWindow42(Screen):
    pass
class ThirteenthWindow43(Screen):
    def on_button_click(self):
        text=self.ids.opt38.text
        if str(text) == 'husband' or str(text) == 'Husband' or str(text) == '1':
            self.parent.current = '1344'
        elif str(text) == 'Neighbour' or str(text) == 'neighbour' or str(text) == '2':
            self.parent.current = '1345'
        elif str(text) == 'Maid' or str(text) == 'maid' or str(text) == '3':
            self.parent.current = '1346'
class ThirteenthWindow44(Screen):
    def on_button_click(self):
        text=self.ids.opt39.text
        if str(text) == 'Yes' or str(text) == 'yes' or str(text) == 'y' or str(text) == 'Y':
            self.parent.current = '1343'
        elif str(text) == 'No' or str(text) == 'no' or str(text) == 'n' or str(text) == 'N':
            self.parent.current = '1347'
class ThirteenthWindow45(Screen):
    def on_button_click(self):
        text=self.ids.opt40.text
        if str(text) == 'Yes' or str(text) == 'yes' or str(text) == 'y' or str(text) == 'Y':
            self.parent.current = '1343'
        elif str(text) == 'No' or str(text) == 'no' or str(text) == 'n' or str(text) == 'N':
            self.parent.current = '1347'
class ThirteenthWindow46(Screen):
    def on_button_click(self):
        text=self.ids.opt41.text
        if str(text) == 'Yes' or str(text) == 'yes' or str(text) == 'y' or str(text) == 'Y':
            self.parent.current = '1343'
        elif str(text) == 'No' or str(text) == 'no' or str(text) == 'n' or str(text) == 'N':
            self.parent.current = '1347'
class ThirteenthWindow47(Screen):
    m = 0
    def on_button_click(self):
        print("click")
        text = self.ids.opt42.text
        if self.m < 2:
            if str(text) == 'husband' or str(text) == 'Husband':
                self.parent.current = '1348'
                self.m+=1
            else:
                self.parent.current='1347'
                self.m += 1
        else:
                self.parent.current = '1349'

class ThirteenthWindow48(Screen):#id43
    def on_button_click(self):
        text=self.ids.opt43.text
        if str(text) == 'emma' or str(text) == 'Emma' or str(text) == '1':
            self.parent.current = 'Sinha'
        elif str(text) == 'Dr.Sinha' or str(text) == 'sinha' or str(text) == '1' or str(text) == 'dr sinha' or str(text) == 'dr':
            self.parent.current = 'emma'

class ThirteenthWindow49(Screen):
    pass
class ThirteenthWindow51(Screen):
    pass
class ThirteenthWindow52(Screen):
    pass
class ThirteenthWindow53(Screen):
    def on_button_click(self):
        text=self.ids.opt44.text
        if str(text) == 'husband' or str(text) == 'Husband' or str(text) == '1':
            self.parent.current = '1354'
        elif str(text) == 'Neighbour' or str(text) == 'neighbour' or str(text) == '2':
            self.parent.current = '1355'
        elif str(text) == 'Maid' or str(text) == 'maid' or str(text) == '3':
            self.parent.current = '1356'
class ThirteenthWindow54(Screen):
    def on_button_click(self):
        text=self.ids.opt45.text
        if str(text) == 'Yes' or str(text) == 'yes' or str(text) == 'y' or str(text) == 'Y':
            self.parent.current = '1353'
        elif str(text) == 'No' or str(text) == 'no' or str(text) == 'n' or str(text) == 'N':
            self.parent.current = '1357'
class ThirteenthWindow55(Screen):
    def on_button_click(self):
        text=self.ids.opt46.text
        if str(text) == 'Yes' or str(text) == 'yes' or str(text) == 'y' or str(text) == 'Y':
            self.parent.current = '1353'
        elif str(text) == 'No' or str(text) == 'no' or str(text) == 'n' or str(text) == 'N':
            self.parent.current = '1357'
class ThirteenthWindow56(Screen):
    def on_button_click(self):
        text=self.ids.opt47.text
        if str(text) == 'Yes' or str(text) == 'yes' or str(text) == 'y' or str(text) == 'Y':
            self.parent.current = '1353'
        elif str(text) == 'No' or str(text) == 'no' or str(text) == 'n' or str(text) == 'N':
            self.parent.current = '1357'
class ThirteenthWindow57(Screen):
    n = 0
    def on_button_click(self):
        text = self.ids.opt48.text
        if self.n < 2:
            if str(text) == 'husband' or str(text) == 'Husband':
                self.parent.current = '1358'
            else:
                self.n+=1
                self.parent.current = '1357'
        else:
                self.parent.current = '1359'

class ThirteenthWindow58(Screen):#49
    def on_button_click(self):
        text=self.ids.opt49.text
        if str(text) == 'Emma' or str(text) == 'emma' or str(text) == '1':
            self.parent.current = 'winston'
        elif str(text) == 'winston' or str(text) == 'Winston' or str(text) == '2':
            self.parent.current = 'emma'
class ThirteenthWindow59(Screen):
    pass
class ThirteenthWindow61(Screen):
    pass
class ThirteenthWindow62(Screen):
    pass
class ThirteenthWindow63(Screen):
    def on_button_click(self):
        text=self.ids.opt50.text
        if str(text) == 'husband' or str(text) == 'Husband' or str(text) == '1':
            self.parent.current = '1364'
        elif str(text) == 'Neighbour' or str(text) == 'neighbour' or str(text) == '2':
            self.parent.current = '1365'
        elif str(text) == 'Maid' or str(text) == 'maid' or str(text) == '3':
            self.parent.current = '1366'
class ThirteenthWindow64(Screen):
    def on_button_click(self):
        text=self.ids.opt51.text
        if str(text) == 'Yes' or str(text) == 'yes' or str(text) == 'y' or str(text) == 'Y':
            self.parent.current = '1363'
        elif str(text) == 'No' or str(text) == 'no' or str(text) == 'n' or str(text) == 'N':
            self.parent.current = '1367'
class ThirteenthWindow65(Screen):
    def on_button_click(self):
        text=self.ids.opt52.text
        if str(text) == 'Yes' or str(text) == 'yes' or str(text) == 'y' or str(text) == 'Y':
            self.parent.current = '1363'
        elif str(text) == 'No' or str(text) == 'no' or str(text) == 'n' or str(text) == 'N':
            self.parent.current = '1367'
class ThirteenthWindow66(Screen):
    def on_button_click(self):
        text=self.ids.opt53.text
        if str(text) == 'Yes' or str(text) == 'yes' or str(text) == 'y' or str(text) == 'Y':
            self.parent.current = '1363'
        elif str(text) == 'No' or str(text) == 'no' or str(text) == 'n' or str(text) == 'N':
            self.parent.current = '1367'
class ThirteenthWindow67(Screen):
    l = 0
    def on_button_click(self):
        text = self.ids.opt54.text
        if self.l< 2:
            if str(text) == 'husband' or str(text) == 'Husband':
                self.parent.current = '1368'
            else:
                self.parent.current = '1367'
                self.l+=1
        else:
                self.parent.current = '1369'

class ThirteenthWindow68(Screen):
    def on_button_click(self):
        text=self.ids.opt55.text
        if str(text) == 'Dr.Sinha' or str(text) == 'sinha' or str(text) == '1' or str(text) == 'dr sinha' or str(text) == 'dr':
            self.parent.current = 'winston'
        elif str(text) == 'winston' or str(text) == 'Winston' or str(text) == '2':
            self.parent.current = 'Sinha'
class ThirteenthWindow69(Screen):#49
    pass

class FourteenthWindow11(Screen):
    def on_button_click(self):
        text=self.ids.opt56.text
        if str(text) == '1' or str(text) == 'one' or str(text) == 'option 1' or str(text) == 'option1':
            self.parent.current = 'alisha2'
        elif str(text) == '2' or str(text) == 'two' or str(text) == 'option 2' or str(text) == 'option2':
            self.parent.current = 'alisha3'

class FourteenthWindow12(Screen):
    pass
class FourteenthWindow13(Screen):
    def on_button_click(self):
        text=self.ids.opt57.text
        if str(text) == '1' or str(text) == 'one' or str(text) == 'option 1' or str(text) == 'option1':
            self.parent.current = 'alisha4'
        elif str(text) == '2' or str(text) == 'two' or str(text) == 'option 2' or str(text) == 'option2':
            self.parent.current = 'alisha5'
class FourteenthWindow14(Screen):
    pass
class FourteenthWindow15(Screen):
    def on_button_click(self):
        text=self.ids.opt58.text
        if str(text) == '1' or str(text) == 'one' or str(text) == 'option 1' or str(text) == 'option1':
            self.parent.current = 'alisha6'
        elif str(text) == '2' or str(text) == 'two' or str(text) == 'option 2' or str(text) == 'option2':
            self.parent.current = 'alisha7'
class FourteenthWindow16(Screen):
    pass
class FourteenthWindow17(Screen):
    pass
class FourteenthWindow2(Screen):
    pass
class FourteenthWindow3(Screen):
    pass
class FourteenthWindow4(Screen):
    pass

class WindowManager(ScreenManager):
    pass

class Glitch(App):
    #def build(self):
       # global sm
       # return sm
    pass

Glitch().run()
