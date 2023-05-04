from app.v1.view import template
from flask import  render_template


@template.route('/tool/html', methods=['GET'])
def prescriptionFetch():
    msg = "my name is me, China up!"
    return render_template("v1_tool.html", data=msg)
