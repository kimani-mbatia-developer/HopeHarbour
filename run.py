from backend import app, app_swagger
from backend.models.common import db

if __name__ == "__main__":
    app.run()
    app_swagger.run(port=5000, debug=True)
