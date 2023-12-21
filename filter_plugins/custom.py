import datetime

def to_datetime_from_iso(string):
    return datetime.datetime.fromisoformat(string)

class FilterModule(object):
    def filters(self):
        return {
            'to_datetime_from_iso': to_datetime_from_iso,
        }
