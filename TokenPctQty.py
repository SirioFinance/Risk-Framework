def calculate_token_quantity_to_move_price_weighted(pools, price_change_percentage):
    """
    Calculate the total quantity of tokens needed to change the price by a specified percentage across multiple liquidity pools,
    weighting the impact of each pool based on its liquidity relative to the total liquidity.
    
    Args:
        pools (list of dicts): Each dict should contain 'token_x' (quantity of token A) and 'token_y' (quantity of the other asset, e.g., USDC)
        price_change_percentage (float): Desired price change percentage (e.g., 0.25 for a 25% price change)
    
    Returns:
        float: Total quantity of tokens needed to change the price across all pools, weighted by liquidity.
    """
    total_liquidity = 0  # Total market liquidity (sum of all token_x and token_y across pools)
    total_token_quantity = 0  # Total tokens needed to move the price

    # Calculate the new price factor (e.g., for a 25% price change, this is 1.25)
    price_factor = 1 + price_change_percentage

    # Step 1: Calculate total liquidity in the market (sum of all token_x and token_y)
    for pool in pools:
        total_liquidity += pool['token_x'] + pool['token_y']

    # Step 2: Calculate token quantity needed for each pool, weighted by its liquidity
    for pool in pools:
        token_x = pool['token_x']  # Quantity of token A in the pool
        token_y = pool['token_y']  # Quantity of USDC or the other asset

        # Initial price: token_y / token_x
        price_initial = token_y / token_x

        # Desired final price after the change
        price_final = price_initial * price_factor

        # Calculate the quantity of token A needed to reach the new price
        delta_x = (token_y / price_final) - token_x

        # Weight this quantity based on the pool's liquidity relative to the total liquidity
        pool_liquidity = token_x + token_y
        weight = pool_liquidity / total_liquidity

        # Add the weighted token quantity to the total
        total_token_quantity += abs(delta_x) * weight

    return total_token_quantity


# Example usage
pools = [
    {"token_x": 78, "token_y": 2000},  # Pool 1: 1000 token A, 2000 USDC
    {"token_x": 500, "token_y": 1000},   # Pool 2: 500 token A, 1000 USDC
    {"token_x": 1500, "token_y": 3000}   # Pool 3: 1500 token A, 3000 USDC
]

price_change_percentage = 0.25  # 25% price change

# Calculate the total token quantity needed, weighted by pool liquidity
total_quantity_needed = calculate_token_quantity_to_move_price_weighted(pools, price_change_percentage)

print(f"Total token quantity needed to change the price by 25% (weighted): {total_quantity_needed}")
