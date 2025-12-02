"""CP1404/CP5632 Practical - Simple Flask demo with greeting and temperature conversion."""

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    """Display a simple Hello World heading."""
    return "<h1>Hello World :)</h1>"


@app.route("/greet")
@app.route("/greet/<name>")
def greet(name=""):
    """Greet the given name or a generic greeting if no name is provided."""
    if not name:
        return "Hello"
    return f"Hello {name}"


def celsius_to_fahrenheit(celsius):
    """Convert Celsius temperature to Fahrenheit."""
    return celsius * 9.0 / 5 + 32


@app.route("/convert/<celsius>")
def convert(celsius):
    """Show Fahrenheit result for a Celsius value passed via the URL."""
    try:
        celsius_value = float(celsius)
    except ValueError:
        return f"'{celsius}' is not a valid number."
    fahrenheit_value = celsius_to_fahrenheit(celsius_value)
    return f"{celsius_value}°C is {fahrenheit_value:.1f}°F"


if __name__ == "__main__":
    app.run()
