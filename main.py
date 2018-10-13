from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

page_header = """
    <!DOCTYPE html>
    <html>
        <head>
            <title>Web Caesar</title>
        </head>
        <body>
"""

page_footer = """
        </body>
    </html>
"""

form = """
    <!DOCTYPE html>
    <html>
        <head>
            <style>
                form {
                    background-color: #eee;
                    padding: 20px;
                    width: 540px;
                    font: 16px sans-serif;
                    border-radius: 10px;
                }
                textarea {
                    margin: 10px 0;
                    width: 540px;
                    height: 120px;
                }
            </style>
        </head>
        <body>
            <form action="/" method="post">
                <label for="rot">
                    Rotate by: 
                    <input type="text" name="rot" id="rot" value="0"/>
                </label>
                <textarea name="text"></textarea>
                <input type="submit" value="Submit">
            </form>
        </body>
    </html>
"""

@app.route("/")
def index():
    return form

@app.route("/", methods=['POST'])
def encrypt():
    user_rot = request.form['rot']
    user_rot = int(user_rot)
    user_message = request.form['text']

    # run request variables through function
    new_message = rotate_string(user_message, user_rot)
    content = page_header + "<h1>" + new_message + "</h1>" + page_footer

    return content

app.run()