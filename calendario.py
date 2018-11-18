from icalendar import Calendar, Event
from datetime import datetime
import pytz

def save_cal(calendar):
	output_file = open('calendarioprova.ics', 'wb')
	output_file.write(calendar.to_ical())
	output_file.close()


def month_to_int(month):
	if (isinstance(month, str)):
		month = month.lower()
		if month == 'gennaio':
			return(1)
		elif month == 'febbraio':
			return(2)
		elif month == 'marzo':
			return(3)
		elif month == 'aprile':
			return(4)
		elif month == 'maggio':
			return(5)
		elif month == 'giugno':
			return(6)
		elif month == 'luglio':
			return(7)
		elif month == 'agosto':
			return(8)
		elif month == 'settembre':
			return(9)
		elif month == 'ottobre':
			return(10)
		elif month == 'novembre':
			return(11)
		elif month == 'dicembre':
			return(12)									
	elif ((isinstance(month, int))or(isinstance(month, float))):
		return(int(month))



def main():
	print ("Inserisci tutti i compleanni che vuoi salvare")

	add_new = "yes"
	cal = Calendar()

	while(add_new != 'no'):
		festeggiato = input("Di chi è il compleanno?")
		month = input("in che mese compie gli anni?")
		month = month_to_int(month)
		day = int(input("che giorno?"))
		timezone = pytz.timezone('Europe/Rome')
		data_inizio = datetime(2019, month, day, 10, 00, tzinfo=timezone)
		data_fine = datetime(2019, month, day, 11, 00, tzinfo=timezone)

		event = Event()
		event.add('summary', "compleanno di " + festeggiato)
		event.add('dtstart', data_inizio)
		event.add('dtend', data_fine)

		cal.add_component(event)
		add_new = input("vuoi aggiungere un altro compleanno?")

	save_cal(cal)





if __name__ == "__main__":
	main()