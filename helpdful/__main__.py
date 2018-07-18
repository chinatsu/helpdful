from helpdful import helpdful
from flask import Flask, make_response
from time import time

app = Flask(__name__)

@app.route('/')
def test():
    file = "test"
    now = time()
    pdf = helpdful.Helpdful(name=file).render()
    print("PDF generation took {} ms".format((time() - now)*1000))
    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'inline; filename={}.pdf'.format(file)
    return response


if __name__ == "__main__":
    app.run("0.0.0.0", port=3000)
