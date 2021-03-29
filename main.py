from flask import Flask, render_template
from flask import request
import i2clcda
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def server():
    page = '''<form method="POST">
        Write a message :<br>
        <input type="text" name="tag" maxlength="16"><br>
        <input type="text" name="tag2" maxlength="16"><br>
        <input type="submit" value="Display">
        </form>'''
    if request.method != 'POST':
        return page

    tag = request.form['tag']
    tag2 = request.form['tag2']
    i2clcda.main(tag, tag2)
    return page


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=False)
