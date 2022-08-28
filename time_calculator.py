def add_time(start, duration, weekday=''):

  #case for day of the week, case insensitive
  
  #makes a list with (start hour, start minute, start PM/AM)
  stime = start.split(':')
  stime_temp = stime[1].split(' ')
  stime.pop(1)
  stime.extend(stime_temp)
  del stime_temp

  #makes a list with (hours to be added, minutes to be added)
  dtime = duration.split(':')

  #calculates how many hours and minutes we get after the duration
  hour = int(stime[0]) + int(dtime[0])
  minute = int(stime[1]) + int(dtime[1])
  if minute >= 60 :
    hour = hour + int(minute / 60)
    minute = minute%60
    
  #empty values of the new time
  noon = ''
  nday = ''
  nweekday = ''
  nhour = str(hour%12)
  
  if nhour == '0' :
    nhour = '12'
    
  #will it become AM or PM after the added duration
  if stime[2] == 'AM' :
    #float -> int, so it's a round number
    days = int(hour / 24)
    halfdays = int(hour / 12)
    
    if halfdays%2 == 0 :
      noon = 'AM'
    else :
      noon = 'PM'

  if stime[2] == 'PM' :
    #respectively +12 and +1, at PM half of the day has already passed
    days = int((hour + 12) / 24)
    halfdays = int(hour / 12) + 1
    
    if halfdays%2 == 0 :
      noon = 'AM'
    else :
      noon = 'PM'
      
  #looks at how many days have passed
  if days == 1 :
    nday = 'next day'
  if days > 1 :
    nday = str(days) + ' days later'

  #looks for the correct weekday in the dictionary of tuples, then chooses the new weekday with a reminder for division by 7 
  if weekday :
    weekdays = {0:"Monday", 1:"Tuesday", 2:"Wednesday", 3:"Thursday", 4:"Friday", 5:"Saturday", 6:"Sunday"}
    for i in range(0,len(weekdays)) :
      if weekdays[i].casefold() == weekday.casefold():
        nweekday = weekdays[(i + days)%7]

  #constructs new_time
  new_time = nhour + ':' + str(minute).zfill(2) + ' ' + noon

  if weekday : 
    new_time += ', ' + nweekday
  if days >= 1 :
      new_time += ' (' + nday + ')'

  return new_time