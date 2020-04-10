from flask import Flask
from funcs.token_verify import token_verify_service
from utils import *


app = Flask(__name__)
app.json_encoder = CustomJSONEncoder
app.register_blueprint(token_verify_service)




if __name__ == '__main__':
	app.run(debug=True)
