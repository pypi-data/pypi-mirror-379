from dataclasses import dataclass
from typing import List, Optional
import numpy as np
import pandas as pd

from .line import Pivot, Point

import logging
logger = logging.getLogger(__name__)

@dataclass
class Zigzag:
    def __init__(self, backcandles: int = 5, forwardcandles: int = 5,
                 pivot_limit: int = 20, offset: int = 0,
                 strong_trend_threshold: float = 0.1,
                 candle_direction_threshold: float = 0.05):
        self.backcandles = backcandles
        self.forwardcandles = forwardcandles
        self.pivot_limit = pivot_limit
        self.offset = offset
        self.strong_trend_threshold = strong_trend_threshold
        self.candle_direction_threshold = candle_direction_threshold
        self.zigzag_pivots: List[Pivot] = []
        self.df = None

    def update_pivot_properties(self, pivot: Pivot) -> 'Zigzag':
        """
        Update the properties of the pivot
        """
        if len(self.zigzag_pivots) > 1:
            dir = np.sign(pivot.direction)
            value = pivot.point.price
            last_pivot = self.zigzag_pivots[1]
            if last_pivot.point.index == pivot.point.index:
                raise ValueError(f"Last pivot index {last_pivot.point.index} "
                                 f"is the same as current pivot index {pivot.point.index}")
            pivot.index_diff = pivot.point.index - last_pivot.point.index
            last_value = last_pivot.point.price
            value_diff = value - last_value
            # Determine if trend is strong (2) or weak (1)
            if dir == 1 and value_diff > abs(last_value) * self.strong_trend_threshold:
                pivot.direction = 2
            elif dir == -1 and value_diff < -abs(last_value) * self.strong_trend_threshold:
                pivot.direction = -2

            # Calculate difference between last and current pivot
            pivot.value_diff = value_diff
            pivot.candle_body_diff = value - last_pivot.point.candle_body_price
            if len(self.zigzag_pivots) > 2:
                llast_pivot = self.zigzag_pivots[2]
                llast_value = llast_pivot.point.price
                # Calculate slope between last and current pivot
                pivot.cross_diff = value - llast_value
                pivot.cross_candle_body_diff = pivot.point.candle_body_price - \
                    llast_pivot.point.candle_body_price
                pivot.cross_index_diff = pivot.point.index - llast_pivot.point.index

    def add_new_pivot(self, pivot: Pivot) -> 'Zigzag':
        """
        Add a new pivot to the zigzag

        Args:
            pivot: Pivot object to add

        Returns:
            self: Returns zigzag object for method chaining

        Raises:
            ValueError: If direction mismatch with last pivot
        """
        if len(self.zigzag_pivots) >= 1:
            # Check direction mismatch
            if np.sign(self.zigzag_pivots[0].direction) == np.sign(pivot.direction):
                raise ValueError('Direction mismatch')

        # Insert at beginning and maintain max size
        self.zigzag_pivots.insert(0, pivot)
        self.update_pivot_properties(pivot)

        if len(self.zigzag_pivots) > self.pivot_limit:
            logger.warning(f"Warning: pivots exceeded limit {self.pivot_limit}, "
                           f"popping pivot {self.zigzag_pivots[-1].point.index}")
            self.zigzag_pivots.pop()

        return self

    def calculate(self, df: pd.DataFrame, offset: Optional[int] = None) -> 'Zigzag':
        """
        Calculate zigzag pivots from DataFrame

        Args:
            df: DataFrame with 'high' and 'low' columns
            offset: Offset to apply to the dataframe index
        Returns:
            self: Returns zigzag object for method chaining
        """
        if offset is not None:
            self.offset = offset

        # rescale the dataframe using the max and low prices in the range
        if df.get('high') is None or df.get('low') is None:
            raise ValueError("High and low prices not found in dataframe")

        self.zigzag_pivots = []

        highs, lows = window_peaks(df, self.backcandles, self.forwardcandles)

        # Calculate pivot highs
        pivot_highs = df['high'].where((df['high'] == highs))
        volume_hights = df['volume'].where((df['high'] == highs))

        # Calculate pivot lows
        pivot_lows = df['low'].where((df['low'] == lows))
        volume_lows = df['volume'].where((df['low'] == lows))

        # Process pivot points into zigzag
        last_pivot_price = None
        last_pivot_direction = 0

        for i in range(len(df)):
            if not (pd.isna(pivot_highs.iloc[i]) and pd.isna(pivot_lows.iloc[i])):
                current_index = i + self.offset
                current_time = df.index[i]
                candle_len = df.iloc[i]['high'] - df.iloc[i]['low']
                if pd.isna(candle_len) or candle_len == 0 or \
                    abs(df.iloc[i]['close'] - df.iloc[i]['open']) / candle_len \
                     < self.candle_direction_threshold:
                    candle_direction = 0
                else:
                    candle_direction = int(np.sign(df.iloc[i]['close'] - df.iloc[i]['open']))
                take_high = True
                if not pd.isna(pivot_highs.iloc[i]) and not pd.isna(pivot_lows.iloc[i]):
                    # both high and low pivot, take the more extreme one
                    if last_pivot_price is not None:
                        assert last_pivot_direction != 0
                        if last_pivot_direction == 1:
                            if pivot_highs.iloc[i] <= last_pivot_price:
                                # the current pivot high is lower than the last pivot high, take low instead
                                take_high = False
                        else:
                            if pivot_lows.iloc[i] < last_pivot_price:
                                # the current pivot low is lower than the last pivot low, take low instead
                                take_high = False
                elif pd.isna(pivot_highs.iloc[i]):
                    take_high = False

                if take_high:
                    current_price = pivot_highs.iloc[i]
                    current_volume = volume_hights.iloc[i]
                    candle_body_price = max(df.iloc[i]['open'], df.iloc[i]['close'])
                    current_direction = 1 # bullish
                else:
                    current_price = pivot_lows.iloc[i]
                    current_volume = volume_lows.iloc[i]
                    candle_body_price = min(df.iloc[i]['open'], df.iloc[i]['close'])
                    current_direction = -1 # bearish

                # Create and add pivot if valid
                if last_pivot_price is None or last_pivot_direction != current_direction:
                    new_pivot = Pivot(
                        point=Point(
                            price=current_price,
                            volume=current_volume,
                            candle_body_price=candle_body_price,
                            candle_direction=candle_direction,
                            index=current_index,
                            time=current_time
                        ),
                        direction=current_direction
                    )

                    self.add_new_pivot(new_pivot)
                    last_pivot_price = current_price
                    last_pivot_direction = current_direction

                # Update last pivot if same direction but more extreme
                elif ((current_direction == 1 and current_price > last_pivot_price) or
                    (current_direction == -1 and current_price < last_pivot_price)):
                    # Update the last pivot
                    last_pivot = self.zigzag_pivots[0]
                    last_pivot.point.price = current_price
                    last_pivot.point.volume = current_volume
                    last_pivot.point.candle_body_price = candle_body_price
                    last_pivot.point.candle_direction = candle_direction
                    last_pivot.point.index = current_index
                    last_pivot.point.time = current_time
                    self.update_pivot_properties(last_pivot)
                    last_pivot_price = current_price

        # record the dataframe
        self.df = df.copy()

        return self

    def get_pivot_by_index(self, index: int) -> Optional[Pivot]:
        """Get pivot at specific index"""
        for i in range(len(self.zigzag_pivots)):
            current_pivot = self.zigzag_pivots[len(self.zigzag_pivots) - i - 1]
            if current_pivot.point.index == index:
                return current_pivot
        return None

    def get_pivot(self, offset: int) -> Optional[Pivot]:
        """Get pivot at specific index"""
        if 0 <= offset < len(self.zigzag_pivots):
            return self.zigzag_pivots[offset]
        return None

    def get_last_pivot(self) -> Optional[Pivot]:
        """Get the most recent pivot"""
        return self.zigzag_pivots[0] if self.zigzag_pivots else None

    def get_df_data_by_index(self, index: int) -> pd.Series:
        """Get the dataframe data at a specific index"""
        if self.df is not None:
            if index < self.offset or index - self.offset >= len(self.df):
                raise ValueError(f"Index {index} is out of bounds")
            return self.df.iloc[index - self.offset]
        raise ValueError("DataFrame not calculated")

def window_peaks(data, before: int, after: int) -> tuple[pd.Series, pd.Series]:
    """
    Faster version using numpy's stride tricks

    Args:
        df: DataFrame with 'high' and 'low' columns
        before: Number of bars before the current bar
        after: Number of bars after the current bar

    Returns:
        pd.Series: Series of highs and lows
    """
    if isinstance(data, pd.DataFrame):
        if data.empty or 'high' not in data or 'low' not in data:
            raise ValueError("DataFrame is empty or missing 'high'/'low' columns")
        values_high = data["high"].values
        values_low = data["low"].values
    elif isinstance(data, pd.Series):
        if data.empty:
            raise ValueError("Series is empty")
        values_high = data.values
        values_low = data.values
    else:
        raise ValueError("Unsupported dataframe type")

    if len(values_high) == 0 or len(values_low) == 0:
        raise ValueError("Input data is empty")

    result_high = np.zeros(len(values_high))
    result_low = np.zeros(len(values_low))

    # Handle edges with padding
    padded_high = np.pad(values_high, (before, after), mode='edge')
    padded_low = np.pad(values_low, (before, after), mode='edge')

    # Create rolling window view
    windows_high = np.lib.stride_tricks.sliding_window_view(padded_high, before + after + 1)
    windows_low = np.lib.stride_tricks.sliding_window_view(padded_low, before + after + 1)
    result_high = np.max(windows_high, axis=1)
    result_low = np.min(windows_low, axis=1)

    return pd.Series(result_high, index=data.index), pd.Series(result_low, index=data.index)
