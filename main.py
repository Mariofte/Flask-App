import os
from core import Web

path = os.path.dirname(os.path.abspath(__file__))

web = Web(
    __name__,
    os.path.join(path, 'static'),
    os.path.join(path, 'templates')
)

if __name__ == '__main__':
    web.run(host='localhost', port=4400, debug=True)