import os
import string
import gspread
import pandas as pd
from celery import shared_task
from events.models import Event
from venues.models import Venue 

@shared_task(ignore_result=True)
def create_new_events():

    gc = gspread.service_account(os.environ.get('GOOGLE_APPLICATION_CREDENTIALS'))
    worksheet = gc.open("Class / Lecture Tracker").sheet1
    letters = list(string.ascii_uppercase)[0:18]
    cell_list = [letter+'3:'+letter for letter in letters]

    try:
        data = pd.DataFrame(worksheet.batch_get(cell_list))
    except KeyError:
        print('Empty rows')

    data[0] = data[0].apply(lambda x: x[0])
    data[1] = data[1].apply(lambda x: x[0])
    data = data.T
    data = data.rename(columns=data.iloc[0]).drop(data.index[0])

    for i in range(1,len(data)+1):
        if (data['Approved'][i].lower() == 'yes'):        
            new_venue, _ = Venue.objects.get_or_create(name=data['Masjid'][i],
                                                    city=data['City'][i],
                                                    country=data['Country'][i],
                                                    logo_url=data['Image / Logo'][i])
            new_venue.save()

            new_event, _ = Event.objects.get_or_create(venue=new_venue,
                                                    speaker=data['Speaker'][i], 
                                                    title=data['Title'][i],
                                                    startDate=data['Start Date'][i],
                                                    endDate=data['End Date'][i],
                                                    frequency=data['Recurrence'][i],
                                                    startTime=data['Start Time'][i],
                                                    endTime=data['End Time'][i],
                                                    timezone=data['Timezone'][i],
                                                    language=data['Language'][i],
                                                    stream_medium=data['Stream Medium'][i],
                                                    stream_link=data['Stream Link'][i],
                                                    is_live=data['Live'][i].lower() == 'yes',
                                                    qa_allowed=data['Q&A Allowed'][i].lower() == 'yes')
            new_event.save()
    else:
        print("Not yet approved by admin!")