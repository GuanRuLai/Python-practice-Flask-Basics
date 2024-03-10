from flask import Flask, request, render_template, redirect, url_for

# create flask app
app = Flask(__name__)

@app.route("/form")
def formPage():
    return render_template("Form.html")

@app.route("/submit", methods = ["POST", "GET"])
def submit():
    if request.method == "POST":
        user = request.form["user"] # extract user data from form submission
        print("post : user => ", user) 
        return redirect(url_for("success", name=user, action="post")) # redirect to success route with user data

    else:
        user = request.args.get("user") # extract user data from URL parameters
        print("get : user => ", user)
        return redirect(url_for("success", name=user, action="get")) # redirect to success route with user data

@app.route("/success/<action>/<name>")
def success(name, action):
    return "{} : Welcome {} ~ !!".format(action, name)

if __name__ == "__main__":
    app.run(debug=True)


#%%
