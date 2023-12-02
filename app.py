from flask import Flask,request,render_template


app=Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to the Flask class"

@app.route("/cal",methods=["GET"])
def math_operator():
    opreation=request.json["operation"]
    number1=request.json["number1"]
    number2=request.json["number2"]

    if opreation=="add":
        result=number1+number2
    elif opreation=="multiply":
        result=number1*number2
    elif opreation=="devision":
        result=number1/number2
    else:
        result=number1-number2
    return result


print(__name__)
if __name__=="__main__":
    app.run()