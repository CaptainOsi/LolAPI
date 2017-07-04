from flask import Flask
from flask.json import JSONEncoder
from datetime import date

app = Flask(__name__)


class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):
        try:
            if isinstance(obj, date):
                return obj.isoformat()
            iterable = iter(obj)
        except TypeError:
            pass
        else:
            return list(iterable)
        return JSONEncoder.default(self, obj)


app.json_encoder = CustomJSONEncoder

from Controller.NewsController import *
from Controller.SalesController import *
from Controller.FreechampController import *

if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=80
    )
