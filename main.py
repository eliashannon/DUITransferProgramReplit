from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    # Get form data
    name = request.form['name']
    num_education = int(request.form['num_education'])
    num_group = int(request.form['num_group'])
    num_face_to_face = int(request.form['num_face_to_face'])
    num_reentry = int(request.form['num_reentry'])
    from_ventura = request.form['from_ventura']

    # Fixed costs
    transfer_fee = 75
    education_cost = 17
    group_cost = 54
    face_to_face_cost = 25
    reentry_cost = 80
    ventura_fee = 50 if from_ventura == "no" else 0

    # Calculations
    total_education = num_education * education_cost
    total_group = num_group * group_cost
    total_face_to_face = num_face_to_face * face_to_face_cost
    total_reentry = num_reentry * reentry_cost
    total = total_education + total_group + total_face_to_face + total_reentry + transfer_fee + ventura_fee

    return render_template('results.html',
                         name=name,
                         num_education=num_education,
                         num_group=num_group,
                         num_face_to_face=num_face_to_face,
                         num_reentry=num_reentry,
                         from_ventura=from_ventura,
                         education_cost=education_cost,
                         group_cost=group_cost,
                         face_to_face_cost=face_to_face_cost,
                         reentry_cost=reentry_cost,
                         total_education=total_education,
                         total_group=total_group,
                         total_face_to_face=total_face_to_face,
                         total_reentry=total_reentry,
                         transfer_fee=transfer_fee,
                         ventura_fee=ventura_fee,
                         total=total)

if __name__ == '__main__':
    print("Starting Flask app on port 5000...")
    app.run(host='0.0.0.0', port=5000, debug=True)