"""Learning exercise: illustrative fuel cost estimate, not a live price feed."""

import math

EFFICIENCY_KM_PER_LITRE = 10.0

try:
    distance_km = float(input("Distance (km): "))
    price_per_litre = float(input("Fuel price (R/litre): "))
except ValueError:
    print("Please enter numeric values.")
else:
    if (
        not math.isfinite(distance_km)
        or not math.isfinite(price_per_litre)
        or distance_km < 0
        or price_per_litre <= 0
    ):
        print("Enter a non-negative distance and a positive, finite fuel price.")
    else:
        litres = distance_km / EFFICIENCY_KM_PER_LITRE
        cost = litres * price_per_litre
        print(f"Fuel required: {litres:.2f} litres")
        print(f"Estimated cost: R{cost:.2f}")
