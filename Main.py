import typer
from Trade_Bot.Bot.Orders import place_order
from Trade_Bot.Bot.Validators import validate_input
from Trade_Bot.Bot.Logging import setup_logger
import logging

setup_logger()

app = typer.Typer()

@app.command()
def trade(
    symbol: str = typer.Option(...),
    side: str = typer.Option(...),
    order_type: str = typer.Option(...),
    quantity: float = typer.Option(...),
    price: float = typer.Option(None)
):
    #### Returning Results or else returing error state
    try:
        validate_input(symbol, side, order_type, quantity, price)

        logging.info(f"Placing order: {symbol} {side} {order_type}")

        result = place_order(symbol, side, order_type, quantity, price)

        print("Order Response:", result)
        logging.info(f"Response: {result}")

    except Exception as e:
        print("Error:", e)
        logging.error(str(e))

if __name__ == "__main__":
    app()