import random
from flask import Flask, render_template, request

app = Flask(__name__)

options = ("steen", "papier", "schaar")


@app.route("/", methods=["GET", "POST"])
def home():
    player = None
    computer = None
    result = None

    if request.method == "POST":

        # Haal jouw keuze uit het formulier
        player = request.form.get("choice")

        # De computer kiest automatisch
        computer = random.choice(options)

        # Bepaal wie er wint
        if player == computer:
            result = "Gelijkspel!"

        elif (
            (player == "steen" and computer == "schaar")
            or (player == "papier" and computer == "steen")
            or (player == "schaar" and computer == "papier")
        ):
            result = "Je hebt gewonnen!"

        else:
            result = "De computer heeft gewonnen!"

    return render_template(
        "steen.html",
        player=player,
        computer=computer,
        result=result
    )


if __name__ == "__main__":
    app.run(debug=True)