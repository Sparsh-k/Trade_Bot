def validate_input(symbol, side, order_type, quantity, price):
    #### Validate side input
    if side not in ["BUY", "SELL"]:
        raise ValueError("Invalid side")

    #### Validate order type input
    if order_type not in ["MARKET", "LIMIT"]:
        raise ValueError("Invalid order type")

    #### Validate price when order type is "Limit"
    if order_type == "LIMIT" and price is None:
        raise ValueError("Price required for LIMIT order")