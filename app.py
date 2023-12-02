from flask import Flask,request


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
        result=int(number1)+int(number2)
    elif opreation=="multiply":
        result=int(number1)*int(number2)
    elif opreation=="devision":
        result=int(number1)/int(number2)
    else:
        result=int(number1)-int(number2)
    return "The given operation {} and the result is {}".format(operation,result)


print(__name__)
if __name__=="__main__":
    app.run()