#JSONEncoder to convert datetime values in json objects to isoformat
import json
import datetime
class json_datetime_encoder(json.JSONEncoder):
    import datetime
    def default(self,obj):
        if isinstance(obj, (datetime.datetime, datetime.date, datetime.time)):
            return obj.isoformat()
        return super().default(obj)

if __name__ == "__main__":
    print("Import as module")