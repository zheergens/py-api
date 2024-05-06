from app.v1.view import template
from flask import  render_template, g


@template.route('/tool', methods=['GET'])
def prescriptionFetch():
    msg = "my name is me, China up!"
    s = g.db.mongo.test.find_one()
    msg = s['key']
    return render_template("v1_tool.html", data=msg)
