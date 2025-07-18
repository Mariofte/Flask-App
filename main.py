import os
from core import Web

web = Web(
    __name__,
    os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static'),
    os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
)

if __name__ == '__main__':
    web.run(host='localhost', port=4400, debug=True)