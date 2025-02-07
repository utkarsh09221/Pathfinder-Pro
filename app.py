import subprocess
from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('webpage.html')

@app.route('/open_autogenrate_console')
def open_autogenrate_console():
    try:
        # Run the script directly as a background process
        process = subprocess.Popen(
            ["python3", "autogenrate.py"], 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE
        )
        return redirect(url_for('visiual'))
    except Exception as e:
        return f"Error running autogenrate.py: {e}", 500

@app.route('/open_megenrate_console')
def open_megenrate_console():
    try:
        process = subprocess.Popen(
            ["python3", "megenrate.py"], 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE
        )
        return redirect(url_for('visiual'))
    except Exception as e:
        return f"Error running megenrate.py: {e}", 500

if __name__ == '__main__':
    app.run(debug=True)

