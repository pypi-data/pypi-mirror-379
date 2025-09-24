import numba
import numpy as np
from numba import prange


@numba.njit
def _sift_up(heap_times, heap_coords, idx):
    while idx > 0:
        parent = (idx - 1) // 2
        if heap_times[idx] < heap_times[parent]:
            # Swap times
            tmp_time = heap_times[idx]
            heap_times[idx] = heap_times[parent]
            heap_times[parent] = tmp_time
            # Swap coords
            tmp_coord0 = heap_coords[idx, 0]
            tmp_coord1 = heap_coords[idx, 1]
            heap_coords[idx, 0] = heap_coords[parent, 0]
            heap_coords[idx, 1] = heap_coords[parent, 1]
            heap_coords[parent, 0] = tmp_coord0
            heap_coords[parent, 1] = tmp_coord1
            idx = parent
        else:
            break


@numba.njit
def _sift_down(heap_times, heap_coords, heap_size, idx):
    while 2 * idx + 1 < heap_size:
        left = 2 * idx + 1
        right = left + 1
        smallest = idx
        if heap_times[left] < heap_times[smallest]:
            smallest = left
        if right < heap_size and heap_times[right] < heap_times[smallest]:
            smallest = right
        if smallest != idx:
            # Swap times
            tmp_time = heap_times[idx]
            heap_times[idx] = heap_times[smallest]
            heap_times[smallest] = tmp_time
            # Swap coords
            tmp_coord0 = heap_coords[idx, 0]
            tmp_coord1 = heap_coords[idx, 1]
            heap_coords[idx, 0] = heap_coords[smallest, 0]
            heap_coords[idx, 1] = heap_coords[smallest, 1]
            heap_coords[smallest, 0] = tmp_coord0
            heap_coords[smallest, 1] = tmp_coord1
            idx = smallest
        else:
            break


@numba.njit(parallel=True)
def _mask_burn_times(burn_times, burn_time_minutes):
    nrows, ncols = burn_times.shape
    for i in prange(nrows):
        for j in range(ncols):
            if burn_times[i, j] > burn_time_minutes:
                burn_times[i, j] = np.inf


@numba.njit
def mtt_minimum_travel_time(
    burn_times,
    fuel_models,
    moisture_1hr,
    moisture_10hr,
    moisture_100hr,
    moisture_herb,
    moisture_woody,
    wind_speed,
    wind_direction,
    slope,
    aspect,
    spatial_resolution,
    burn_time_minutes,
):
    """
    Numba-accelerated Minimum Travel Time (MTT) fire spread algorithm.
    Arguments:
        burn_times: 2D array of burn times (np.inf for unburned)
        fuel_models: 2D array of fuel model codes
        moisture_1hr, moisture_10hr, moisture_100hr, moisture_herb, moisture_woody: 2D arrays
        wind_speed, wind_direction: 2D arrays
        slope, aspect: 2D arrays
        spatial_resolution: cell size (meters)
        burn_time_minutes: max simulation time (minutes)
    Returns:
        Updated burn_times array (in-place)
    Note: All arrays must be contiguous and correct dtype before calling this function.
    """
    # If needed, ensure arrays are contiguous (no dtype argument in Numba)
    burn_times = np.ascontiguousarray(burn_times)
    fuel_models = np.ascontiguousarray(fuel_models)
    moisture_1hr = np.ascontiguousarray(moisture_1hr)
    moisture_10hr = np.ascontiguousarray(moisture_10hr)
    moisture_100hr = np.ascontiguousarray(moisture_100hr)
    moisture_herb = np.ascontiguousarray(moisture_herb)
    moisture_woody = np.ascontiguousarray(moisture_woody)
    wind_speed = np.ascontiguousarray(wind_speed)
    wind_direction = np.ascontiguousarray(wind_direction)
    slope = np.ascontiguousarray(slope)
    aspect = np.ascontiguousarray(aspect)

    nrows, ncols = burn_times.shape
    processed = np.zeros((nrows, ncols), dtype=np.int8)
    dr = np.array([-1, -1, 0, 1, 1, 1, 0, -1])
    dc = np.array([0, 1, 1, 1, 0, -1, -1, -1])
    np.array([0, 45, 90, 135, 180, 225, 270, 315])
    max_heap = nrows * ncols
    heap_times = np.empty(max_heap, dtype=np.float32)
    heap_coords = np.empty((max_heap, 2), dtype=np.int32)
    heap_size = 0
    # Initialize heap with ignition points
    for i in range(nrows):
        for j in range(ncols):
            if burn_times[i, j] == 0.0:
                heap_times[heap_size] = 0.0
                heap_coords[heap_size, 0] = i
                heap_coords[heap_size, 1] = j
                _sift_up(heap_times, heap_coords, heap_size)
                heap_size += 1
    while heap_size > 0:
        # Pop min
        time_val = heap_times[0]
        i = heap_coords[0, 0]
        j = heap_coords[0, 1]
        heap_size -= 1
        if heap_size > 0:
            heap_times[0] = heap_times[heap_size]
            heap_coords[0, 0] = heap_coords[heap_size, 0]
            heap_coords[0, 1] = heap_coords[heap_size, 1]
            _sift_down(heap_times, heap_coords, heap_size, 0)
        if processed[i, j]:
            continue
        processed[i, j] = 1
        # Nonburnable check
        if fuel_models[i, j] in (91, 92, 93, 98, 99):
            continue
        fuel_model = fuel_models[i, j]
        m1 = moisture_1hr[i, j]
        m10 = moisture_10hr[i, j]
        m100 = moisture_100hr[i, j]
        mh = moisture_herb[i, j]
        mw = moisture_woody[i, j]
        ws = wind_speed[i, j]
        wd = wind_direction[i, j]
        sl = slope[i, j]
        asp = aspect[i, j]
        for k in range(8):
            nr = i + dr[k]
            nc = j + dc[k]
            if nr < 0 or nr >= nrows or nc < 0 or nc >= ncols:
                continue
            if processed[nr, nc] or fuel_models[nr, nc] in (
                91,
                92,
                93,
                98,
                99,
            ):
                continue
            # Calculate realistic base rate from fuel model (m/min)
            # Adjusted for reasonable spread rates (target: 30-120 m/hr = 0.5-2.0 m/min)
            base_rate = 0.3  # Default for unknown fuels
            if fuel_model == 1:
                base_rate = 1.0  # GR1 - Short grass
            elif fuel_model == 2:
                base_rate = 1.2  # GR2 - Low load grass
            elif fuel_model == 3:
                base_rate = 1.5  # GR3 - Low load grass
            elif fuel_model == 4:
                base_rate = 2.0  # GR4 - Moderate load grass
            elif fuel_model == 5:
                base_rate = 0.8  # GS1 - Low load shrub
            elif fuel_model == 6:
                base_rate = 1.0  # GS2 - Moderate load shrub
            elif fuel_model == 7:
                base_rate = 1.2  # GS3 - Moderate load shrub
            elif fuel_model == 8:
                base_rate = 0.6  # SH1 - Low load shrub
            elif fuel_model == 9:
                base_rate = 0.8  # SH2 - Moderate load shrub
            elif fuel_model == 10:
                base_rate = 1.0  # SH3 - High load shrub
            elif fuel_model == 11:
                base_rate = 0.7  # TU1 - Light load timber
            elif fuel_model == 12:
                base_rate = 0.9  # TU2 - Moderate load timber
            elif fuel_model == 13:
                base_rate = 1.1  # TU3 - Moderate load timber

            # Calculate realistic moisture effect using Rothermel model approach
            # Dead fuel moisture effect (1hr, 10hr, 100hr are most critical)
            avg_dead_moisture = (m1 + m10 + m100) / 3.0
            moisture_extinction = 15.0  # Typical extinction moisture for grass fuels

            # Moderate moisture effect - fire stops when moisture > extinction
            if avg_dead_moisture >= moisture_extinction:
                moisture_effect = 0.0  # No fire spread
            else:
                # Exponential decay as moisture approaches extinction
                moisture_ratio = avg_dead_moisture / moisture_extinction
                moisture_effect = np.exp(-1.5 * moisture_ratio)  # Reduced from -3.0 to -1.5

            # Live fuel moisture has additional dampening effect
            avg_live_moisture = (mh + mw) / 2.0
            if avg_live_moisture > 100.0:  # Live fuels very wet
                live_dampening = np.exp(-(avg_live_moisture - 100.0) / 50.0)
                moisture_effect *= live_dampening

            # Calculate elliptical parameters
            a, b, c = _calculate_elliptical_parameters(base_rate * moisture_effect, ws, wd, sl, asp)

            # Calculate travel time using elliptical model
            dx = (nc - j) * spatial_resolution
            dy = (nr - i) * spatial_resolution
            travel_time = _calculate_travel_time(a, b, c, dx, dy, wd)

            if travel_time == np.inf:
                continue

            new_time = time_val + travel_time
            if new_time > burn_time_minutes:
                continue
            if new_time < burn_times[nr, nc]:
                burn_times[nr, nc] = new_time
                # Push to heap
                heap_times[heap_size] = new_time
                heap_coords[heap_size, 0] = nr
                heap_coords[heap_size, 1] = nc
                _sift_up(heap_times, heap_coords, heap_size)
                heap_size += 1
    _mask_burn_times(burn_times, burn_time_minutes)
    return burn_times


@numba.njit
def _calculate_base_spread_rate(
    fuel_model,
    fuel_loading_1hr,
    fuel_loading_10hr,
    fuel_loading_100hr,
    fuel_sav_1hr,
    fuel_depth,
    fuel_moisture_extinction,
):
    """
    Calculate base spread rate from fuel model using simplified Rothermel equations.

    Args:
        fuel_model: Fuel model code
        fuel_loading_1hr: 1-hour fuel loading array
        fuel_loading_10hr: 10-hour fuel loading array
        fuel_loading_100hr: 100-hour fuel loading array
        fuel_sav_1hr: Surface area to volume ratio array
        fuel_depth: Fuel bed depth array

    Returns:
        Base spread rate in m/min
    """
    # Get fuel properties from the arrays
    loading_1hr = fuel_loading_1hr[fuel_model] if fuel_model < len(fuel_loading_1hr) else 0.0
    loading_10hr = fuel_loading_10hr[fuel_model] if fuel_model < len(fuel_loading_10hr) else 0.0
    loading_100hr = fuel_loading_100hr[fuel_model] if fuel_model < len(fuel_loading_100hr) else 0.0
    sav_1hr = fuel_sav_1hr[fuel_model] if fuel_model < len(fuel_sav_1hr) else 2000.0
    depth = fuel_depth[fuel_model] if fuel_model < len(fuel_depth) else 1.0

    # Simplified Rothermel calculation
    # Reaction intensity (simplified)
    total_loading = loading_1hr + loading_10hr + loading_100hr
    if total_loading <= 0:
        return 0.1  # Minimum base rate for any fuel

    # Surface area to volume ratio effect (normalized)
    sav_factor = min(sav_1hr / 2000.0, 3.0)  # Allow up to 3x effect

    # Fuel bed depth effect (normalized)
    depth_factor = min(depth / 1.0, 2.0)  # Normalize to 1.0 instead of 2.0

    # More realistic base rate calculation
    # Use primarily 1-hour fuels but include some contribution from other classes
    effective_loading = loading_1hr + (loading_10hr * 0.5) + (loading_100hr * 0.1)

    # Base rate calculation - much more realistic scaling
    base_rate = (
        effective_loading * sav_factor * depth_factor
    ) * 10.0  # Increased multiplier significantly

    # Realistic bounds for fire spread rates
    # Typical fire spread: 5-30 m/min (300-1800 m/hr) in moderate conditions
    base_rate = max(0.5, min(base_rate, 5.0))  # Between 0.5 and 5.0 m/min (30-300 m/hr)

    return base_rate


@numba.njit
def _calculate_elliptical_parameters(base_rate, wind_speed, wind_direction, slope, aspect):
    """
    Calculate elliptical fire spread parameters (a, b, c) based on environmental conditions.

    Args:
        base_rate: Base spread rate (m/min)
        wind_speed: Wind speed (km/h)
        wind_direction: Wind direction (degrees)
        slope: Slope (degrees)
        aspect: Aspect (degrees)

    Returns:
        Tuple of (a, b, c) where:
        a: Flanking spread rate
        b: Forward spread rate
        c: Offset from center to ignition point
    """
    # Convert wind speed from km/h to mph for Rothermel model
    wind_speed_mph = wind_speed / 1.609  # km/h to mph

    # Moderate wind effect - realistic but not extreme
    # Reduced from previous version to prevent absurd spread rates
    if wind_speed_mph > 0.1:
        phi_w = np.power(wind_speed_mph / 15.0, 1.2)  # Reduced exponent and denominator
        wind_effect = 1.0 + phi_w
        wind_effect = min(wind_effect, 5.0)  # Much lower cap
    else:
        wind_effect = 1.0

    # Moderate slope effect - reduced to prevent extreme spread rates
    slope_rad = np.deg2rad(abs(slope))
    tan_slope = np.tan(slope_rad)
    # Reduced coefficient for more reasonable slope effect
    phi_s = 8.0 * tan_slope * tan_slope  # Reduced from 30.0
    slope_effect = 1.0 + phi_s
    slope_effect = min(slope_effect, 8.0)  # Much lower cap

    # Realistic aspect effect - wind-slope interaction
    # Calculate angle between wind direction and upslope direction (aspect)
    aspect_diff = abs((aspect - wind_direction + 360) % 360)
    if aspect_diff > 180:
        aspect_diff = 360 - aspect_diff

    # Strong aspect effect based on wind-slope alignment
    # When wind and slope align (aspect_diff = 0): maximum effect (3x)
    # When perpendicular (aspect_diff = 90): moderate effect (1x)
    # When opposing (aspect_diff = 180): minimum effect (0.1x)
    alignment = np.cos(np.deg2rad(aspect_diff))  # 1.0 when aligned, -1.0 when opposing
    # Map from [-1,1] to [0.1,3.0] with 1.0 at perpendicular
    # Use a more extreme mapping: 1.0 + alignment * 0.9 gives range [0.1, 1.9] with 1.0 at 90°
    aspect_effect = 1.0 + alignment * 0.9  # Range: [0.1, 1.9] with 1.0 at 90°
    aspect_effect = max(0.1, min(3.0, aspect_effect))

    # Calculate fire spread rates: head (downwind), flank (perpendicular), back (upwind)
    head_rate = base_rate * wind_effect * slope_effect * aspect_effect  # Head (fastest)
    flank_rate = base_rate * slope_effect * aspect_effect  # Flanks (no wind effect)
    back_rate = (
        base_rate * slope_effect * aspect_effect * 0.2
    )  # Back (much slower, 20% of no-wind rate)

    # Assign to a, b, c for compatibility
    a = flank_rate  # Flanking spread rate (perpendicular to wind)
    b = head_rate  # Head spread rate (downwind, fastest)
    c = back_rate  # Back spread rate (upwind, slowest)

    # Conservative bounds to prevent absurd spread rates
    b = min(b, 4.0)  # Cap head spread at 4 m/min (240 m/hr)
    a = min(a, 2.0)  # Cap flank spread at 2 m/min (120 m/hr)
    c = min(c, 0.8)  # Cap back spread at 0.8 m/min (48 m/hr)

    return a, b, c


@numba.njit
def _calculate_spread_rate(a, b, c, theta):
    """
    Calculate fire spread rate at angle theta using standard elliptical fire spread model.

    Args:
        a: Semi-minor axis (flanking spread rate)
        b: Semi-major axis (forward spread rate)
        c: Offset from center (not used in standard ellipse equation)
        theta: Angle from major axis (-π < θ < π)

    Returns:
        Spread rate at angle theta
    """
    # Standard ellipse equation: r = ab / sqrt((a*sin(θ))² + (b*cos(θ))²)
    # This gives the radius (spread rate) at angle theta from the major axis
    cos_theta = np.cos(theta)
    sin_theta = np.sin(theta)
    denominator = np.sqrt((a * sin_theta) * (a * sin_theta) + (b * cos_theta) * (b * cos_theta))

    # Avoid division by zero
    if denominator < 1e-10:
        return 0.0

    return (a * b) / denominator


@numba.njit
def _calculate_travel_time(a, b, c, dx, dy, wind_direction):
    """
    Calculate travel time using asymmetric fire ellipse with head/back distinction.

    Args:
        a: Flanking spread rate (perpendicular to wind)
        b: Head spread rate (downwind, fastest)
        c: Back spread rate (upwind, slowest)
        dx: X component of distance (positive = east)
        dy: Y component of distance (positive = north)
        wind_direction: Wind direction in degrees (direction wind is blowing TO)

    Returns:
        Travel time in minutes
    """
    # Calculate distance
    distance = np.sqrt(dx * dx + dy * dy)
    if distance < 1e-10:
        return 0.0

    # Calculate angle from positive x-axis (east = 0°, north = 90°)
    theta = np.arctan2(dy, dx)

    # Convert wind direction to radians
    wind_rad = np.deg2rad(wind_direction)

    # Calculate angle relative to wind direction
    # Wind direction is where wind is blowing TO, so head is in that direction
    # If wind is toward 90° (east) and we're going east (θ=0°), relative should be 0°
    relative_theta = theta - wind_rad

    # Normalize angle to [-π, π]
    while relative_theta > np.pi:
        relative_theta -= 2 * np.pi
    while relative_theta < -np.pi:
        relative_theta += 2 * np.pi

    # Calculate spread rate based on direction relative to wind
    np.cos(relative_theta)
    np.sin(relative_theta)

    # Determine if we're in the head (downwind) or back (upwind) sector
    # For wind blowing TO wind_direction:
    # Head: direction aligned with wind (relative_theta ≈ 0)
    # Back: direction opposite to wind (relative_theta ≈ ±π)

    if abs(relative_theta) < np.pi / 2:
        # Forward hemisphere - interpolate between head and flank rates
        # At 0°: pure head (b), at ±90°: pure flank (a)

        # Calculate how "forward" we are: 1 at 0° (pure head), 0 at ±90° (pure flank)
        head_factor = 1.0 - (abs(relative_theta) / (np.pi / 2))
        head_factor = min(1.0, max(0.0, head_factor))  # Clamp to [0,1]

        # Interpolate between head rate and flanking rate
        effective_rate = b * head_factor + a * (1.0 - head_factor)
        spread_rate = effective_rate
    else:
        # Backward hemisphere - use asymmetric back fire model
        # For angles in back hemisphere, interpolate between flanking (a) and back (c) rates

        # Calculate how "backwards" we are: 0 at ±90° (pure flank), 1 at 180° (pure back)
        back_factor = abs(abs(relative_theta) - np.pi / 2) / (np.pi / 2)
        back_factor = min(1.0, max(0.0, back_factor))  # Clamp to [0,1]

        # Interpolate between flanking rate and back rate
        effective_rate = a * (1.0 - back_factor) + c * back_factor
        spread_rate = effective_rate

    # Ensure minimum spread rate
    spread_rate = max(spread_rate, 0.01)

    # Return travel time
    return distance / spread_rate


@numba.njit
def _dijkstra_cell_based(
    burn_times,
    fuel_models,
    moisture_1hr,
    moisture_10hr,
    moisture_100hr,
    moisture_herb,
    moisture_woody,
    wind_speed,
    wind_direction,
    slope,
    aspect,
    spatial_resolution,
    burn_time_minutes,
    fuel_loading_1hr,
    fuel_loading_10hr,
    fuel_loading_100hr,
    fuel_sav_1hr,
    fuel_depth,
    fuel_moisture_extinction,
):
    """
    Sequential Dijkstra's algorithm for cell-based MTT fire spread.
    """
    nrows, ncols = burn_times.shape
    processed = np.zeros((nrows, ncols), dtype=np.int8)

    # Use heap for proper Dijkstra's algorithm
    max_heap = nrows * ncols
    heap_times = np.empty(max_heap, dtype=np.float32)
    heap_coords = np.empty((max_heap, 2), dtype=np.int32)
    heap_size = 0

    # Initialize heap with ignition points
    for i in range(nrows):
        for j in range(ncols):
            if burn_times[i, j] == 0.0:
                heap_times[heap_size] = 0.0
                heap_coords[heap_size, 0] = i
                heap_coords[heap_size, 1] = j
                _sift_up(heap_times, heap_coords, heap_size)
                heap_size += 1

    # Standard 8-neighbor connectivity with proper distance weighting
    dr = np.array([-1, -1, -1, 0, 0, 1, 1, 1])
    dc = np.array([-1, 0, 1, -1, 1, -1, 0, 1])
    # Distance weights: diagonal neighbors are sqrt(2) times farther
    np.array([1.414, 1.0, 1.414, 1.0, 1.0, 1.414, 1.0, 1.414])

    while heap_size > 0:
        # Pop minimum time cell
        time_val = heap_times[0]
        i = heap_coords[0, 0]
        j = heap_coords[0, 1]

        # Remove from heap
        heap_size -= 1
        if heap_size > 0:
            heap_times[0] = heap_times[heap_size]
            heap_coords[0, 0] = heap_coords[heap_size, 0]
            heap_coords[0, 1] = heap_coords[heap_size, 1]
            _sift_down(heap_times, heap_coords, heap_size, 0)

        if processed[i, j]:
            continue
        processed[i, j] = 1

        # Skip non-burnable cells
        if fuel_models[i, j] in (91, 92, 93, 98, 99):
            continue

        # Get environmental conditions for current cell
        fuel_model = fuel_models[i, j]
        m1 = moisture_1hr[i, j]
        m10 = moisture_10hr[i, j]
        m100 = moisture_100hr[i, j]
        mh = moisture_herb[i, j]
        mw = moisture_woody[i, j]
        ws = wind_speed[i, j]
        wd = wind_direction[i, j]
        sl = slope[i, j]
        asp = aspect[i, j]

        # Check moisture extinction thresholds based on fuel model
        moisture_extinction = (
            fuel_moisture_extinction[fuel_model]
            if fuel_model < len(fuel_moisture_extinction)
            else 15.0
        )

        # Check if any moisture class exceeds extinction threshold
        # Dead fuels (1hr, 10hr, 100hr) are most critical for fire spread
        if m1 > moisture_extinction or m10 > moisture_extinction or m100 > moisture_extinction:
            continue  # Skip this cell - fire cannot spread here

        # Calculate base spread rate
        base_rate = _calculate_base_spread_rate(
            fuel_model,
            fuel_loading_1hr,
            fuel_loading_10hr,
            fuel_loading_100hr,
            fuel_sav_1hr,
            fuel_depth,
            fuel_moisture_extinction,
        )

        # Calculate elliptical parameters
        a, b, c = _calculate_elliptical_parameters(base_rate, ws, wd, sl, asp)

        # Additional check for live fuels - they have much higher extinction thresholds
        # Live fuels typically have 100-300% moisture content and don't prevent fire spread
        # unless extremely wet (>200% for herbs, >300% for woody)
        live_extinction_herb = 200.0  # 200% moisture extinction for herbaceous fuels
        live_extinction_woody = 300.0  # 300% moisture extinction for woody fuels
        if mh > live_extinction_herb or mw > live_extinction_woody:
            continue  # Skip this cell - live fuels too wet

        # Process all 8 neighbors
        for k in range(8):
            nr = i + dr[k]
            nc = j + dc[k]

            if nr < 0 or nr >= nrows or nc < 0 or nc >= ncols:
                continue
            if processed[nr, nc] or fuel_models[nr, nc] in (
                91,
                92,
                93,
                98,
                99,
            ):
                continue

            # Check if neighbor cell can burn (moisture extinction check)
            neighbor_fuel_model = fuel_models[nr, nc]
            neighbor_moisture_extinction = (
                fuel_moisture_extinction[neighbor_fuel_model]
                if neighbor_fuel_model < len(fuel_moisture_extinction)
                else 15.0
            )
            neighbor_m1 = moisture_1hr[nr, nc]
            neighbor_m10 = moisture_10hr[nr, nc]
            neighbor_m100 = moisture_100hr[nr, nc]
            neighbor_mh = moisture_herb[nr, nc]
            neighbor_mw = moisture_woody[nr, nc]

            # Skip neighbor if too wet to burn
            if (
                neighbor_m1 > neighbor_moisture_extinction
                or neighbor_m10 > neighbor_moisture_extinction
                or neighbor_m100 > neighbor_moisture_extinction
            ):
                continue

            neighbor_live_extinction_herb = 200.0  # 200% moisture extinction for herbaceous fuels
            neighbor_live_extinction_woody = 300.0  # 300% moisture extinction for woody fuels
            if (
                neighbor_mh > neighbor_live_extinction_herb
                or neighbor_mw > neighbor_live_extinction_woody
            ):
                continue

            # Calculate travel time with proper distance weighting
            dx = dc[k] * spatial_resolution
            dy = dr[k] * spatial_resolution
            travel_time = _calculate_travel_time(a, b, c, dx, dy, wd)

            if travel_time == np.inf:
                continue

            new_time = time_val + travel_time
            if new_time > burn_time_minutes:
                continue

            # Update if shorter path found
            if new_time < burn_times[nr, nc]:
                burn_times[nr, nc] = new_time
                # Add to heap
                heap_times[heap_size] = new_time
                heap_coords[heap_size, 0] = nr
                heap_coords[heap_size, 1] = nc
                _sift_up(heap_times, heap_coords, heap_size)
                heap_size += 1


@numba.njit
def mtt_minimum_travel_time_improved(
    burn_times,
    fuel_models,
    moisture_1hr,
    moisture_10hr,
    moisture_100hr,
    moisture_herb,
    moisture_woody,
    wind_speed,
    wind_direction,
    slope,
    aspect,
    spatial_resolution,
    burn_time_minutes,
    fuel_loading_1hr,
    fuel_loading_10hr,
    fuel_loading_100hr,
    fuel_sav_1hr,
    fuel_depth,
    fuel_moisture_extinction,
):
    """
    Improved Minimum Travel Time (MTT) fire spread algorithm using sequential Dijkstra's algorithm.
    """
    # Run sequential Dijkstra's algorithm (using existing function)
    _dijkstra_cell_based(
        burn_times,
        fuel_models,
        moisture_1hr,
        moisture_10hr,
        moisture_100hr,
        moisture_herb,
        moisture_woody,
        wind_speed,
        wind_direction,
        slope,
        aspect,
        spatial_resolution,
        burn_time_minutes,
        fuel_loading_1hr,
        fuel_loading_10hr,
        fuel_loading_100hr,
        fuel_sav_1hr,
        fuel_depth,
        fuel_moisture_extinction,
    )

    # Mask burn times
    _mask_burn_times(burn_times, burn_time_minutes)

    return burn_times
