from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import List, Tuple, Optional
import numpy as np
import pandas as pd
from .line import Point, Pivot, Line
from .zigzag import Zigzag
from .chart_pattern import ChartPattern, ChartPatternProperties, get_pivots_from_zigzag, \
    is_same_height, volume_exceeds

import logging
logger = logging.getLogger(__name__)

@dataclass
class TrendLineProperties(ChartPatternProperties):
    # minimum number of pivots to form a pattern
    number_of_pivots: int = 5
    # minimum number of periods lapsed between pivots
    min_periods_lapsed: int = 21
    # maximum allowed flat ratio between flat trend lines
    flat_ratio: float = 0.1
    # maximum allowed ratio between aligned diagonal pivots
    align_ratio: float = 0.4
    # maximum allowed ratio between parallel trend lines
    parallel_ratio: float = 0.1
    # maximum apex span for triangle patterns
    max_apex_periods: int = 150
    # maximum allowed candle body crosses for a valid trend line
    max_candle_body_crosses: int = 1
    # check if the volume matches the pattern
    enable_volume_check: bool = False
    # major volume percentage difference percentage
    major_volume_diff_pct: float = 0.1
    # minor volume percentage difference percentage
    minor_volume_diff_pct: float = 0.02

class TrendLinePattern(ChartPattern):
    apex: Point = None
    target_price_delta: float = 0

    def __init__(self, pivots: List[Pivot], trend_line1: Line, trend_line2: Line):
        self.pivots = pivots
        self.trend_line1 = trend_line1
        self.trend_line2 = trend_line2
        self.extra_props = {}

    @classmethod
    def from_dict(cls, dict):
        self = cls(pivots=[Pivot.from_dict(p) for p in dict["pivots"]],
                   trend_line1=Line.from_dict(dict["trend_line1"]),
                   trend_line2=Line.from_dict(dict["trend_line2"]))
        self.target_price_delta = dict["target_price_delta"]
        if "apex" in dict:
            self.apex = Point.from_dict(dict["apex"])
        self.pattern_type = dict["pattern_type"]
        self.pattern_name = dict["pattern_name"]
        return self

    def dict(self):
        obj = super().dict()
        obj["trend_line1"] = self.trend_line1.dict()
        obj["trend_line2"] = self.trend_line2.dict()
        obj["target_price_delta"] = self.target_price_delta
        if self.apex is not None:
            obj["apex"] = self.apex.dict()
        return obj

    def get_pattern_name_by_id(self, id: int) -> str:
        pattern_names = {
            1: "Ascending Channel",
            2: "Descending Channel",
            3: "Ranging Channel",
            4: "Ranging Channel (Bullish)",
            5: "Ranging Channel (Bearish)",
            6: "Diverging Triangle",
            7: "Converging Triangle (Bullish)",
            8: "Converging Triangle (Bearish)",
            9: "Rising Wedge (Contracting)",
            10: "Falling Wedge (Contracting)",
            11: "Converging Triangle",
            12: "Descending Triangle (Contracting)",
            13: "Ascending Triangle (Contracting)",
        }
        return pattern_names.get(id, "Error")

    def get_apex(self, start_index: int, start_time: datetime,
                 interval: timedelta, max_apex_periods: int) -> Optional[Point]:
        """Get the apex point of the pattern if two trend lines converge"""
        if self.pivots[0].direction > 0:
            upper_line = self.trend_line1
            lower_line = self.trend_line2
        else:
            upper_line = self.trend_line2
            lower_line = self.trend_line1
        for i in range(1, max_apex_periods):
            index = start_index + i
            p1 = upper_line.get_price(index)
            p2 = lower_line.get_price(index)
            if p1 <= p2:
                return Point(index=index, time=start_time + i * interval, price=p1)
        return None

    def check_volume(self, properties: TrendLineProperties) -> int:
        if self.pivots[-1].direction > 0:
            up_pivot = self.pivots[-1]
            down_pivot = self.pivots[-2]
        else:
            up_pivot = self.pivots[-2]
            down_pivot = self.pivots[-1]
        if up_pivot.point.candle_direction > 0:
            if down_pivot.point.candle_direction < 0:
                up_volume_pivot = up_pivot
                down_volume_pivot = down_pivot
            else:
                return 1
        elif up_pivot.point.candle_direction < 0:
            if down_pivot.point.candle_direction > 0:
                up_volume_pivot = down_pivot
                down_volume_pivot = up_pivot
            else:
                return -1
        else:
            if down_pivot.point.candle_direction < 0:
                return -1
            elif down_pivot.point.candle_direction > 0:
                return 1
            else:
                return 0
        logger.debug(f"Up pivot {up_volume_pivot.point.index}: "
                     f"candle direction {up_volume_pivot.point.candle_direction}, "
                     f"volume {up_volume_pivot.point.volume}, "
                     f"Down pivot {down_volume_pivot.point.index}: "
                     f"candle direction {down_volume_pivot.point.candle_direction}, "
                     f"volume {down_pivot.point.volume}")
        if volume_exceeds(up_volume_pivot.point.volume, down_volume_pivot.point.volume,
                                    properties.major_volume_diff_pct):
            return 1
        elif volume_exceeds(down_volume_pivot.point.volume, up_volume_pivot.point.volume,
                                    properties.minor_volume_diff_pct):
            return -1
        else:
            return 0

    def check_profit_triangle(self, is_bullish: bool, properties: TrendLineProperties) -> bool:
        """Check if the profit is greater than the minimum profit"""
        if self.apex is None:
            raise ValueError("Apex point should not be None for triangle pattern!")
        else:
            support_price = self.apex.price
            resistance_price = self.apex.price
            self.target_price_delta = min(abs(self.pivots[0].value_diff),
                                     abs(self.trend_line1.p1.price - self.trend_line2.p1.price))
            return self.calculate_profit_ratio(support_price, resistance_price,
                                               self.target_price_delta, is_bullish, properties)

    def check_profit_channel(self, is_bullish: bool, properties: TrendLineProperties) -> bool:
        """Check if the profit is greater than the minimum profit"""
        if self.pivots[0].direction > 0:
            support_price = self.trend_line1.p2.price
            resistance_price = self.trend_line2.p2.price
        else:
            support_price = self.trend_line2.p2.price
            resistance_price = self.trend_line1.p2.price
        self.target_price_delta = min(abs(self.pivots[0].value_diff),
                                 abs(self.trend_line1.p1.price - self.trend_line2.p1.price))
        return self.calculate_profit_ratio(support_price, resistance_price,
                                           self.target_price_delta, is_bullish, properties)

    def calculate_profit_ratio(self, support_price: float, resistance_price: float,
                                target_price_delta: float, is_bullish: bool,
                                properties: TrendLineProperties) -> float:
        if is_bullish:
            return target_price_delta >= support_price * properties.min_profit_pct
        else:
            return target_price_delta >= resistance_price * properties.min_profit_pct

    def resolve(self, properties: TrendLineProperties) -> 'TrendLinePattern':
        self.resolve_shape(properties)
        if self.pattern_type == 1:
            # Ascending channel patterns
            if not self.check_profit_channel(False, properties):
                logger.debug(f"Pivot start {self.pivots[0].point.index}, end {self.pivots[-1].point.index} "
                            f"Ascending channel pattern bearish profit check failed")
                self.pattern_type = 0
            elif properties.enable_volume_check and self.check_volume(properties) != -1:
                logger.debug(f"Pivot start {self.pivots[0].point.index}, end {self.pivots[-1].point.index} "
                            f"Ascending channel pattern bearish volume check failed")
                self.pattern_type = 0
        elif self.pattern_type == 2:
            # Descending channel patterns
            if not self.check_profit_channel(True, properties):
                logger.debug(f"Pivot start {self.pivots[0].point.index}, end {self.pivots[-1].point.index} "
                            f"Descending channel pattern bullish profit check failed")
                self.pattern_type = 0
            elif properties.enable_volume_check and self.check_volume(properties) != 1:
                logger.debug(f"Pivot start {self.pivots[0].point.index}, end {self.pivots[-1].point.index} "
                            f"Descending channel pattern bullish volume check failed")
                self.pattern_type = 0
        elif self.pattern_type == 3:
            # Ranging channel patterns
            if self.pivots[0].direction > 0:
                if not self.check_profit_channel(True, properties):
                    logger.debug(f"Pivot start {self.pivots[0].point.index}, end {self.pivots[-1].point.index} "
                                f"Ranging channel pattern bullish profit check failed")
                    self.pattern_type = 0
                elif properties.enable_volume_check and self.check_volume(properties) != 1:
                    logger.debug(f"Pivot start {self.pivots[0].point.index}, end {self.pivots[-1].point.index} "
                                f"Ranging channel pattern bullish volume check failed")
                    self.pattern_type = 0
                else:
                    self.pattern_type = 4 # Ranging Channel (Bullish)
            else:
                if not self.check_profit_channel(False, properties):
                    logger.debug(f"Pivot start {self.pivots[0].point.index}, end {self.pivots[-1].point.index} "
                                f"Ranging channel pattern bearish profit check failed")
                    self.pattern_type = 0
                elif properties.enable_volume_check and self.check_volume(properties) != -1:
                    logger.debug(f"Pivot start {self.pivots[0].point.index}, end {self.pivots[-1].point.index} "
                                f"Ranging channel pattern bearish volume check failed")
                    self.pattern_type = 0
                else:
                    self.pattern_type = 5 # Ranging Channel (Bearish)
        elif self.pattern_type == 9:
            # Rising wedge patterns
            if not self.check_profit_triangle(False, properties):
                logger.debug(f"Pivot start {self.pivots[0].point.index}, end {self.pivots[-1].point.index} "
                            f"Rising wedge pattern bearish profit check failed")
                self.pattern_type = 0
            elif properties.enable_volume_check and self.check_volume(properties) != -1:
                logger.debug(f"Pivot start {self.pivots[0].point.index}, end {self.pivots[-1].point.index} "
                            f"Rising wedge pattern bearish volume check failed")
                self.pattern_type = 0
        elif self.pattern_type == 10:
            # Falling wedge patterns
            if not self.check_profit_triangle(True, properties):
                logger.debug(f"Pivot start {self.pivots[0].point.index}, end {self.pivots[-1].point.index} "
                            f"Falling wedge pattern bullish profit check failed")
                self.pattern_type = 0
            elif properties.enable_volume_check and self.check_volume(properties) != 1:
                logger.debug(f"Pivot start {self.pivots[0].point.index}, end {self.pivots[-1].point.index} "
                            f"Falling wedge pattern bullish volume check failed")
                self.pattern_type = 0
        elif self.pattern_type == 11:
            # Converging triangle patterns
            if self.pivots[0].direction > 0 and \
                self.check_profit_triangle(True, properties):
                if properties.enable_volume_check and self.check_volume(properties) != 1:
                    logger.debug(f"Pivot start {self.pivots[0].point.index}, end {self.pivots[-1].point.index} "
                                f"Converging triangle pattern bullish volume check failed")
                    self.pattern_type = 0
                else:
                    self.pattern_type = 7 # Converging Triangle (Bullish)
            elif self.pivots[0].direction < 0 and \
                self.check_profit_triangle(False, properties):
                if properties.enable_volume_check and self.check_volume(properties) != -1:
                    logger.debug(f"Pivot start {self.pivots[0].point.index}, end {self.pivots[-1].point.index} "
                                f"Converging triangle pattern bearish volume check failed")
                    self.pattern_type = 0
                else:
                    self.pattern_type = 8 # Converging Triangle (Bearish)
            else:
                logger.debug(f"Pivot start {self.pivots[0].point.index}, end {self.pivots[-1].point.index} "
                            f"Converging triangle pattern profit/volume check failed")
                self.pattern_type = 0
        elif self.pattern_type == 12:
            # Descending triangle patterns
            if not self.check_profit_triangle(False, properties):
                logger.debug(f"Pivot start {self.pivots[0].point.index}, end {self.pivots[-1].point.index} "
                            f"Descending triangle pattern bearish profit check failed")
                self.pattern_type = 0
            elif properties.enable_volume_check and self.check_volume(properties) != -1:
                logger.debug(f"Pivot start {self.pivots[0].point.index}, end {self.pivots[-1].point.index} "
                            f"Descending triangle pattern bearish volume check failed")
                self.pattern_type = 0
        elif self.pattern_type == 13:
            # Ascending triangle patterns
            if not self.check_profit_triangle(True, properties):
                logger.debug(f"Pivot start {self.pivots[0].point.index}, end {self.pivots[-1].point.index} "
                            f"Ascending triangle pattern bullish profit check failed")
            elif properties.enable_volume_check and self.check_volume(properties) != 1:
                logger.debug(f"Pivot start {self.pivots[0].point.index}, end {self.pivots[-1].point.index} "
                            f"Ascending triangle pattern bullish volume check failed")
                self.pattern_type = 0
        else:
            # invalidate other patterns
            self.pattern_type = 0
        return self

    def resolve_shape(self, properties: TrendLineProperties) -> 'TrendLinePattern':
        """
        Resolve pattern by updating trend lines, pivot points, and ratios

        Args:
            properties: ScanProperties object containing pattern parameters

        Returns:
            self: Returns the pattern object for method chaining
        """
        # Get first and last indices/times from pivots
        first_index = self.pivots[0].point.index
        last_index = self.pivots[-1].point.index
        first_time = self.pivots[0].point.time
        last_time = self.pivots[-1].point.time

        # Update trend line 1 endpoints
        self.trend_line1.p1 = Point(
            time=first_time,
            index=first_index,
            price=self.trend_line1.get_price(first_index)
        )
        self.trend_line1.p2 = Point(
            time=last_time,
            index=last_index,
            price=self.trend_line1.get_price(last_index)
        )

        # Update trend line 2 endpoints
        self.trend_line2.p1 = Point(
            time=first_time,
            index=first_index,
            price=self.trend_line2.get_price(first_index)
        )
        self.trend_line2.p2 = Point(
            time=last_time,
            index=last_index,
            price=self.trend_line2.get_price(last_index)
        )

        # Update pivot points to match trend lines
        for i, pivot in enumerate(self.pivots):
            current_trend_line = self.trend_line2 if i % 2 == 1 else self.trend_line1

            # Update pivot price to match trend line
            pivot.point.price = current_trend_line.get_price(pivot.point.index)

        # Resolve pattern name
        self.resolve_pattern_name(properties)
        if self.pattern_type == 9 or self.pattern_type == 10 or self.pattern_type == 11 or \
           self.pattern_type == 12 or self.pattern_type == 13:
            interval = (pd.to_datetime(last_time) - pd.to_datetime(first_time)) / (last_index - first_index)
            self.apex = self.get_apex(first_index, first_time, interval, properties.max_apex_periods)
            if self.apex is None:
                logger.warning(f"Pivot start {self.pivots[0].point.index}, end {self.pivots[-1].point.index} "
                            f"Triangle pattern invalid, apex point is None!")
                self.pattern_type = 0
        return self

    def resolve_pattern_name(self, properties: TrendLineProperties) -> 'TrendLinePattern':
        """Determine the pattern type based on trend lines and angles"""
        if self.pivots[0].direction > 0:
            upper_line = self.trend_line1
            lower_line = self.trend_line2
        else:
            upper_line = self.trend_line2
            lower_line = self.trend_line1
        upper1 = upper_line.p1.price
        upper2 = upper_line.p2.price
        lower1 = lower_line.p1.price
        lower2 = lower_line.p2.price
        max_val = max(upper1, upper2)
        min_val = min(lower1, lower2)

        if min_val == max_val or np.sign(upper1 - lower1) != np.sign(upper2 - lower2):
            logger.debug(f"Pivot start {self.pivots[0].point.index}, end {self.pivots[-1].point.index} "
                        f"Trend line pattern invalid, upper line has already crossed lower line!")
            self.pattern_type = 0
            return self

        is_upper_flat = is_within_ratio_threshold(upper1-min_val, upper2-min_val, properties.flat_ratio)
        is_lower_flat = is_within_ratio_threshold(max_val-lower1, max_val-lower2, properties.flat_ratio)

        # Calculate differences and ratios
        start_diff = abs(upper1 - lower1)
        end_diff = abs(upper2 - lower2)
        is_channel = is_within_ratio_threshold(start_diff, end_diff, properties.parallel_ratio)
        is_expanding = not is_channel and end_diff > start_diff
        is_contracting = not is_channel and start_diff > end_diff

        upper_diff = upper2 - upper1
        lower_diff = lower2 - lower1

        if is_channel:
            if is_upper_flat or is_lower_flat:
                self.pattern_type = 3 # Range Channel
            elif abs(upper_diff) >= abs(lower_diff):
                if upper_diff > 0 and self.pivots[0].direction < 0:
                    self.pattern_type = 1  # Ascending Channel
                elif upper_diff < 0 and self.pivots[0].direction > 0:
                    self.pattern_type = 2  # Descending Channel
                else:
                    logger.debug(f"Pivot start {self.pivots[0].point.index}, end {self.pivots[-1].point.index} "
                                f"cannot determine the channel shape with a leading upper line!")
                    self.pattern_type = 0
            else:
                if lower_diff > 0 and self.pivots[0].direction < 0:
                    self.pattern_type = 1  # Ascending Channel
                elif lower_diff < 0 and self.pivots[0].direction > 0:
                    self.pattern_type = 2  # Descending Channel
                else:
                    logger.debug(f"Pivot start {self.pivots[0].point.index}, end {self.pivots[-1].point.index} "
                                f"cannot determine the channel shape with a leading lower line!")
                    self.pattern_type = 0
        elif is_expanding:
            self.pattern_type = 6  # Diverging Triangle
        elif is_contracting:
            if is_upper_flat and self.pivots[0].direction > 0:
                self.pattern_type = 13 # Ascending Triangle (Contracting)
            elif is_lower_flat and self.pivots[0].direction < 0:
                self.pattern_type = 12  # Descending Triangle (Contracting)
            elif upper_diff < 0 and lower_diff > 0:
                self.pattern_type = 11  # Converging Triangle
            elif upper_diff > 0 and self.pivots[0].direction < 0:
                self.pattern_type = 9  # Rising Wedge (Contracting)
            elif upper_diff < 0 and self.pivots[0].direction > 0:
                self.pattern_type = 10  # Falling Wedge (Contracting)
            else:
                logger.debug(f"Pivot start {self.pivots[0].point.index}, end {self.pivots[-1].point.index} "
                            f"cannot determine the contracting shape!")
                self.pattern_type = 0
        else:
            logger.debug(f"Pivot start {self.pivots[0].point.index}, end {self.pivots[-1].point.index} "
                         f"cannot determine the trendline shape.")
            self.pattern_type = 0

        return self

def is_within_ratio_threshold(val1: float, val2: float, ratio_threshold: float) -> bool:
    """Check if the ratio is within the threshold"""
    if val1 == 0 or val2 == 0:
        return False
    fit_ratio = 1 - ratio_threshold
    ratio = abs(val1 / val2)
    if ratio < 1:
        return ratio >= fit_ratio
    else:
        return ratio <= 1 / fit_ratio

def is_aligned(pivots: List[Pivot], ref_pivots: List[Pivot], align_ratio: float,
               flat_ratio: float) -> bool:
    if len(pivots) > 3:
        raise ValueError("Pivots can't be more than 3")
    if len(pivots) < 3:
        return True

    first = pivots[0]
    second = pivots[1]
    third = pivots[2]
    if is_same_height(first, second, ref_pivots, flat_ratio) and \
        is_same_height(second, third, ref_pivots, flat_ratio):
        logger.debug(f"Pivots: {first.point.index}, {second.point.index}, {third.point.index} "
                     f"are aligned as a horizontal line")
        return True

    # check the ratio of the price differences to the bar differences
    if third.cross_diff == 0:
        # the first and third pivots are the same height, but they are not aligned
        # with the second pivot
        return False
    price_ratio = second.cross_diff / third.cross_diff
    bar_ratio = float(second.point.index - first.point.index) / \
        float(third.point.index - second.point.index)
    aligned = is_within_ratio_threshold(price_ratio, bar_ratio, align_ratio)
    logger.debug(f"Pivots: {first.point.index}, {second.point.index}, {third.point.index} "
                 f"price ratio: {price_ratio:.4f}, bar ratio: {bar_ratio:.4f}")
    return aligned

def check_if_line_cross_candle_body(line: Line, direction: float, zigzag: Zigzag,
                                    line_start_index: Optional[int] = None,
                                    line_end_index: Optional[int] = None) -> int:
    """
    Check if a line crosses the candle body
    """
    if line_start_index is not None and line_start_index < line.p1.index:
        start_index = line_start_index
    else:
        start_index = line.p1.index

    if line_end_index is not None and line_end_index > line.p2.index:
        end_index = line_end_index
    else:
        end_index = line.p2.index

    crosses = 0
    for i in range(start_index + 1, end_index):
        bar_data = zigzag.get_df_data_by_index(i)
        if direction > 0 and line.get_price(i) < max(bar_data['open'], bar_data['close']):
            crosses += 1
        elif direction < 0 and line.get_price(i) > min(bar_data['open'], bar_data['close']):
            crosses += 1
    return crosses

def inspect_line_by_point(line: Line, point_bar: int, direction: float,
                          zigzag: Zigzag) -> Tuple[bool, float]:
    """
    Inspect a single line against price data from a pandas DataFrame

    Args:
        line: Line object to inspect
        point_bar: Index of the point to inspect
        direction: Direction of the trend (1 for up, -1 for down)
        zigzag: Zigzag calculator instance

    Returns:
        Tuple of (valid: bool, diff: float)
    """
    # Get price data from DataFrame
    bar_data = zigzag.get_df_data_by_index(point_bar)

    # Determine prices based on direction
    line_price = line.get_price(point_bar)
    line_price_diff = abs(line.p1.price - line.p2.price)
    if direction > 0:
        # upper line
        body_high_price = max(bar_data['open'], bar_data['close'])
        if line_price < body_high_price:
            # invalid if line is crossing the candle body
            return False, float('inf') # make the difference as large as possible
        elif line_price > bar_data['high']:
            # line is above the candle wick
            diff = line_price - bar_data['high']
            return diff < line_price_diff, diff
        else:
            # line is crossing the candle wick
            return True, 0
    else:
        # lower line
        body_low_price = min(bar_data['open'], bar_data['close'])
        if line_price > body_low_price:
            # invalid if line is crossing the candle body
            return False, float('inf') # make the difference as large as possible
        elif line_price < bar_data['low']:
            # line is below the candle wick
            diff = bar_data['low'] - line_price
            return diff < line_price_diff, diff
        else:
            # line is crossing the candle wick
            return True, 0

def inspect_pivots(pivots: List[Pivot], direction: float, properties: TrendLineProperties,
                   first_pivot: Pivot, last_pivot: Pivot, zigzag: Zigzag) -> Tuple[bool, Line]:
    """
    Inspect multiple pivots to find the best trend line using DataFrame price data

    Args:
        pivots: List of pivots to create trend lines
        direction: Direction of the trend
        properties: TrendLineProperties object containing pattern parameters
        first_pivot: The first pivot to inspect
        last_pivot: The last pivot to inspect
        zigzag: Zigzag calculator instance

    Returns:
        Tuple of (valid: bool, best_trend_line: Line)
    """
    if len(pivots) == 3:
        # Create three possible trend lines
        trend_line1 = Line(pivots[0].point, pivots[2].point)  # First to last
        # check if the line consisting of the first and last points crosses the candle body
        if check_if_line_cross_candle_body(trend_line1, direction, zigzag) > \
            properties.max_candle_body_crosses:
            return False, None
        # inspect line by middle point
        valid1, diff1 = inspect_line_by_point(trend_line1, pivots[1].point.index,
                                              direction, zigzag)
        if valid1 and diff1 == 0:
            # prefer the line connecting the first and last points
            return True, trend_line1

        trend_line2 = Line(pivots[0].point, pivots[1].point)  # First to middle
        valid2, diff2 = inspect_line_by_point(trend_line2, pivots[2].point.index,
                                              direction, zigzag)

        trend_line3 = Line(pivots[1].point, pivots[2].point)  # Middle to last
        valid3, diff3 = inspect_line_by_point(trend_line3, pivots[0].point.index,
                                              direction, zigzag)

        if not valid1 and not valid2 and not valid3:
            return False, None

        # Find the best line
        if valid1:
            trendline = trend_line1
        elif valid2 and diff2 < diff1:
            trendline = trend_line2
        elif valid3 and diff3 < min(diff1, diff2):
            trendline = trend_line3
        else:
            return False, None

        return True, trendline
    else:
        # For 2 points, simply create one trend line
        trend_line = Line(pivots[0].point, pivots[1].point)
        valid = check_if_line_cross_candle_body(
            trend_line, direction, zigzag,
            first_pivot.point.index, last_pivot.point.index) <= \
            properties.max_candle_body_crosses
        return valid, trend_line

def find_trend_lines(zigzag: Zigzag, offset: int, properties: TrendLineProperties,
                patterns: List[TrendLinePattern]) -> bool:
    """
    Find patterns using DataFrame price data

    Args:
        zigzag: ZigZag calculator instance
        offset: Offset to start searching for pivots
        properties: Scan properties
        patterns: List to store found patterns

    Returns:
        int: Index of the pivot that was used to find the pattern
    """
    # Get pivots
    if properties.number_of_pivots < 4 or properties.number_of_pivots > 6:
        raise ValueError("Number of pivots must be between 4 and 6")

    pivots = []
    min_pivots = get_pivots_from_zigzag(zigzag, pivots, offset, properties.number_of_pivots)
    if min_pivots != properties.number_of_pivots:
        return False

    # Validate pattern
    # Create point arrays for trend lines
    trend_pivots1 = ([pivots[0], pivots[2], pivots[4]]
                      if properties.number_of_pivots == 5
                      else [pivots[0], pivots[2]])
    trend_pivots2 = ([pivots[1], pivots[3], pivots[5]]
                      if properties.number_of_pivots == 6
                      else [pivots[1], pivots[3]])

    if not is_aligned(trend_pivots1, pivots, properties.align_ratio,
                      properties.flat_ratio) or \
        not is_aligned(trend_pivots2, pivots, properties.align_ratio,
                       properties.flat_ratio):
        return False

    # Validate trend lines using DataFrame
    valid1, trend_line1 = inspect_pivots(trend_pivots1,
                                        np.sign(trend_pivots1[0].direction),
                                        properties, pivots[0], pivots[-1], zigzag)
    valid2, trend_line2 = inspect_pivots(trend_pivots2,
                                        np.sign(trend_pivots2[0].direction),
                                        properties, pivots[0], pivots[-1], zigzag)

    if valid1 and valid2:
        index_delta = pivots[-1].point.index - pivots[0].point.index + 1
        if index_delta < properties.min_periods_lapsed:
            # only consider patterns with enough time lapsed
            return False
        # Create pattern
        pattern = TrendLinePattern(
            pivots=pivots,
            trend_line1=trend_line1,
            trend_line2=trend_line2,
        ).resolve(properties)

        # Process pattern (resolve type, check if allowed, etc.)
        return pattern.process_pattern(properties, patterns)
    else:
        logger.debug(f"Invalid pattern: start {pivots[0].point.index}, end {pivots[-1].point.index}")
        return False
