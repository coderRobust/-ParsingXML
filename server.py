# Using flask to make an api
# import necessary libraries and functions
from flask import Flask, jsonify, request
from utils.xml_parsing import xml_data_parsing

# creating a Flask app
app = Flask(__name__)

# A function to get Parsed XML data
@app.route('/xmlParsedData', methods = ['GET'])
def getXmlParsedData():
	data = xml_data_parsing()
	print(data)
	return "Successfully Parsed"


# driver function
if __name__ == '__main__':
	app.run(debug = True)