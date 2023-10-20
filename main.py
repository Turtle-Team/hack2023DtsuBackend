
import flask_app
import swagger
import swagger.route
import settings
from flask_cors import CORS

if __name__ == '__main__':
    app = flask_app.app
    CORS(app)
    app.run(host=settings.FLASK_IP, debug=False, port=settings.FLASK_PORT)


