
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
    is expected to be in bytes as an int or long.
    
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
