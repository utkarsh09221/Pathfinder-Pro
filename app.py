from flask import Flask, render_template, request, redirect, url_for
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('webpage.html')

@app.route('/open_autogenrate_console')
def open_autogenrate_console():
    try:
        # Run the script directly in the background
        subprocess.Popen(["python3", "autogenrate.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return redirect(url_for('visiual'))
    except Exception as e:
        return f"Error: {e}", 500

@app.route('/open_megenrate_console')
def open_megenrate_console():
    try:
        subprocess.Popen(["python3", "megenrate.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return redirect(url_for('visiual'))
    except Exception as e:
        return f"Error: {e}", 500

if __name__ == '__main__':
    app.run(debug=True)
