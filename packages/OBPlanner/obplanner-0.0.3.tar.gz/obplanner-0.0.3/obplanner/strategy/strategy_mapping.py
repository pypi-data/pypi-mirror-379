from obplanner.strategy.sort_strategies import spot_sorting, line_sorting, contour_sorting

sort_function_map = {
    'SpotRandom': spot_sorting.SpotRandom,
    'LineSort': line_sorting.LineSort,
    'LineSnake': line_sorting.LineSnake,
    'SpotOrdered': spot_sorting.SpotOrdered,
    'LineConcentric' : line_sorting.LineConcentric,
    'ContourLine': contour_sorting.ContourLine
}
