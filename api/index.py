from flask import Flask, render_template
import os

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    template_path = os.path.join(app.template_folder, 'index.html')
    return render_template(template_path)

# Note: The following block is removed for Vercel deployment.
# if __name__ == '__main__':
#     app.run()
