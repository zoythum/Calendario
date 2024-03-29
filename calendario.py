#!/usr/bin/env python
from icalendar import Calendar, Event
from datetime import datetime
from dialog import Dialog
import pytz
import os

ics_path = 'Path to ics file'

def save_cal(calendar):
	output_file = open('Compleanni.ics', 'wb')
	output_file.write(calendar.to_ical())
	output_file.close()

def obtain_birthdays(path):
	compleanni = {}
	i = 0
	k = 0
	
	with open(path) as file:
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


def ics2text():
	global ics_path
	ics_file = open(ics_path, 'rb')
	calendar = Calendar.from_ical(ics_file.read())
	output = open('output.txt', 'w')
	entries = {}

	for event in calendar.walk('VEVENT'):
		entries[event['SUMMARY']] = event['DTSTART'].dt

	for key in entries:
		output.write("Summary:     " + key)
		output.write("\n")
		output.write("Start:       " + str(entries[key]))
		output.write("\n")
	output.close()
	return('output.txt')




def populate_calendar(compleanni, calendar, main_dialog):
	timezone = pytz.timezone('Europe/Rome')
	nomi_festeggiati = []
	for y in compleanni:
		nome_festeggiato = y.replace("Compleanno di ", "")
		nomi_festeggiati.append(nome_festeggiato)
	code, tags = main_dialog.checklist("Seleziona quali compleanni vuoi salvare", choices=[("{}".format(x), "", False) for x in nomi_festeggiati])

	if (code == main_dialog.OK):
		for elem in tags:
			nome_festeggiato = "Compleanno di " + elem
			event = Event()
			event.add('summary', nome_festeggiato)
			month, day = convert_date(compleanni[nome_festeggiato])
			data_inizio = datetime(2019, int(month), int(day), 10, 00, tzinfo=timezone)
			data_fine = datetime(2019, int(month), int(day), 11, 00, tzinfo=timezone)
			event.add('dtstart', data_inizio)
			event.add('dtend', data_fine)
			calendar.add_component(event)
	else:
		print("Va bene")

	return(calendar)


def convert_date(date):
	lista_data = date.split('-')
	mese = lista_data[1]
	giorno = lista_data[2]
	return(mese, giorno)

def main():
	main_dialog = Dialog(dialog="dialog")
	main_dialog.set_background_title("Creazione Calendario")
	if (main_dialog.yesno("Vuoi creare un nuovo calendario?") == main_dialog.OK):
		path = ics2text()
		compleanni = obtain_birthdays(path)
		cal = Calendar()
		cal = populate_calendar(compleanni, cal, main_dialog)
		save_cal(cal)
		os.remove("output.txt")



if __name__ == "__main__":
	main()