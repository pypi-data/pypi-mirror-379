from numba import njit
import numpy as np
from typing import Tuple


@njit
def volume_profile_features(prices: np.ndarray, volumes: np.ndarray, n_bins: int = 20) -> Tuple[float, float]:
    """
    Extract POC (Point of Control) and its normalized position within the price range.

    Parameters
    ----------
    prices : np.ndarray
        1D array of price values corresponding to each tick.
    volumes : np.ndarray
        1D array of traded volume at each tick.
    n_bins : int, default=20
        Number of price bins to use for the volume profile.

    Returns
    -------
    Tuple[float, float]
        - poc_price : Price level with the highest accumulated volume.
        - poc_position : Normalized position of POC between min and max price (range 0–1).
    """
    price_min = prices.min()
    price_max = prices.max()
    bin_edges = np.linspace(price_min, price_max, n_bins + 1)
    volume_per_bin = np.zeros(n_bins)

    for i in range(prices.shape[0]):
        price = prices[i]
        volume = volumes[i]

        for j in range(n_bins):
            if bin_edges[j] <= price < bin_edges[j + 1]:
                volume_per_bin[j] += volume
                break
            elif j == n_bins - 1 and price == bin_edges[-1]:
                volume_per_bin[j] += volume
                break

    max_idx = np.argmax(volume_per_bin)
    poc_price = (bin_edges[max_idx] + bin_edges[max_idx + 1]) / 2

    poc_position = (poc_price - price_min) / (price_max - price_min) if price_max > price_min else 0.0

    return poc_price, poc_position


@njit
def max_traded_volume(prices: np.ndarray, volumes: np.ndarray) -> Tuple[float, float]:
    """
    Return the maximum traded volume and the associated price.

    Parameters
    ----------
    prices : np.ndarray
        1D array of price values corresponding to each tick.
    volumes : np.ndarray
        1D array of traded volume at each tick.

    Returns
    -------
    Tuple[float, float]
        - max_volume : Highest volume exchanged on a single tick.
        - price_at_max_volume : Price level at which the maximum volume occurred.
    """
    n = len(volumes)
    if n == 0:
        return 0.0, 0.0

    max_idx = 0
    max_vol = volumes[0]

    for i in range(1, n):
        if volumes[i] > max_vol:
            max_vol = volumes[i]
            max_idx = i

    return max_vol, prices[max_idx]