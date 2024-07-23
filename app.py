from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
import json


app = Flask(__name__)
CORS(app)

@app.route('/process_task', methods=['POST'])
def process_task():
    data = request.json
    task_name = data['task_name']
    path = 'E:/aolabs/aolabs2/ARC-AGI/data/training/'+str(task_name)

    
    # pred_array = np.random.rand(10, 10).tolist()
    test_file = open(path)
    test_data = json.load(test_file)

    

    # pred_array = test_data['train']
    pred_array = []
    for pair in test_data['test']:
        onp = (pair['output'])
        pred_array.append(onp)
       
   
    return jsonify(pred_array=pred_array)

if __name__ == '__main__':
    app.run(debug=True)

