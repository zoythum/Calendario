from icalendar import Calendar, Event
from datetime import datetime
import pytz

def save_cal(calendar):
	output_file = open('Compleanni.ics', 'wb')
	output_file.write(calendar.to_ical())
	output_file.close()

def obtain_birthdays():
	compleanni = {}
	i = 0
	k = 0
	
	with open('percorso del file .txt di partenza') as file:
		content = [line.rstrip('\n') for line in file]	

	while i < len(content):
		if (content[i] == ''):
			content.pop(i)
		i+=1

	while k < len(content):
		summary = content[k].split(':')[1].strip()
		date = content[k+1].split(':')[1].strip()
		compleanni[summary] = date
		k += 2

	return(compleanni)

def populate_calendar(compleanni, calendar):

	timezone = pytz.timezone('Europe/Rome')
	for keys in compleanni:
		nome_festeggiato = keys.replace("Compleanno di ", "")
		to_add = input("vuoi aggiungere il compleanno di {}? (y/n)".format(nome_festeggiato))	

		if (to_add == 'y'):
			print("Ok, lo aggiungo\n")
			event = Event()
			event.add('summary', keys)
			month, day = convert_date(compleanni[keys])
			data_inizio = datetime(2019, int(month), int(day), 10, 00, tzinfo=timezone)
			data_fine = datetime(2019, int(month), int(day), 11, 00, tzinfo=timezone)
			event.add('dtstart', data_inizio)
			event.add('dtend', data_fine)
			calendar.add_component(event)
		elif (to_add == 'n'):
			print("Va bene, non sarà aggiunto\n")
		else:
			print("Rispondi solo con y/n")
	return(calendar)

def convert_date(date):
	lista_data = date.split('-')
	mese = lista_data[1]
	giorno = lista_data[2]
	return(mese, giorno)

def main():

	print("Seleziona quali compleanni vuoi salvare, rispondi solo con y/n")
	compleanni = obtain_birthdays()
	cal = Calendar()
	cal = populate_calendar(compleanni, cal)
	save_cal(cal)



if __name__ == "__main__":
	main()