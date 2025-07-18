from flask import Flask,render_template,request,redirect,url_for,jsonify

app=Flask(__name__)

@app.route("/",methods=["GET"])
def welcome():
    return "Welcome"


@app.route("/index",methods=["GET"])
def index():
    return "Welcome to index page"

#variable rule - defining datatype specifically 
@app.route("/success/<int:score>")
def success(score):
    return "The person has passed the exam with score : " + str(score)

@app.route("/fail/<int:score>")
def fail(score):
    return "The person has failed the exam with score : " + str(score)

@app.route("/form",methods=["GET","POST"])
def form():
    if request.method == 'GET':
        return render_template('form.html')
    else:
        maths= float(request.form['maths'])
        science= float(request.form['science'])
        history= float(request.form['history'])

        average_score = (maths + science + history)/3
        res=''
        if average_score >= 40:
            res='success'
        else:
            res='fail'

        return redirect(url_for(res,score = average_score))

        ## return render_template('calculate.html',score = average_score)

@app.route("/api",methods =["POST"])
def calculate():
    data = request.get_json()
    a_val = float(dict(data)['a'])
    b_val = float(dict(data)['b'])
    return jsonify(a_val + b_val)

if __name__ == '__main__':
    app.run(debug=True)