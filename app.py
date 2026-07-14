import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)


data = pd.read_csv("property_data.csv")

@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        
        location = request.form["location"].strip()
        price = float(request.form["price"])
        years = int(request.form["years"])

        
        result = data[data["Location"].str.lower() == location.lower()]

       
        if not result.empty:

            
            growth_rate = result.iloc[0]["GrowthRate"]

            
            future_value = price * (1 + growth_rate / 100) ** years

            
            profit = future_value - price

            
            if growth_rate >= 11:
                rating = "Excellent Investment"
            elif growth_rate >= 8:
                rating = "Good Investment"
            else:
                rating = "Stable Investment"

            return f"""
PROPERTY ANALYSIS
<pre>
Location: {location}

Historical Growth Rate: {growth_rate}%

Current Price: ₹{price:,.2f}

Predicted Future Value: ₹{future_value:,.2f}

Estimated Profit: ₹{profit:,.2f}

Investment Rating: {rating}
</pre>
"""

        else:
            return "Location not found in dataset."

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)