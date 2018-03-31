from flask import Flask, request, render_template
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form="""<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form method="POST">
            Rotate By : <input value="0" name="rot">
			<textarea name="text" rows="4" cols="50">{0}</textarea>
            <input value="Submit Query" type="submit">
        </form>
    </body>
</html>"""

@app.route("/")
def index():
    return form.format("")
    #return render_template('form.html')


@app.route('/', methods=['POST'])
def encrypt():
    rot = int(request.form['rot'])
    text = request.form['text']
    enc=rotate_string(text,rot)
    #return enc
    #return rotate_string(text,rot)
    return form.format(enc)
    

app.run()