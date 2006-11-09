from datetime import datetime

def day_suffix(day):
    """
    Return correct English suffix (i.e. 'st', 'nd' etc.)
    """
    
    if 4 <= day <= 20 or 24 <= day <= 30:
        return 'th'
    else:
        return ["st", "nd", "rd"][day % 10 - 1]
    
def fancy_date_interval(start, end):
    """
    If dates share month and year, format it so the month
    is only displayed once.

    >>> from datetime import datetime
    >>> fancy_date_interval(datetime(2006, 1, 29), datetime(2006, 1, 30))
    'Jan 29th-30th, 2006'

    >>> fancy_date_interval(datetime(2006, 1, 29), datetime(2006, 2, 1))
    'Jan 29th-Feb 1st, 2006'

    >>> fancy_date_interval(datetime(2006, 1, 29), datetime(2006, 1, 29))
    'Jan 29th, 2006'

    """
    if (start.year == end.year) and (start.month == end.month) and (start.day == end.day):
        return "%s %s%s, %s" % (start.strftime("%b"),
                                     start.day,
                                     day_suffix(start.day),
                                     start.year)

    elif (start.year == end.year) and (start.month == end.month):
        return "%s %s%s-%s%s, %s" % (start.strftime("%b"),
                                     start.day,
                                     day_suffix(start.day),
                                     end.day,
                                     day_suffix(end.day),
                                     start.year)
    else:
        return "%s %s%s-%s %s%s, %s" % (start.strftime("%b"),
                                     start.day,
                                     day_suffix(start.day),
                                     end.strftime("%b"),
                                     end.day,
                                     day_suffix(end.day),
                                     start.year)
    
def fancy_time_amount(v):
    """Produce a friendly representation of the given time amount.  The
    value is expected to be in seconds as an int.
    
      >>> fancy_time_amount(391)
      u'06:31 (mm:ss)'
      
      >>> fancy_time_amount(360)
      u'06:00 (mm:ss)'

      >>> fancy_time_amount(6360)
      u'01:46:00 (hh:mm:ss)'
    """
    
    remainder = v
    hours = remainder / 60 / 60
    remainder = remainder - (hours * 60 * 60)
    mins = remainder / 60
    secs = remainder - (mins * 60)
    
    if hours > 0:
        return u'%02i:%02i:%02i (hh:mm:ss)' % (hours, mins, secs)
    else:
        return u'%02i:%02i (mm:ss)' % (mins, secs)

def fancy_data_size(v):
    """Produce a friendly reprsentation of the given value.  The value
    Is expected to be in bytes as an int or long.
    
      >>> fancy_data_size(54)
      u'54 B'
      
      >>> fancy_data_size(37932)
      u'37.0 KB'

      >>> fancy_data_size(1237932)
      u'1.2 MB'
    
      >>> fancy_data_size(2911237932)
      u'2.7 GB'
    """
    
    suffix = 'B'
    
    format = u'%i %s'
    if v > 1024:
        suffix = 'KB'
        v = float(v) / 1024.0
        format = u'%.1f %s'
    
    if v > 1024:
        suffix = 'MB'
        v = v / 1024.0
    
    if v > 1024:
        suffix = 'GB'
        v = v / 1024.0

    return format % (v, suffix)

def _test():
    import doctest
    doctest.testmod()
    
if __name__ == "__main__":
    _test()
