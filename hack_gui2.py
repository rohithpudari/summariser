# -*- coding: utf-8 -*-

import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s',level = logging.INFO)
from gensim.summarization import summarize
import Tkinter
from tkFileDialog import askopenfilename
m = Tkinter.Tk()
m.title('News Summarizer ')
m.minsize(width=5000, height=1000)

label2 = Tkinter.Label( m, text = "welcome to news Summarizer" ,font=("Helvetica", 26))
label2.pack()
label2.place(x=500,y=50)

label3 = Tkinter.Label( m, text = "choose the file conataining any random news" ,font=("Helvetica",16))
label3.pack()
label3.place(x=520,y=100)
text = '''Sports and games both are very important and easy way to improve physical and mental fitness. Now-a-days, the scope of the sports and games has been increased by the effort of the government. Anyone of us can establish a good career in the sports for whole life together with the maintenance of food health and fitness of the body. It has become a very good way to achieve success and good job. It is the useful means of getting entertainment and physical activity on daily basis. It is the character and discipline building technique which holds with us whole life. It makes us active and gives us energy and strength.
Playing sports and games continuously means motivating the mental and physical growth. It makes us learn about how to maintain the physical and mental balance as it improves the concentration level and memory. It makes life too peaceful to tackle any difficult situation. It develops sense of friendliness and removes all the differences between two people. It keeps body in shape which makes us strong and active however it also keeps mind peaceful which brings positive thoughts and keeps us away from the many diseases and disorders.
It gives us lots of energy and strength as well as removes all the tiredness and lethargy by improving the blood circulation all through the body and promoting the physical and mental well-being. It improves ones capability, work efficiency and prevent from being exhausted mentally and physically. It is the integral part of improving the quality of education among students. Sports and education both together are the best ways of achieving success in life.
Everybody understands that, sports and games mean only the physical and mental fitness. However it has many hidden benefits as well. Sports and good education both together become the way to achieve success in the life of a child. Both should be given equal priority in the school and colleges to go ahead and make the bright career of the students. Sports mean not only the bodily exercise however it means to promote the concentration level of the students towards study. There is a common saying about the sports that “A sound mind in a sound body” means there should be a well working mind in the fit body in order to go ahead and get success in the life.'''
def choosefile():
	filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
	label = Tkinter.Label( m, text = filename )
	label.pack()
	label.place(x=550,y=130)
	var = filename
def summarizefile():
	summary = summarize(text)
	print summary
summary = summarize(text)
def categorize():
	input_list = []

	with open(askopenfilename(),'r') as f:
		for line in f:
			for word in line.split():
				chars_to_remove=['.',',','?','!','@','#','$','%','^','&','*',')','(','-','_','+','=','{','}','[','}','|','<','>',':',';','"']
				r=word.translate(None, ''.join(chars_to_remove))
				input_list.append(r) #print(word)


#print input_list

	stop_words_list = []

	with open('stop_words.txt','r') as f:
		for line in f:
			for word in line.split():
				stop_words_list.append(word)

	c_list = []
	c_list = list(set(input_list) - set(stop_words_list))
	c_list = list(set(c_list))

	sports_list,entertainment_list,politics_list,business_list = [],[],[],[]

	with open('sports.txt','r') as f:
		for line in f:
			for word in line.split(','):
				sports_list.append(word)

	with open('politics.txt','r') as f:
		for line in f:
			for word in line.split(','):
				politics_list.append(word)

	with open('entertainment.txt','r') as f:
		for line in f:
			for word in line.split(','):
				entertainment_list.append(word)

	with open('business_2.txt','r') as f:
		for line in f:
			for word in line.split(','):
				business_list.append(word)

#print politics_list

	sports_count,ent_count,politics_count,business_count,other_count = 0,0,0,0,0

	for item in c_list:
		if item in sports_list:
			sports_count +=1
		if item in entertainment_list:
			ent_count +=1
		if item in politics_list:
			politics_count +=1
		if item in business_list:
			business_count +=1
	#else:
	#	other_count +=1

	dict = {'sports':sports_count,'Entertainment':ent_count,'politics':politics_count,'Business':business_count,'other':other_count}

	print dict

	result = max(dict,key = dict.get)
	fresult = 'This news is about '+result
	fsum = 'it is mainly talking about: \n'+summary
	if result == 'other':
		print "This content does not belong to any news"
	else:
		label = Tkinter.Label( m, text = fresult,font=("Helvetica", 20) )
		label1 = Tkinter.Label( m,text = fsum,font=("Helvetica",16))
		label.pack()
		label1.pack()
		label.place(x=160,y=200)
		label1.place(x=50,y=150)




#B_choose = Tkinter.Button(m, text ="summarize?", command = summarizefile)
#B_choose.place(x=250,y=130)


categorize = Tkinter.Button(m, text ="brief it?", command = categorize)
categorize.place(x=650,y=170)


m.mainloop()
