import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os.path
import pickle
import platform

class Player:
	def __init__(self, name, bets):
		self.__name = name
		self.__bets = bets

	@property
	def name(self):
		return self.__name

	@property
	def bets(self):
		return self.__bets

	def getPlayerBets(self):
		str = self.__name.upper() + ": \n"
		str += self.__bets.getBets()
		return str

class Bets:
	def __init__(self, costume, makeup, sound, score, song, adaptScreen, origiScreen, prodDesign, supActress, supActor, edit, cinematography, vfx, direct, international, animation, actor, actress, movie):
		self.__costume = costume
		self.__makeup = makeup
		self.__sound = sound
		self.__score = score
		self.__song = song
		self.__adaptScreen = adaptScreen
		self.__origiScreen = origiScreen
		self.__prodDesign = prodDesign
		self.__supActress = supActress
		self.__supActor = supActor
		self.__edit = edit
		self.__cinematography = cinematography
		self.__vfx = vfx
		self.__direct = direct
		self.__international = international
		self.__animation = animation
		self.__actor = actor
		self.__actress = actress
		self.__movie = movie
		
	@property
	def costume(self):
		return self.__costume

	@property
	def makeup(self):
		return self.__makeup

	@property
	def sound(self):
		return self.__sound

	@property
	def score(self):
		return self.__score

	@property
	def song(self):
		return self.__song

	@property
	def adaptScreen(self):
		return self.__adaptScreen

	@property
	def origiScreen(self):
		return self.__origiScreen

	@property
	def prodDesign(self):
		return self.__prodDesign

	@property
	def supActress(self):
		return self.__supActress

	@property
	def supActor(self):
		return self.__supActor

	@property
	def edit(self):
		return self.__edit

	@property
	def cinematography(self):
		return self.__cinematography

	@property
	def vfx(self):
		return self.__vfx
		
	@property
	def direct(self):
		return self.__direct

	@property
	def international(self):
		return self.__international

	@property
	def animation(self):
		return self.__animation

	@property
	def actor(self):
		return self.__actor

	@property
	def actress(self):
		return self.__actress

	@property
	def movie(self):
		return self.__movie

	def getBets(self):
		str = "\nCOSTUME DESIGN: " + self.__costume
		str += "\nMAKEUP AND HAIRSTYLING: " + self.__makeup
		str += "\nSOUND: " + self.__sound
		str += "\nORIGINAL SCORE: " + self.__score
		str += "\nORIGINAL SONG: " + self.__song
		str += "\nPRODUCTION DESIGN: " + self.__prodDesign
		str += "\nADAPTED SCREENPLAY: " + self.__adaptScreen
		str += "\nORIGINAL SCREENPLAY: " + self.__origiScreen
		str += "\nACTRESS IN A SUPPORTING ROLE: " + self.__supActress
		str += "\nACTOR IN A SUPPORTING ROLE: " + self.__supActor
		str += "\nFILM EDITING: " + self.__edit
		str += "\nCINEMATOGRAPHY: " + self.__cinematography
		str += "\nVISUAL EFFECTS: " + self.__vfx
		str += "\nDIRECTING: " + self.__direct
		str += "\nINTERNATIONAL FEATURE FILM: " + self.__international
		str += "\nANIMATED FEATURE FILM: " + self.__animation
		str += "\nACTRESS IN A LEADING ROLE: " + self.__actress
		str += "\nACTOR IN A LEADING ROLE: " + self.__actor
		str += "\nBEST PICTURE: " + self.__movie

		return str

class ViewNominees(tk.Toplevel):
	def __init__(self, control, nominees):
		#GENERAL
		tk.Toplevel.__init__(self)
		self.geometry('350x250')

		width = self.winfo_screenwidth()	#User's window size
		height = self.winfo_screenheight()
		
		if platform.system() == 'Windows':	#Using Replit, it doesn't fullscreen the window
			self.state('zoomed')	#Fullscreen window
		else:
			self.geometry('%dx%d' % (width, height))	#Window screen's sized
		
		self.title("Oscar 2023 Nominees")
		self.ctrl = control

		#INFOS
		self.frameInfo = tk.Frame(self)
		self.frameInfo.pack()
		self.textInfo = tk.Text(self.frameInfo, height=int((height/7)-(height/7)*0.61), width=int((width/7)-4))	#Adequate to the window size
		self.textInfo.pack()
		self.textInfo.config(state=tk.DISABLED)

		self.textInfo.config(state='normal')
		self.textInfo.delete('1.0', tk.END)
		self.textInfo.insert(1.0, nominees)
		self.textInfo.config(state='disable')

		#BUTTON
		self.frameButton = tk.Frame(self)
		self.frameButton.pack()

		self.buttonClose = tk.Button(self.frameButton, text="OK")
		self.buttonClose.pack(side="left")
		self.buttonClose.bind("<Button>", control.closeHandler)

class ViewCreateBet(tk.Toplevel):
	def __init__(self, control, nomineesList):
		#GENERAL
		tk.Toplevel.__init__(self)

		width = self.winfo_screenwidth()	#User's window size
		height = self.winfo_screenheight()

		if platform.system() == 'Windows':	#Using Replit, it doesn't fullscreen the window
			self.state('zoomed')	#Fullscreen window
		else:
			self.geometry('%dx%d' % (width, height))	#Window screen's sized
			
		self.title("Create a Bet")
		self.ctrl = control

		#SETTINGS
		font_size = 6
		
		#NAME
		self.frameName = tk.Frame(self)
		self.frameName.pack()
		self.labelName = tk.Label(self.frameName, text="Player Name: ", font=("Arial Black Bold", font_size))
		self.labelName.pack(side="left")
		self.inputName = tk.Entry(self.frameName, width=25, font=("Arial Black Bold", font_size))
		self.inputName.pack(side="left")

		#COMBOBOXES
		#Makeup and Hairstyling
		self.frameCombo = tk.Frame(self)
		self.frameCombo.pack()

		self.labelMakeups = tk.Label(self.frameCombo, text="Makeup and Hairstyling:", font=("Arial Black Bold", font_size))
		self.labelMakeups.pack(side="top")
		self.chooseMakeup = tk.StringVar()
		self.comboboxMakeup = ttk.Combobox(self.frameCombo, width=35, values=nomineesList[1], textvariable=self.chooseMakeup, font=("Arial Black Bold", font_size))
		self.comboboxMakeup.set("Select nominee")
		self.comboboxMakeup.pack(side="left")

		#Production Design
		self.frameCombo = tk.Frame(self)
		self.frameCombo.pack()

		self.labelProdDesigns = tk.Label(self.frameCombo, text="Production Design:", font=("Arial Black Bold", font_size))
		self.labelProdDesigns.pack(side="top")
		self.chooseProdDesign = tk.StringVar()
		self.comboboxProdDesign = ttk.Combobox(self.frameCombo, width=35, values=nomineesList[7], textvariable=self.chooseProdDesign, font=("Arial Black Bold", font_size))
		self.comboboxProdDesign.set("Select nominee")
		self.comboboxProdDesign.pack(side="left")

		#Sound
		self.frameCombo = tk.Frame(self)
		self.frameCombo.pack()

		self.labelSounds = tk.Label(self.frameCombo, text="Sound:", font=("Arial Black Bold", font_size))
		self.labelSounds.pack(side="top")
		self.chooseSound = tk.StringVar()
		self.comboboxSound = ttk.Combobox(self.frameCombo, width=35, values=nomineesList[2], textvariable=self.chooseSound, font=("Arial Black Bold", font_size))
		self.comboboxSound.set("Select nominee")
		self.comboboxSound.pack(side="left")

		#Original Song
		self.frameCombo = tk.Frame(self)
		self.frameCombo.pack()

		self.labelSongs = tk.Label(self.frameCombo, text="Original Song:", font=("Arial Black Bold", font_size))
		self.labelSongs.pack(side="top")
		self.chooseSong = tk.StringVar()
		self.comboboxSong = ttk.Combobox(self.frameCombo, width=35, values=nomineesList[4], textvariable=self.chooseSong, font=("Arial Black Bold", font_size))
		self.comboboxSong.set("Select nominee")
		self.comboboxSong.pack(side="left")

		#Score
		self.frameCombo = tk.Frame(self)
		self.frameCombo.pack()

		self.labelScores = tk.Label(self.frameCombo, text="Original Score:", font=("Arial Black Bold", font_size))
		self.labelScores.pack(side="top")
		self.chooseScore = tk.StringVar()
		self.comboboxScore = ttk.Combobox(self.frameCombo, width=35, values=nomineesList[3], textvariable=self.chooseScore, font=("Arial Black Bold", font_size))
		self.comboboxScore.set("Select nominee")
		self.comboboxScore.pack(side="left")

		#Costume Design
		self.frameCombo = tk.Frame(self)
		self.frameCombo.pack()

		self.labelCostumes = tk.Label(self.frameCombo, text="Costume Design:", font=("Arial Black Bold", font_size))
		self.labelCostumes.pack(side="top")
		self.chooseCostume = tk.StringVar()
		self.comboboxCostume = ttk.Combobox(self.frameCombo, width=35, values=nomineesList[0],  textvariable=self.chooseCostume, font=("Arial Black Bold", font_size))
		self.comboboxCostume.set("Select nominee")
		self.comboboxCostume.pack(side="left")

		#Adapted Screenplay
		self.frameCombo = tk.Frame(self)
		self.frameCombo.pack()

		self.labelAdaptScreens = tk.Label(self.frameCombo, text="Adapted Screenplay:", font=("Arial Black Bold", font_size))
		self.labelAdaptScreens.pack(side="top")
		self.chooseAdaptScreen = tk.StringVar()
		self.comboboxAdaptScreen = ttk.Combobox(self.frameCombo, width=35, values=nomineesList[5], textvariable=self.chooseAdaptScreen, font=("Arial Black Bold", font_size))
		self.comboboxAdaptScreen.set("Select nominee")
		self.comboboxAdaptScreen.pack(side="left")

		#Original Screenplay
		self.frameCombo = tk.Frame(self)
		self.frameCombo.pack()

		self.labelOrigiScreens = tk.Label(self.frameCombo, text="Original Screenplay:", font=("Arial Black Bold", font_size))
		self.labelOrigiScreens.pack(side="top")
		self.chooseOrigiScreen = tk.StringVar()
		self.comboboxOrigiScreen = ttk.Combobox(self.frameCombo, width=35, values=nomineesList[6], textvariable=self.chooseOrigiScreen, font=("Arial Black Bold", font_size))
		self.comboboxOrigiScreen.set("Select nominee")
		self.comboboxOrigiScreen.pack(side="left")

		#Actress in a Supporting Role
		self.frameCombo = tk.Frame(self)
		self.frameCombo.pack()

		self.labelSupActresses = tk.Label(self.frameCombo, text="Actress in a Supporting Role:", font=("Arial Black Bold", font_size))
		self.labelSupActresses.pack(side="top")
		self.chooseSupActress = tk.StringVar()
		self.comboboxSupActress = ttk.Combobox(self.frameCombo, width=35, values=nomineesList[8], textvariable=self.chooseSupActress, font=("Arial Black Bold", font_size))
		self.comboboxSupActress.set("Select nominee")
		self.comboboxSupActress.pack(side="left")

		#Actor in a Supporting Role
		self.frameCombo = tk.Frame(self)
		self.frameCombo.pack()

		self.labelSupActors = tk.Label(self.frameCombo, text="Actor in a Supporting Role:", font=("Arial Black Bold", font_size))
		self.labelSupActors.pack(side="top")
		self.chooseSupActor = tk.StringVar()
		self.comboboxSupActor = ttk.Combobox(self.frameCombo, width=35, values=nomineesList[9], textvariable=self.chooseSupActor, font=("Arial Black Bold", font_size))
		self.comboboxSupActor.set("Select nominee")
		self.comboboxSupActor.pack(side="left")

		#Film Editing
		self.frameCombo = tk.Frame(self)
		self.frameCombo.pack()

		self.labelEdits = tk.Label(self.frameCombo, text="Film Editing:", font=("Arial Black Bold", font_size))
		self.labelEdits.pack(side="top")
		self.chooseEdit = tk.StringVar()
		self.comboboxEdit = ttk.Combobox(self.frameCombo, width=35, values=nomineesList[10], textvariable=self.chooseEdit, font=("Arial Black Bold", font_size))
		self.comboboxEdit.set("Select nominee")
		self.comboboxEdit.pack(side="left")

		#Cinematography
		self.frameCombo = tk.Frame(self)
		self.frameCombo.pack()

		self.labelCinematographies = tk.Label(self.frameCombo, text="Cinematography:", font=("Arial Black Bold", font_size))
		self.labelCinematographies.pack(side="top")
		self.chooseCinematography = tk.StringVar()
		self.comboboxCinematography = ttk.Combobox(self.frameCombo, width=35, values=nomineesList[11], textvariable=self.chooseCinematography, font=("Arial Black Bold", font_size))
		self.comboboxCinematography.set("Select nominee")
		self.comboboxCinematography.pack(side="left")

		#Visual Effects
		self.frameCombo = tk.Frame(self)
		self.frameCombo.pack()

		self.labelVfxes = tk.Label(self.frameCombo, text="Visual Effects:", font=("Arial Black Bold", font_size))
		self.labelVfxes.pack(side="top")
		self.chooseVfx = tk.StringVar()
		self.comboboxVfx = ttk.Combobox(self.frameCombo, width=35, values=nomineesList[12], textvariable=self.chooseVfx, font=("Arial Black Bold", font_size))
		self.comboboxVfx.set("Select nominee")
		self.comboboxVfx.pack(side="left")

		#International Feature Film
		self.frameCombo = tk.Frame(self)
		self.frameCombo.pack()

		self.labelInternationals = tk.Label(self.frameCombo, text="International Feature Film:", font=("Arial Black Bold", font_size))
		self.labelInternationals.pack(side="top")
		self.chooseInternational = tk.StringVar()
		self.comboboxInternational = ttk.Combobox(self.frameCombo, width=35, values=nomineesList[14], textvariable=self.chooseInternational, font=("Arial Black Bold", font_size))
		self.comboboxInternational.set("Select nominee")
		self.comboboxInternational.pack(side="left")

		#Directing
		self.frameCombo = tk.Frame(self)
		self.frameCombo.pack()

		self.labelDirects = tk.Label(self.frameCombo, text="Directing:", font=("Arial Black Bold", font_size))
		self.labelDirects.pack(side="top")
		self.chooseDirect = tk.StringVar()
		self.comboboxDirect = ttk.Combobox(self.frameCombo, width=35, values=nomineesList[13], textvariable=self.chooseDirect, font=("Arial Black Bold", font_size))
		self.comboboxDirect.set("Select nominee")
		self.comboboxDirect.pack(side="left")

		#Animated Feature Film
		self.frameCombo = tk.Frame(self)
		self.frameCombo.pack()

		self.labelAnimations = tk.Label(self.frameCombo, text="Animated Feature Film:", font=("Arial Black Bold", font_size))
		self.labelAnimations.pack(side="top")
		self.chooseAnimation = tk.StringVar()
		self.comboboxAnimation = ttk.Combobox(self.frameCombo, width=35, values=nomineesList[15], textvariable=self.chooseAnimation, font=("Arial Black Bold", font_size))
		self.comboboxAnimation.set("Select nominee")
		self.comboboxAnimation.pack(side="left")

		#Actress in a Leading Role
		self.frameCombo = tk.Frame(self)
		self.frameCombo.pack()

		self.labelActresses = tk.Label(self.frameCombo, text="Actress in a Leading Role:", font=("Arial Black Bold", font_size))
		self.labelActresses.pack(side="top")
		self.chooseActress = tk.StringVar()
		self.comboboxActress = ttk.Combobox(self.frameCombo, width=35, values=nomineesList[16], textvariable=self.chooseActress, font=("Arial Black Bold", font_size))
		self.comboboxActress.set("Select nominee")
		self.comboboxActress.pack(side="left")

		#Actor in a Leading Role
		self.frameCombo = tk.Frame(self)
		self.frameCombo.pack()

		self.labelActors = tk.Label(self.frameCombo, text="Actor in a Leading Role:", font=("Arial Black Bold", font_size))
		self.labelActors.pack(side="top")
		self.chooseActor = tk.StringVar()
		self.comboboxActor = ttk.Combobox(self.frameCombo, width=35, values=nomineesList[17], textvariable=self.chooseActor, font=("Arial Black Bold", font_size))
		self.comboboxActor.set("Select nominee")
		self.comboboxActor.pack(side="left")

		#Best Picture
		self.frameCombo = tk.Frame(self)
		self.frameCombo.pack()

		self.labelMovies = tk.Label(self.frameCombo, text="Best Picture:", font=("Arial Black Bold", font_size))
		self.labelMovies.pack(side="top")
		self.chooseMovie = tk.StringVar()
		self.comboboxMovie = ttk.Combobox(self.frameCombo, width=35, values=nomineesList[18], textvariable=self.chooseMovie, font=("Arial Black Bold", font_size))
		self.comboboxMovie.set("Select nominee")
		self.comboboxMovie.pack(side="left")

		#BUTTONS
		self.frameButton = tk.Frame(self)
		self.frameButton.pack()

		self.buttonEnter = tk.Button(self.frameButton, text="Enter")
		self.buttonEnter.pack(side="left")
		self.buttonEnter.bind("<Button>", control.enterHandler)

		self.buttonCancel = tk.Button(self.frameButton, text="Cancel")
		self.buttonCancel.pack(side="left")
		self.buttonCancel.bind("<Button>", control.closeHandler)

	def showWindow(self, title, msg):
		messagebox.showinfo(title, msg)

class ViewData(tk.Toplevel):
	def __init__(self, control, info):
		#GENERAL
		tk.Toplevel.__init__(self)
		self.geometry('350x250')

		width = self.winfo_screenwidth()	#User's window size
		height = self.winfo_screenheight()
		
		if platform.system() == 'Windows':	#Using Replit, it doesn't fullscreen the window
			self.state('zoomed')	#Fullscreen window
		else:
			self.geometry('%dx%d' % (width, height))	#Window screen's sized
		
		self.title("Oscar 2023 Nominees")
		self.ctrl = control

		#INFOS
		self.frameInfo = tk.Frame(self)
		self.frameInfo.pack()
		self.textInfo = tk.Text(self.frameInfo, height=int((height/7)-(height/7)*0.61), width=int((width/7)-4))	#Adequate to the window size
		self.textInfo.pack()
		self.textInfo.config(state=tk.DISABLED)

		self.textInfo.config(state='normal')
		self.textInfo.delete('1.0', tk.END)
		self.textInfo.insert(1.0, info)
		self.textInfo.config(state='disable')

		#BUTTON
		self.frameButton = tk.Frame(self)
		self.frameButton.pack()

		self.buttonClose = tk.Button(self.frameButton, text="OK")
		self.buttonClose.pack(side="left")
		self.buttonClose.bind("<Button>", control.closeHandler)

class ViewRegisterWinners(tk.Toplevel):
	def __init__(self, control, nomineesList):
		#GENERAL
		tk.Toplevel.__init__(self)

		width = self.winfo_screenwidth()	#User's window size
		height = self.winfo_screenheight()

		if platform.system() == 'Windows':	#Using Replit, it doesn't fullscreen the window
			self.state('zoomed')	#Fullscreen window
		else:
			self.geometry('%dx%d' % (width, height))	#Window screen's sized
			
		self.title("Create a Bet")
		self.ctrl = control

		#SETTINGS
		font_size = 6

		#COMBOBOXES
		#Makeup and Hairstyling
		self.frameCombo = tk.Frame(self)
		self.frameCombo.pack()

		self.labelMakeups = tk.Label(self.frameCombo, text="Makeup and Hairstyling:", font=("Arial Black Bold", font_size))
		self.labelMakeups.pack(side="top")
		self.chooseMakeup = tk.StringVar()
		self.comboboxMakeup = ttk.Combobox(self.frameCombo, width=35, values=nomineesList[1], textvariable=self.chooseMakeup, font=("Arial Black Bold", font_size))
		self.comboboxMakeup.set("Select nominee")
		self.comboboxMakeup.pack(side="left")

		#Production Design
		self.frameCombo = tk.Frame(self)
		self.frameCombo.pack()

		self.labelProdDesigns = tk.Label(self.frameCombo, text="Production Design:", font=("Arial Black Bold", font_size))
		self.labelProdDesigns.pack(side="top")
		self.chooseProdDesign = tk.StringVar()
		self.comboboxProdDesign = ttk.Combobox(self.frameCombo, width=35, values=nomineesList[7], textvariable=self.chooseProdDesign, font=("Arial Black Bold", font_size))
		self.comboboxProdDesign.set("Select nominee")
		self.comboboxProdDesign.pack(side="left")

		#Sound
		self.frameCombo = tk.Frame(self)
		self.frameCombo.pack()

		self.labelSounds = tk.Label(self.frameCombo, text="Sound:", font=("Arial Black Bold", font_size))
		self.labelSounds.pack(side="top")
		self.chooseSound = tk.StringVar()
		self.comboboxSound = ttk.Combobox(self.frameCombo, width=35, values=nomineesList[2], textvariable=self.chooseSound, font=("Arial Black Bold", font_size))
		self.comboboxSound.set("Select nominee")
		self.comboboxSound.pack(side="left")

		#Original Song
		self.frameCombo = tk.Frame(self)
		self.frameCombo.pack()

		self.labelSongs = tk.Label(self.frameCombo, text="Original Song:", font=("Arial Black Bold", font_size))
		self.labelSongs.pack(side="top")
		self.chooseSong = tk.StringVar()
		self.comboboxSong = ttk.Combobox(self.frameCombo, width=35, values=nomineesList[4], textvariable=self.chooseSong, font=("Arial Black Bold", font_size))
		self.comboboxSong.set("Select nominee")
		self.comboboxSong.pack(side="left")

		#Score
		self.frameCombo = tk.Frame(self)
		self.frameCombo.pack()

		self.labelScores = tk.Label(self.frameCombo, text="Original Score:", font=("Arial Black Bold", font_size))
		self.labelScores.pack(side="top")
		self.chooseScore = tk.StringVar()
		self.comboboxScore = ttk.Combobox(self.frameCombo, width=35, values=nomineesList[3], textvariable=self.chooseScore, font=("Arial Black Bold", font_size))
		self.comboboxScore.set("Select nominee")
		self.comboboxScore.pack(side="left")

		#Costume Design
		self.frameCombo = tk.Frame(self)
		self.frameCombo.pack()

		self.labelCostumes = tk.Label(self.frameCombo, text="Costume Design:", font=("Arial Black Bold", font_size))
		self.labelCostumes.pack(side="top")
		self.chooseCostume = tk.StringVar()
		self.comboboxCostume = ttk.Combobox(self.frameCombo, width=35, values=nomineesList[0],  textvariable=self.chooseCostume, font=("Arial Black Bold", font_size))
		self.comboboxCostume.set("Select nominee")
		self.comboboxCostume.pack(side="left")

		#Adapted Screenplay
		self.frameCombo = tk.Frame(self)
		self.frameCombo.pack()

		self.labelAdaptScreens = tk.Label(self.frameCombo, text="Adapted Screenplay:", font=("Arial Black Bold", font_size))
		self.labelAdaptScreens.pack(side="top")
		self.chooseAdaptScreen = tk.StringVar()
		self.comboboxAdaptScreen = ttk.Combobox(self.frameCombo, width=35, values=nomineesList[5], textvariable=self.chooseAdaptScreen, font=("Arial Black Bold", font_size))
		self.comboboxAdaptScreen.set("Select nominee")
		self.comboboxAdaptScreen.pack(side="left")

		#Original Screenplay
		self.frameCombo = tk.Frame(self)
		self.frameCombo.pack()

		self.labelOrigiScreens = tk.Label(self.frameCombo, text="Original Screenplay:", font=("Arial Black Bold", font_size))
		self.labelOrigiScreens.pack(side="top")
		self.chooseOrigiScreen = tk.StringVar()
		self.comboboxOrigiScreen = ttk.Combobox(self.frameCombo, width=35, values=nomineesList[6], textvariable=self.chooseOrigiScreen, font=("Arial Black Bold", font_size))
		self.comboboxOrigiScreen.set("Select nominee")
		self.comboboxOrigiScreen.pack(side="left")

		#Actress in a Supporting Role
		self.frameCombo = tk.Frame(self)
		self.frameCombo.pack()

		self.labelSupActresses = tk.Label(self.frameCombo, text="Actress in a Supporting Role:", font=("Arial Black Bold", font_size))
		self.labelSupActresses.pack(side="top")
		self.chooseSupActress = tk.StringVar()
		self.comboboxSupActress = ttk.Combobox(self.frameCombo, width=35, values=nomineesList[8], textvariable=self.chooseSupActress, font=("Arial Black Bold", font_size))
		self.comboboxSupActress.set("Select nominee")
		self.comboboxSupActress.pack(side="left")

		#Actor in a Supporting Role
		self.frameCombo = tk.Frame(self)
		self.frameCombo.pack()

		self.labelSupActors = tk.Label(self.frameCombo, text="Actor in a Supporting Role:", font=("Arial Black Bold", font_size))
		self.labelSupActors.pack(side="top")
		self.chooseSupActor = tk.StringVar()
		self.comboboxSupActor = ttk.Combobox(self.frameCombo, width=35, values=nomineesList[9], textvariable=self.chooseSupActor, font=("Arial Black Bold", font_size))
		self.comboboxSupActor.set("Select nominee")
		self.comboboxSupActor.pack(side="left")

		#Film Editing
		self.frameCombo = tk.Frame(self)
		self.frameCombo.pack()

		self.labelEdits = tk.Label(self.frameCombo, text="Film Editing:", font=("Arial Black Bold", font_size))
		self.labelEdits.pack(side="top")
		self.chooseEdit = tk.StringVar()
		self.comboboxEdit = ttk.Combobox(self.frameCombo, width=35, values=nomineesList[10], textvariable=self.chooseEdit, font=("Arial Black Bold", font_size))
		self.comboboxEdit.set("Select nominee")
		self.comboboxEdit.pack(side="left")

		#Cinematography
		self.frameCombo = tk.Frame(self)
		self.frameCombo.pack()

		self.labelCinematographies = tk.Label(self.frameCombo, text="Cinematography:", font=("Arial Black Bold", font_size))
		self.labelCinematographies.pack(side="top")
		self.chooseCinematography = tk.StringVar()
		self.comboboxCinematography = ttk.Combobox(self.frameCombo, width=35, values=nomineesList[11], textvariable=self.chooseCinematography, font=("Arial Black Bold", font_size))
		self.comboboxCinematography.set("Select nominee")
		self.comboboxCinematography.pack(side="left")

		#Visual Effects
		self.frameCombo = tk.Frame(self)
		self.frameCombo.pack()

		self.labelVfxes = tk.Label(self.frameCombo, text="Visual Effects:", font=("Arial Black Bold", font_size))
		self.labelVfxes.pack(side="top")
		self.chooseVfx = tk.StringVar()
		self.comboboxVfx = ttk.Combobox(self.frameCombo, width=35, values=nomineesList[12], textvariable=self.chooseVfx, font=("Arial Black Bold", font_size))
		self.comboboxVfx.set("Select nominee")
		self.comboboxVfx.pack(side="left")

		#International Feature Film
		self.frameCombo = tk.Frame(self)
		self.frameCombo.pack()

		self.labelInternationals = tk.Label(self.frameCombo, text="International Feature Film:", font=("Arial Black Bold", font_size))
		self.labelInternationals.pack(side="top")
		self.chooseInternational = tk.StringVar()
		self.comboboxInternational = ttk.Combobox(self.frameCombo, width=35, values=nomineesList[14], textvariable=self.chooseInternational, font=("Arial Black Bold", font_size))
		self.comboboxInternational.set("Select nominee")
		self.comboboxInternational.pack(side="left")

		#Directing
		self.frameCombo = tk.Frame(self)
		self.frameCombo.pack()

		self.labelDirects = tk.Label(self.frameCombo, text="Directing:", font=("Arial Black Bold", font_size))
		self.labelDirects.pack(side="top")
		self.chooseDirect = tk.StringVar()
		self.comboboxDirect = ttk.Combobox(self.frameCombo, width=35, values=nomineesList[13], textvariable=self.chooseDirect, font=("Arial Black Bold", font_size))
		self.comboboxDirect.set("Select nominee")
		self.comboboxDirect.pack(side="left")

		#Animated Feature Film
		self.frameCombo = tk.Frame(self)
		self.frameCombo.pack()

		self.labelAnimations = tk.Label(self.frameCombo, text="Animated Feature Film:", font=("Arial Black Bold", font_size))
		self.labelAnimations.pack(side="top")
		self.chooseAnimation = tk.StringVar()
		self.comboboxAnimation = ttk.Combobox(self.frameCombo, width=35, values=nomineesList[15], textvariable=self.chooseAnimation, font=("Arial Black Bold", font_size))
		self.comboboxAnimation.set("Select nominee")
		self.comboboxAnimation.pack(side="left")

		#Actress in a Leading Role
		self.frameCombo = tk.Frame(self)
		self.frameCombo.pack()

		self.labelActresses = tk.Label(self.frameCombo, text="Actress in a Leading Role:", font=("Arial Black Bold", font_size))
		self.labelActresses.pack(side="top")
		self.chooseActress = tk.StringVar()
		self.comboboxActress = ttk.Combobox(self.frameCombo, width=35, values=nomineesList[16], textvariable=self.chooseActress, font=("Arial Black Bold", font_size))
		self.comboboxActress.set("Select nominee")
		self.comboboxActress.pack(side="left")

		#Actor in a Leading Role
		self.frameCombo = tk.Frame(self)
		self.frameCombo.pack()

		self.labelActors = tk.Label(self.frameCombo, text="Actor in a Leading Role:", font=("Arial Black Bold", font_size))
		self.labelActors.pack(side="top")
		self.chooseActor = tk.StringVar()
		self.comboboxActor = ttk.Combobox(self.frameCombo, width=35, values=nomineesList[17], textvariable=self.chooseActor, font=("Arial Black Bold", font_size))
		self.comboboxActor.set("Select nominee")
		self.comboboxActor.pack(side="left")

		#Best Picture
		self.frameCombo = tk.Frame(self)
		self.frameCombo.pack()

		self.labelMovies = tk.Label(self.frameCombo, text="Best Picture:", font=("Arial Black Bold", font_size))
		self.labelMovies.pack(side="top")
		self.chooseMovie = tk.StringVar()
		self.comboboxMovie = ttk.Combobox(self.frameCombo, width=35, values=nomineesList[18], textvariable=self.chooseMovie, font=("Arial Black Bold", font_size))
		self.comboboxMovie.set("Select nominee")
		self.comboboxMovie.pack(side="left")

		#BUTTONS
		self.frameButton = tk.Frame(self)
		self.frameButton.pack()

		self.buttonEnter = tk.Button(self.frameButton, text="Enter")
		self.buttonEnter.pack(side="left")
		self.buttonEnter.bind("<Button>", control.regWinners)

		self.buttonCancel = tk.Button(self.frameButton, text="Cancel")
		self.buttonCancel.pack(side="left")
		self.buttonCancel.bind("<Button>", control.closeHandler)

	def showWindow(self, title, msg):
		messagebox.showinfo(title, msg)

class CtrlPlayer():
	def __init__(self, controller):
		self.controller = controller

		#NOMINEES OSCAR 2023
		#Costume Design
		self.costume = ["Babylon - Mary Zophres",
										"Black Panther: Wakanda Forever - Ruth Carter",
									  "Elvis - Catherine Martin",
									  "Everything Everywhere All at Once - Shirley Kurata",
									  "Mrs. Harris Goes to Paris - Jenny Beavan",]
		
		#Makeup and Hairstyling
		self.makeup = ["All Quiet on the Western Front - Heike Merker and Linda Eisenhamerová",
									 "The Batman - Naomi Donne, Mike Marino and Mike Fontano",
									 "Black Panther: Wakanda Forever - Camille Friend and Joel Harlow",
									 "Elvis - Mark Coulier, Jason Baird and Aldo Signoretti",
									 "The Whale - Adrien Morot, Judy Chin and Anne Marie Bradley"]

		#Sound
		self.sound = ["All Quiet on the Western Front - Viktor Prášil, Frank Kruse, Markus Stemler, Lars Ginzel and Stefan Korte",
									"Avatar: The Way of Water - Julian Howarth, Gwendolyn Yates Whittle, Dick Bernstein, Christopher Boyes, Gary Summers and Michael Hedges",
									"The Batman - Stuart Wilson, William Files, Douglas Murray and Andy Nelson",
									"Elvis - David Lee, Wayne Pashley, Andy Nelson and Michael Keller",
									"Top Gun: Maverick - Mark Weingarten, James H. Mather, Al Nelson, Chris Burdon and Mark Taylor"]

		#Original Score
		self.score = ["All Quiet on the Western Front - Volkes Bertelmann",
									"Babylon - Justin Hurwitz",
									"The Banshees of Inisherin - Carter Burwell",
									"Everything Everywhere All at Once - Son Lux",
									"The Fabelmans - John Williams"]

		#Original Song
		self.song = ["Applause - Tell It Like a Woman - Diane Warren",
									"Hold My Hand - Top Gun: Maverick - Lady Gaga",
									"Lift Me Up - Black Panther: Wakanda Forever - Rihanna",
									"Naatu Naatu - RRR - M. M. Keeravaani",
									"This is a Life - Everything Every Where All at Once - Son Lux, Mitski and David Byrne"]

		#Adapted Screenplay
		self.adaptScreen = ["All Quiet on the Western Front - Edward Berger, Lesley Paterson and Ian Stokell",
												"Glass Onion: A Knives Out Mystery - Rian Johnson",
												"Living - Kazuo Ishiguro",
												"Top Gun: Maverick - Ehren Kruger, Eric Warren Singer and Christopher McQuarrie",
												"Women Talking - Sarah Polley"]

		#Original Screenplay
		self.origiScreen = ["The Banshees of Inisherin - Martin McDonaugh",
												"Everything Everywhere All at Once - Daniel Kwan and Daniel Scheinert",
												"The Fabelmans - Steven Spielber and Tony Kushner",
												"Tár - Todd Field",
												"Triangle of Sadness - Ruben Östlund"]

		#Production Design
		self.prodDesign = ["All Quiet on the Western Front - Christian M. Goldbeck",
											 "Avatar: The Way of Water - Dylan Cole and Ben Procter",
											 "Babylon - Florencia Martin",
											 "Elvis - Catherine Martin and Karen Murphy",
											 "The Fabelmans - Rick Carter"]

		#Actress in a Suporting Role
		self.supActress = ["Angela Bassett - Black Panther: Wakanda Forever",
											 "Hong Chau - The Whale",
											 "Kerry Condon - The Banshees of Inisherin",
											 "Jamie Lee Curtis - Everything Everywhere All at Once",
											 "Stephanie Hsu - Everything Everywhere All at Once"]

		#Actor in a Suporting Role
		self.supActor = ["Brendan Gleeson - The Banshees of Inisherin",
										 "Brian Tyree Henry - Causway",
										 "Judd Hirsh - The Fabelmans",
										 "Barry Keoghan - The Banshees of Inisherin",
										 "Kee Huy Quan - Everything Everywhere All at Once"]

		#Film Editing
		self.edit = ["The Banshees of Inisherin - Mikkel E. G. Nielsen",
								 "Elvis - Matt Villa and Jonathan Redmond",
								 "Everything Everywhere All at Once - Paul Rogers",
								 "Tár - Monika Willi",
								 "Top Gun: Maverick - Eddie Hamilton"]

		#Cinematography
		self.cinematography = ["All Quiet on the Western Front - James Friend",
													 "Bardo, False Chronicle of a Handful of Truths - Darius Khondji",
													 "Elvis - Mandy Walker",
													 "Empire of Light - Roger Deakins",
													 "Tár - Florian Hoffmeister"]

		#Visual Effects
		self.vfx = ["All Quiet on the Western Front - Frank Petzold",
								"Avatar: The Way of Water - Joe Letteri",
								"The Batman - Dan Lemmon",
								"Black Panther: Wakanda Forever - Geoffrey Baumann",
								"Top Gun: Maverick - Ryan Tudhope"]

		#Directing
		self.direct = ["The Banshees of Inisherin - Martin McDonagh",
									 "Everything Everywhere All at Once - Daniel Kwan and Daniel Sheinert",
									 "The Fabelmans - Steven Spielberg",
									 "Tár - Todd Field",
									 "Triangle of Sadness - Ruben Östlund"]

		#International Feature Film
		self.international = ["All Quiet on the Western Front - Germany",
													"Argentina, 1985 - Argentina",
													"Close - Belgium",
													"EO - Poland",
													"The Quiet Girl - Ireland"]

		#Animated Feature Film
		self.animation = ["Guillermo Del Toro's Pinocchio - Gullermo del Toro - Netflix",
											"Marcel the Shell With Shoes On - Dean Fleischer Camp - Cinereach",
											"Puss in Boots: The Last Wish - Joel Crawford and Mark Swift - DreamWorks",
											"The Sea Beast - Chris Williams and Jed Schlanger - Netflix",
											"Turning Red - Domee Shi and Lindsey Collins - Disney Pixar"]

		#Actor in a Leading Role
		self.actor = ["Austin Butler - Elvis",
									"Colin Farrell - The Banshees of Inisherin",
									"Brendan Fraser - The Whale",
									"Paul Mescal - Aftersun",
									"Bill Nighy - Living"]

		#Actress in a Leading Role
		self.actress = ["Cate Blanchett - Tár",
										"Ana de Armas - Blonde",
										"Andrea Riseborough - To Leslie",
										"Michelle Williams - The Fabelmans",
										"Michelle Yeoh - Everything Everywhere All at Once"]

		#Best Picture
		self.movie = ["All Quiet on the Western Front - Edward Berger",
									"Avatar: The Way of Water - James Cameron",
									"The Banshees of Inisherin - Martin McDonagh",
								  "Elvis - Baz Luhrmann",
								  "Everything Everywhere All at Once - Daniel Kwan and Daniel Sheinert",
								  "The Fabelmans - Steven Spielberg",
									"Tár - Todd Field",
									"Top Gun: Maverick - Joseph Kosinski",
									"Triangle of Sadness - Ruben Östlund",
									"Women Talking - Sarah Polley"]

		self.nomineesList = [self.costume, self.makeup, self.sound, self.score, self.song, self.adaptScreen, self.origiScreen, self.prodDesign, self.supActress, self.supActor, self.edit, self.cinematography, self.vfx, self.direct, self.international, self.animation, self.actress, self.actor, self.movie]

		if not os.path.isfile("bets.pickle"):
			self.betsList = []
		else:
			with open("bets.pickle", "rb") as f:
				self.betsList = pickle.load(f)

		if not os.path.isfile("winners.pickle"):
			self.winners = None
		else:
			with open("winners.pickle", "rb") as f:
				self.winners = pickle.load(f)
		
	def getNominees(self):
		str = "\nMAKEUP AND HAIRSTYLING | Value: 1\n"
		for nom in self.makeup:
			str += ' -> ' + nom + '\n'

		str += "\nPRODUCTION DESIGN | Value: 1\n"
		for nom in self.prodDesign:
			str += ' -> ' + nom + '\n'

		str += "\nSOUND | Value: 2\n"
		for nom in self.sound:
			str += ' -> ' + nom + '\n'

		str += "\nORIGINAL SONG | Value: 2\n"
		for nom in self.song:
			str += ' -> ' + nom + '\n'

		str += "\nORIGINAL SCORE | Value: 3\n"
		for nom in self.score:
			str += ' -> ' + nom + '\n'


		str += "\nCOSTUME DESIGN | Value: 3\n"
		for nom in self.costume:
			str += ' -> ' + nom + '\n'

		str += "\nADAPTED SCREENPLAY | Value: 3\n"
		for nom in self.adaptScreen:
			str += ' -> ' + nom + '\n'

		str += "\nORIGINAL SCREENPLAY | Value: 3\n"
		for nom in self.origiScreen:
			str += ' -> ' + nom + '\n'

		str += "\nACTRESS IN A SUPPORTING ROLE | Value: 3\n"
		for nom in self.supActress:
			str += ' -> ' + nom + '\n'

		str += "\nACTOR IN A SUPPORTING ROLE | Value: 3\n"
		for nom in self.supActor:
			str += ' -> ' + nom + '\n'

		str += "\nFILM EDITING | Value: 4\n"
		for nom in self.edit:
			str += ' -> ' + nom + '\n'

		str += "\nCINEMATOGRAPHY | Value: 4\n"
		for nom in self.cinematography:
			str += ' -> ' + nom + '\n'

		str += "\nVISUAL EFFECTS | Value: 4\n"
		for nom in self.vfx:
			str += ' -> ' + nom + '\n'

		str += "\nINTERNATIONAL FEATURE FILM | Value: 4\n"
		for nom in self.international:
			str += ' -> ' + nom + '\n'

		str += "\nDIRECTING | Value: 5\n"
		for nom in self.direct:
			str += ' -> ' + nom + '\n'

		str += "\nANIMATED FEATURE FILM | Value: 5\n"
		for nom in self.animation:
			str += ' -> ' + nom + '\n'

		str += "\nACTRESS IN A LEADING ROLE | Value: 6\n"
		for nom in self.actress:
			str += ' -> ' + nom + '\n'

		str += "\nACTOR IN A LEADING ROLE | Value: 6\n"
		for nom in self.actor:
			str += ' -> ' + nom + '\n'

		str += "\nBEST PICTURE | Value: 10\n"
		for nom in self.movie:
			str += ' -> ' + nom + '\n'

		return str
	
	def printNominees(self):
		self.view = ViewNominees(self, self.getNominees())

	def closeHandler(self, event):
		self.view.destroy()

	def createBet(self):
		self.view = ViewCreateBet(self, self.nomineesList)

	def enterHandler(self, event):
		name = self.view.inputName.get()

		if name == None:
			self.view.showWindow('Error', 'Please insert a name')
			return

		bets = [self.view.comboboxActor.get(), self.view.comboboxActress.get(), self.view.comboboxAdaptScreen.get(), self.view.comboboxAnimation.get(), self.view.comboboxCinematography.get(), self.view.comboboxCostume.get(), self.view.comboboxDirect.get(), self.view.comboboxEdit.get(), self.view.comboboxInternational.get(), self.view.comboboxMakeup.get(), self.view.comboboxMovie.get(), self.view.comboboxOrigiScreen.get(), self.view.comboboxProdDesign.get(), self.view.comboboxScore.get(), self.view.comboboxSong.get(), self.view.comboboxSound.get(), self.view.comboboxSupActor.get(), self.view.comboboxSupActress.get(), self.view.comboboxVfx.get()]
		
		if 'Select nominee' in bets:
			self.view.showWindow('Error', 'Please select a nominee for every category')
			return

		plBets = Bets(actor=bets[0], actress=bets[1], adaptScreen=bets[2], animation=bets[3], cinematography=bets[4], costume=bets[5], direct=bets[6], edit=bets[7], international=bets[8], makeup=bets[9], movie=bets[10], origiScreen=bets[11], prodDesign=bets[12], score=bets[13], song=bets[14], sound=bets[15], supActor=bets[16], supActress=bets[17], vfx=bets[18])

		bet = Player(name, plBets)

		self.betsList.append(bet)
		self.saveBets()

		self.view.showWindow('Success', 'Bet created successfully!')
		self.view.destroy()

	def saveBets(self):
		if len(self.betsList) != 0:
			with open("bets.pickle","wb") as f:
				pickle.dump(self.betsList, f)

	def saveWinners(self):
		if self.winners != None:
			with open("winners.pickle","wb") as f:
				pickle.dump(self.winners, f)

	def printData(self):
		info = "Number of players: " + str(len(self.betsList)) + "\nPlayers list:\n"

		for player in self.betsList:
			info += " - " + player.name.title() + "\n"

		if self.winners == None:
			info += "\nWinners yet to be registered."
		else:
			info += "\nOscar Winners:\n" + self.winners.getBets() + "\n\nResults:\n"
			for player in self.betsList:
				points, count = self.calcPoints(player.bets)
				info += " - " + player.name.upper() + ": " + str(points) + " points and " + str(count) + " hits.\n"

		self.view = ViewData(self, info)

	def calcPoints(self, playerBets):
		points = 0
		count = 0
		
		if playerBets.costume == self.winners.costume:
			points += 3
			count += 1
		if playerBets.makeup == self.winners.makeup:
			points += 1
			count += 1
		if playerBets.sound == self.winners.sound:
			points += 2
			count += 1
		if playerBets.score == self.winners.score:
			points += 3
			count += 1
		if playerBets.song == self.winners.song:
			points += 2
			count += 1
		if playerBets.prodDesign == self.winners.prodDesign:
			points += 1
			count += 1
		if playerBets.adaptScreen == self.winners.adaptScreen:
			points += 3
			count += 1
		if playerBets.origiScreen == self.winners.origiScreen:
			points += 3
			count += 1
		if playerBets.supActress== self.winners.supActress:
			points += 3
			count += 1
		if playerBets.supActor == self.winners.supActor:
			points += 3
			count += 1
		if playerBets.edit == self.winners.edit:
			points += 4
			count += 1
		if playerBets.cinematography == self.winners.cinematography:
			points += 4
			count += 1
		if playerBets.vfx == self.winners.vfx:
			points += 4
			count += 1
		if playerBets.direct == self.winners.direct:
			points += 5
			count += 1
		if playerBets.international == self.winners.international:
			points += 4
			count += 1
		if playerBets.animation == self.winners.animation:
			points += 5
			count += 1
		if playerBets.actor == self.winners.actor:
			points += 6
			count += 1
		if playerBets.actress == self.winners.actress:
			points += 6
			count += 1
		if playerBets.movie == self.winners.movie:
			points += 10
			count += 1

		return points, count

	def registerWin(self):
		self.view = ViewRegisterWinners(self, self.nomineesList)

	def regWinners(self, event):
		bets = [self.view.comboboxActor.get(), self.view.comboboxActress.get(), self.view.comboboxAdaptScreen.get(), self.view.comboboxAnimation.get(), self.view.comboboxCinematography.get(), self.view.comboboxCostume.get(), self.view.comboboxDirect.get(), self.view.comboboxEdit.get(), self.view.comboboxInternational.get(), self.view.comboboxMakeup.get(), self.view.comboboxMovie.get(), self.view.comboboxOrigiScreen.get(), self.view.comboboxProdDesign.get(), self.view.comboboxScore.get(), self.view.comboboxSong.get(), self.view.comboboxSound.get(), self.view.comboboxSupActor.get(), self.view.comboboxSupActress.get(), self.view.comboboxVfx.get()]
		
		if 'Select nominee' in bets:
			self.view.showWindow('Error', 'Please select a nominee for every category')
			return

		self.winners = Bets(actor=bets[0], actress=bets[1], adaptScreen=bets[2], animation=bets[3], cinematography=bets[4], costume=bets[5], direct=bets[6], edit=bets[7], international=bets[8], makeup=bets[9], movie=bets[10], origiScreen=bets[11], prodDesign=bets[12], score=bets[13], song=bets[14], sound=bets[15], supActor=bets[16], supActress=bets[17], vfx=bets[18])
		self.saveWinners()

		self.view.showWindow('Success', 'Winners registered successfully!')
		self.view.destroy()