import os
import string
import gspread
from celery import shared_task
from events.models import Event
from venues.models import Venue 

@shared_task(ignore_result=True)
def create_new_events():
    try:
        gc = gspread.service_account(os.environ.get('SERVICE_ACCOUNT'))
    worksheet = gc.open("Class / Lecture Tracker").sheet1
    letters = list(string.ascii_uppercase[0:16])
    cell_list = [letter+'4:'+letter for letter in letters]

    try:
        data = worksheet.batch_get(cell_list)
    except KeyError:
        print('Empty Rows')

    if (data):
        for j in range(len(data[0])):
            event = []
            for i in range(len(data)):
                try:
                    event.append(data[i][j][0])
                except IndexError:
                    event.append('')
            if (event[15].lower() == 'yes'):
                new_venue, _ = Venue.objects.get_or_create(name=event[8],
                                                        city=event[7],
                                                        logo_url=event[10])
                new_venue.save()

                new_event, _ = Event.objects.get_or_create(venue=new_venue,
                                                        speaker=event[0], 
                                                        title=event[1],
                                                        startDate=event[2],
                                                        endDate=event[3],
                                                        frequency=event[4],
                                                        eventTime=event[5],
                                                        timezone=event[6],
                                                        language=event[9],
                                                        stream_medium=event[11],
                                                        stream_link=event[12],
                                                        is_live=event[13].lower() == 'yes',
                                                        qa_allowed=event[14].lower() == 'yes')
                new_event.save()
            else:
                print("Not yet approved")
