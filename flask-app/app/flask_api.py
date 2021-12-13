from BMI_calculator import bmi_result
from flask import Flask, jsonify, request

# instantiating a flask object
app = Flask('__name__')


@app.route('/', methods=['GET', 'POST'])
def bmi_score():
    """function to get and display the weight and heights entered,
    as well as the BMI value resulting from the BMI calculation using the
    provided weight and height"""

    packet = request.get_json(force=True)
    weight = packet["weight"]
    height = packet["height"]

    bmi = bmi_result(weight, height)

    return jsonify(bmi)


# driver function
if __name__ == '__main__':
    app.run()
