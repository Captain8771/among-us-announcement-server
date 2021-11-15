import flask as f
app = f.Flask(__name__)

app.default = """
<size=300%>Hello!</size>
It seems that the creator of this among us mod hasnt set up the custom among us announcement server, or there was an error!
check again later!

<i>If you are the creator of this mod, please check your announcements server</i>
"""

app.announcement = None  # change me

@app.route("/api/announcement")
async def announcement():
    return f.jsonify({
          "data": {
            "type": "announcement",
            "attributes": {
              "id": 69,
              "text": app.announcement or app.default
            }
          }
        })

app.run("127.0.0.1", port=8771)
