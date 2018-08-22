import datetime

def takeNotes():
	observedTeacher = input('What is the name of the teacher being observed? ').title().replace(' ','_')
	observedClass = input('What is the class the teacher is teaching? ').replace(' ','_')
	start = input('Press enter to start taking notes.')
	
	start_time = datetime.datetime.now()
	observationMonth = start_time.month
	observationDay = start_time.day
	observationYear = start_time.year
	outfile = f'observation-{observedTeacher}-{observedClass}-{observationMonth:02d}-{observationDay:02d}-{observationYear:02d}.csv'
	
	with open(outfile, 'w') as f:
		note = input('Notes: ')
		last_time = start_time
		while (note != '' and note != 'Done'):
			note_time = datetime.datetime.now()
			time_delta = note_time - last_time
			minutes, seconds = divmod(int(time_delta.total_seconds()),60)

			col1 = note_time.strftime("%H:%M:%S")
			col2 = f'00:{minutes:02d}:{seconds:02d}'
			col3 = note
			f.write(f'{col1},{col2},{col3}\n')
			note = input('Notes: ')
			last_time = note_time

takeNotes()