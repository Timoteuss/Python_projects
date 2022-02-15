from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route("/")
def bochka_1():

    return "Thr first flask page"

@app.route("/test_method_get", methods=["GET"])
def bochka_2():

    p1 = int(request.args.get('salary'))
    p2 = request.args.get('name')

    resp = {'name': p2,
            'salary': p1,
            'salary_4_years': p1*5}

    return jsonify(resp)


@app.route("/test_method_post", methods=["POST"])
def bochka_3():
    p1 = int(request.form.get('salary'))
    p2 = request.form.get('name')
    p3 = request.form.get('age')

    p4 = request.args.get('salary')


    resp = {'name': p2,
            'salary': p1,
            'salary_4_years': p1 * 5,
            'age': p3,
            'url_salary': p4}

    return jsonify(resp)
