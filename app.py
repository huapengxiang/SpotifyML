from flask import request
from flask import Flask, jsonify
import pickle


app = Flask(__name__)

#load model
model = pickle.load(open('decision_tree_model.pkl', 'r'))

#define route with post request
@app.route('/', methods=["POST"])
def index():
	# get array of features from post requests
	features = request.get_json()

	#creating a response object
    #storing the model's prediction in the object
	response = {}
	response['predictions'] = model.predict([features]).tolist()

	return jsonify(response)

if __name__ == '__main__':
	app.run(debug=True)