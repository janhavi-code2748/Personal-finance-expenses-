from flask import Flask, render_template, request

app = Flask(__name__)

expenses = []

@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        date = request.form["date"]
        category = request.form["category"]
        description = request.form["description"]
        amount = float(request.form["amount"])

        expense = {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }

        expenses.append(expense)

    # Calculate total spending
    total = sum(e["amount"] for e in expenses)

    # Calculate category summary
    summary = {}

    for e in expenses:
        cat = e["category"]

        if cat in summary:
            summary[cat] += e["amount"]
        else:
            summary[cat] = e["amount"]

    return render_template(
        "index.html",
        expenses=expenses,
        total=total,
        summary=summary
    )

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0"
