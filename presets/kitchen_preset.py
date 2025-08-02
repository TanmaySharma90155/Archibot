import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Arc, Circle
from matplotlib.lines import Line2D

# --- Constants for dimensions and appearance ---
WALL_THICKNESS = 0.15 # meters
DOOR_WIDTH = 0.8
WINDOW_WIDTH = 1.2
COUNTER_DEPTH = 0.6 # Standard kitchen counter depth (from wall)
OVERHEAD_CABINET_DEPTH = 0.35 # Depth of overhead cabinets

# Colors
WALL_COLOR = '#b0b0b0' # Gray
FLOOR_COLOR = 'white'
COUNTER_COLOR = '#8B4513' # SaddleBrown (wood)
COUNTERTOP_COLOR = '#a9a9a9' # DarkGray (granite/stone look)
APPLIANCE_COLOR = '#696969' # Dim Gray (stainless steel look)
SINK_COLOR = 'lightgray'
CABINET_COLOR = '#a0522d' # Sienna (overhead cabinet wood)
DOOR_COLOR = 'white'
WINDOW_COLOR = '#add8e6'

# --- Helper Functions (Revised and New) ---

def draw_door(ax, x, y, door_leaf_length, wall_thickness, orientation='h', swing_direction='in_cw'):
    """
    Draws a door opening with swing.
    x,y: bottom-left of the door opening (not hinge).
    door_leaf_length: the length of the door leaf.
    wall_thickness: the thickness of the wall the door is in.
    orientation: 'h' for horizontal wall, 'v' for vertical wall.
    swing_direction: 'in_cw' (inwards, clockwise), 'in_ccw' (inwards, counter-clockwise),
                     'out_cw' (outwards, clockwise), 'out_ccw' (outwards, counter-clockwise)
    """
    # Cut out the door opening (white rectangle)
    if orientation == 'h':
        ax.add_patch(Rectangle((x, y), door_leaf_length, wall_thickness, facecolor=FLOOR_COLOR, edgecolor=FLOOR_COLOR, linewidth=0, zorder=2))
    else: # 'v'
        ax.add_patch(Rectangle((x, y), wall_thickness, door_leaf_length, facecolor=FLOOR_COLOR, edgecolor=FLOOR_COLOR, linewidth=0, zorder=2))

    # Draw door leaf and arc
    door_leaf_color = 'black'
    door_leaf_linewidth = 1.5
    arc_linewidth = 0.8
    arc_linestyle = ':'

    if orientation == 'h': # Door in a horizontal wall (wall along x-axis)
        if swing_direction == 'in_cw':
            hinge_x, hinge_y = x, y + wall_thickness # Hinge is on left, inner side of wall
            ax.add_line(Line2D([hinge_x, hinge_x], [hinge_y, hinge_y + door_leaf_length], color=door_leaf_color, linewidth=door_leaf_linewidth, zorder=3))
            ax.add_patch(Arc((hinge_x, hinge_y), 2*door_leaf_length, 2*door_leaf_length, angle=0, theta1=0, theta2=90, color=door_leaf_color, linestyle=arc_linestyle, linewidth=arc_linewidth, zorder=3))
        elif swing_direction == 'in_ccw':
            hinge_x, hinge_y = x + door_leaf_length, y + wall_thickness # Hinge is on right, inner side of wall
            ax.add_line(Line2D([hinge_x, hinge_x], [hinge_y, hinge_y + door_leaf_length], color=door_leaf_color, linewidth=door_leaf_linewidth, zorder=3))
            ax.add_patch(Arc((hinge_x, hinge_y), 2*door_leaf_length, 2*door_leaf_length, angle=0, theta1=90, theta2=180, color=door_leaf_color, linestyle=arc_linestyle, linewidth=arc_linewidth, zorder=3))
        elif swing_direction == 'out_cw':
            hinge_x, hinge_y = x, y # Hinge is on left, outer side of wall
            ax.add_line(Line2D([hinge_x, hinge_x], [hinge_y, hinge_y - door_leaf_length], color=door_leaf_color, linewidth=door_leaf_linewidth, zorder=3))
            ax.add_patch(Arc((hinge_x, hinge_y), 2*door_leaf_length, 2*door_leaf_length, angle=0, theta1=270, theta2=360, color=door_leaf_color, linestyle=arc_linestyle, linewidth=arc_linewidth, zorder=3))
        elif swing_direction == 'out_ccw':
            hinge_x, hinge_y = x + door_leaf_length, y # Hinge is on right, outer side of wall
            ax.add_line(Line2D([hinge_x, hinge_x], [hinge_y, hinge_y - door_leaf_length], color=door_leaf_color, linewidth=door_leaf_linewidth, zorder=3))
            ax.add_patch(Arc((hinge_x, hinge_y), 2*door_leaf_length, 2*door_leaf_length, angle=0, theta1=180, theta2=270, color=door_leaf_color, linestyle=arc_linestyle, linewidth=arc_linewidth, zorder=3))
    else: # Door in a vertical wall (wall along y-axis)
        if swing_direction == 'in_cw':
            hinge_x, hinge_y = x + wall_thickness, y + door_leaf_length # Hinge is on top, inner side of wall
            ax.add_line(Line2D([hinge_x, hinge_x - door_leaf_length], [hinge_y, hinge_y], color=door_leaf_color, linewidth=door_leaf_linewidth, zorder=3))
            ax.add_patch(Arc((hinge_x, hinge_y), 2*door_leaf_length, 2*door_leaf_length, angle=0, theta1=180, theta2=270, color=door_leaf_color, linestyle=arc_linestyle, linewidth=arc_linewidth, zorder=3))
        elif swing_direction == 'in_ccw':
            hinge_x, hinge_y = x + wall_thickness, y # Hinge is on bottom, inner side of wall
            ax.add_line(Line2D([hinge_x, hinge_x - door_leaf_length], [hinge_y, hinge_y], color=door_leaf_color, linewidth=door_leaf_linewidth, zorder=3))
            ax.add_patch(Arc((hinge_x, hinge_y), 2*door_leaf_length, 2*door_leaf_length, angle=0, theta1=270, theta2=360, color=door_leaf_color, linestyle=arc_linestyle, linewidth=arc_linewidth, zorder=3))
        elif swing_direction == 'out_cw':
            hinge_x, hinge_y = x, y + door_leaf_length # Hinge is on top, outer side of wall
            ax.add_line(Line2D([hinge_x, hinge_x + door_leaf_length], [hinge_y, hinge_y], color=door_leaf_color, linewidth=door_leaf_linewidth, zorder=3))
            ax.add_patch(Arc((hinge_x, hinge_y), 2*door_leaf_length, 2*door_leaf_length, angle=0, theta1=90, theta2=180, color=door_leaf_color, linestyle=arc_linestyle, linewidth=arc_linewidth, zorder=3))
        elif swing_direction == 'out_ccw':
            hinge_x, hinge_y = x, y # Hinge is on bottom, outer side of wall
            ax.add_line(Line2D([hinge_x, hinge_x + door_leaf_length], [hinge_y, hinge_y], color=door_leaf_color, linewidth=door_leaf_linewidth, zorder=3))
            ax.add_patch(Arc((hinge_x, hinge_y), 2*door_leaf_length, 2*door_leaf_length, angle=0, theta1=0, theta2=90, color=door_leaf_color, linestyle=arc_linestyle, linewidth=arc_linewidth, zorder=3))


def draw_window(ax, x, y, length, thickness, orientation='h'):
    """Draws a window as a thin rectangle over the wall area. x,y is bottom-left of window opening."""
    if orientation == 'h': # Horizontal wall (window runs horizontally)
        ax.add_patch(Rectangle((x, y), length, thickness, facecolor=WINDOW_COLOR, edgecolor='black', linewidth=0.5, zorder=2))
        # Center line for glass
        ax.add_line(Line2D([x, x + length], [y + thickness / 2, y + thickness / 2], color='black', linewidth=1, zorder=3))
    else: # Vertical wall (window runs vertically)
        ax.add_patch(Rectangle((x, y), thickness, length, facecolor=WINDOW_COLOR, edgecolor='black', linewidth=0.5, zorder=2))
        # Center line for glass
        ax.add_line(Line2D([x + thickness / 2, x + thickness / 2], [y, y + length], color='black', linewidth=1, zorder=3))

def draw_room_label(ax, x_inner, y_inner, width_inner, height_inner, label):
    ax.text(x_inner + width_inner / 2, y_inner + height_inner / 2,
            label, ha='center', va='center', fontsize=14, color='darkslategray', alpha=0.7)

# --- KITCHEN SPECIFIC HELPER FUNCTIONS ---

def draw_kitchen_counter_segment(ax, x, y, width, height, is_vertical=False):
    """
    Draws a segment of kitchen counter with detail for base cabinets.
    x,y is bottom-left. `width` is length along wall, `height` is depth into room (or vice versa).
    """
    # Base cabinet rectangle
    ax.add_patch(Rectangle((x, y), width, height, facecolor=COUNTER_COLOR, edgecolor='black', linewidth=0.8, zorder=4))
    # Countertop (thin rectangle on top of base cabinet)
    if is_vertical: # If counter segment is vertical (along Y-axis)
        ax.add_patch(Rectangle((x, y + height - 0.05), width, 0.05, facecolor=COUNTERTOP_COLOR, edgecolor='black', linewidth=0.5, zorder=5))
        # Indicate cabinet doors/drawers with lines
        num_units = max(1, int(width / 0.6)) # Each unit approx 0.6m
        for i in range(1, num_units):
            ax.add_line(Line2D([x + i * (width / num_units), x + i * (width / num_units)], [y, y + height], color='black', linewidth=0.5, linestyle=':', zorder=5))
    else: # If counter segment is horizontal (along X-axis)
        ax.add_patch(Rectangle((x, y + height - 0.05), width, 0.05, facecolor=COUNTERTOP_COLOR, edgecolor='black', linewidth=0.5, zorder=5))
        num_units = max(1, int(width / 0.6))
        for i in range(1, num_units):
            ax.add_line(Line2D([x + i * (width / num_units), x + i * (width / num_units)], [y, y + height], color='black', linewidth=0.5, linestyle=':', zorder=5))


def draw_sink_basin(ax, x_center, y_center, size=0.4):
    """Draws a square sink basin centered at (x_center, y_center)."""
    ax.add_patch(Rectangle((x_center - size/2, y_center - size/2), size, size, facecolor=SINK_COLOR, edgecolor='black', linewidth=0.5, zorder=6))
    ax.add_line(Line2D([x_center - size/2 + 0.05, x_center + size/2 - 0.05], [y_center - size/2 + 0.05, y_center + size/2 - 0.05], color='black', linestyle=':', linewidth=0.5, zorder=7)) # Drain cross
    ax.add_line(Line2D([x_center - size/2 + 0.05, x_center + size/2 - 0.05], [y_center + size/2 - 0.05, y_center - size/2 + 0.05], color='black', linestyle=':', linewidth=0.5, zorder=7))

def draw_stove(ax, x, y, width, depth, label="Stove"):
    """Draws a stove/cooktop with oven door line. x,y is bottom-left."""
    ax.add_patch(Rectangle((x, y), width, depth, facecolor=APPLIANCE_COLOR, edgecolor='black', linewidth=0.8, zorder=4))
    # Burners (simple circles)
    burner_r = 0.08
    ax.add_patch(Circle((x + width*0.25, y + depth*0.25), burner_r, facecolor='black', zorder=5))
    ax.add_patch(Circle((x + width*0.75, y + depth*0.25), burner_r, facecolor='black', zorder=5))
    ax.add_patch(Circle((x + width*0.25, y + depth*0.75), burner_r, facecolor='black', zorder=5))
    ax.add_patch(Circle((x + width*0.75, y + depth*0.75), burner_r, facecolor='black', zorder=5))
    # Oven door line
    ax.add_line(Line2D([x + width * 0.1, x + width * 0.9], [y + depth * 0.3, y + depth * 0.3], color='white', linewidth=1.5, zorder=5))
    ax.text(x + width / 2, y + depth / 2, label, ha='center', va='center', fontsize=7, color='white', weight='bold', zorder=6)

def draw_refrigerator(ax, x, y, width, depth, label="Fridge"):
    """Draws a refrigerator. x,y is bottom-left."""
    ax.add_patch(Rectangle((x, y), width, depth, facecolor=APPLIANCE_COLOR, edgecolor='black', linewidth=0.8, zorder=4))
    # Simple lines for doors and handles
    ax.add_line(Line2D([x, x + width], [y + depth/2, y + depth/2], color='white', linestyle='--', linewidth=1.0, zorder=5)) # Freezer/Fridge split
    ax.add_line(Line2D([x + width*0.1, x + width*0.1], [y + depth*0.2, y + depth*0.4], color='white', linewidth=1.5, zorder=5)) # Handle
    ax.add_line(Line2D([x + width*0.1, x + width*0.1], [y + depth*0.6, y + depth*0.8], color='white', linewidth=1.5, zorder=5)) # Handle
    ax.text(x + width / 2, y + depth / 2, label, ha='center', va='center', fontsize=7, color='white', weight='bold', zorder=6)

def draw_dishwasher(ax, x, y, width, depth, label="Dishwasher"):
    """Draws a dishwasher. x,y is bottom-left."""
    ax.add_patch(Rectangle((x, y), width, depth, facecolor=APPLIANCE_COLOR, edgecolor='black', linewidth=0.8, zorder=4))
    # Door handle line
    ax.add_line(Line2D([x + width*0.1, x + width*0.9], [y + depth*0.15, y + depth*0.15], color='white', linewidth=1.5, zorder=5))
    # Control panel (small rectangle on top)
    ax.add_patch(Rectangle((x + width*0.1, y + depth*0.8), width*0.8, depth*0.15, facecolor='darkgray', edgecolor='black', linewidth=0.5, zorder=5))
    ax.text(x + width / 2, y + depth / 2, label, ha='center', va='center', fontsize=7, color='white', weight='bold', zorder=6)

def draw_microwave(ax, x, y, width, depth, label="Micro."):
    """Draws a small counter-top microwave. x,y is bottom-left."""
    ax.add_patch(Rectangle((x, y), width, depth, facecolor=APPLIANCE_COLOR, edgecolor='black', linewidth=0.8, zorder=4))
    # Door and controls
    ax.add_line(Line2D([x + width * 0.2, x + width * 0.2], [y + depth * 0.1, y + depth * 0.9], color='white', linewidth=1.0, zorder=5)) # Door edge
    ax.add_patch(Rectangle((x + width * 0.7, y + depth * 0.7), width * 0.2, depth * 0.2, facecolor='gray', edgecolor='black', linewidth=0.5, zorder=5)) # Control panel
    ax.text(x + width / 2, y + depth / 2, label, ha='center', va='center', fontsize=6, color='white', weight='bold', zorder=6)

def draw_exhaust_hood(ax, x, y, width, depth, label="Hood"):
    """Draws an exhaust hood, typically above a stove. x,y is bottom-left of hood base."""
    # This represents the base of the hood, slightly smaller than the stove.
    ax.add_patch(Rectangle((x, y), width, depth, facecolor=APPLIANCE_COLOR, edgecolor='black', linewidth=0.8, zorder=4, hatch='///'))
    ax.text(x + width / 2, y + depth / 2, label, ha='center', va='center', fontsize=6, color='white', weight='bold', zorder=5)

def draw_dining_table(ax, x, y, size_x, size_y, chairs=4, label="Table"):
    """Draws a dining table with chairs. x,y is bottom-left."""
    ax.add_patch(Rectangle((x, y), size_x, size_y, facecolor=FURNITURE_COLOR, edgecolor='black', linewidth=0.8, zorder=4))
    # Simple chairs as small circles
    chair_r = 0.2
    if chairs >= 2: # Top/Bottom chairs
        ax.add_patch(Circle((x + size_x / 2, y - chair_r - 0.1), chair_r, facecolor=FURNITURE_COLOR, edgecolor='black', zorder=5))
        ax.add_patch(Circle((x + size_x / 2, y + size_y + chair_r + 0.1), chair_r, facecolor=FURNITURE_COLOR, edgecolor='black', zorder=5))
    if chairs >= 4: # Side chairs
        ax.add_patch(Circle((x - chair_r - 0.1, y + size_y / 2), chair_r, facecolor=FURNITURE_COLOR, edgecolor='black', zorder=5))
        ax.add_patch(Circle((x + size_x + chair_r + 0.1, y + size_y / 2), chair_r, facecolor=FURNITURE_COLOR, edgecolor='black', zorder=5))
    ax.text(x + size_x / 2, y + size_y / 2, label, ha='center', va='center', fontsize=8, color='white', weight='bold', zorder=6)


# --- Main Kitchen Preset Generator ---

def generate_kitchen_preset(
    kitchen_width=4.5,  # Inner width of the room
    kitchen_height=3.5  # Inner height of the room
):
    fig, ax = plt.subplots(figsize=(10, 8))

    # --- 1. Define Room Boundaries ---
    room_origin_x = 0
    room_origin_y = 0

    outer_width = kitchen_width + 2 * WALL_THICKNESS
    outer_height = kitchen_height + 2 * WALL_THICKNESS

    inner_room_x = room_origin_x + WALL_THICKNESS
    inner_room_y = room_origin_y + WALL_THICKNESS

    # --- 2. Draw Walls ---
    # Outer rectangle (wall color)
    ax.add_patch(Rectangle(
        (room_origin_x, room_origin_y),
        outer_width, outer_height,
        facecolor=WALL_COLOR, edgecolor='black', linewidth=1, zorder=0
    ))
    # Inner rectangle (floor color)
    ax.add_patch(Rectangle(
        (inner_room_x, inner_room_y),
        kitchen_width, kitchen_height,
        facecolor=FLOOR_COLOR, edgecolor='black', linewidth=0, zorder=1
    ))
    '''
    # --- 3. Door ---
    # Placed on the bottom wall, near left corner
    door_pos_x = inner_room_x + 0.5
    door_pos_y = room_origin_y # Outer edge of the bottom wall (where the opening is cut)
    draw_door(ax, door_pos_x, door_pos_y, DOOR_WIDTH, WALL_THICKNESS, 'h', 'in_cw')
    '''
    # --- 4. Window ---
    # Placed on the top wall, centered
    window_pos_x = inner_room_x + (kitchen_width - WINDOW_WIDTH) / 2
    window_pos_y = inner_room_y + kitchen_height # Inner edge of the top wall
    draw_window(ax, window_pos_x, window_pos_y, WINDOW_WIDTH, WALL_THICKNESS, 'h')

    # --- 5. Kitchen Layout: L-shaped counter and appliances ---

    # Standard appliance dimensions for placement (approximate, meters)
    FRIDGE_W = 0.9 # Width along wall for a standard fridge
    FRIDGE_D = 0.7 # Depth from wall for a standard fridge (includes handle)
    STOVE_W = 0.75 # Width of stove
    STOVE_D = COUNTER_DEPTH
    SINK_W = 0.8 # Width of sink cabinet
    SINK_D = COUNTER_DEPTH
    DISHWASHER_W = 0.6 # Width of dishwasher
    DISHWASHER_D = COUNTER_DEPTH
    MICROWAVE_W = 0.5
    MICROWAVE_D = 0.4

    # Calculate main counter segment lengths
    # We will run counters along the left and top walls for an L-shape
    # Ensure there's enough space for fridge at one end of the left wall counter.
    # The fridge will be placed against the leftmost wall.

    # Refrigerator placement (at the bottom-left corner against the left wall)
    fridge_x = inner_room_x # Against left inner wall
    fridge_y = inner_room_y + 0.1 # Small offset from door/bottom wall
    draw_refrigerator(ax, fridge_x, fridge_y, FRIDGE_D, FRIDGE_W) # Fridge is deeper than it is wide on plan

    # Counter 1: Along the left wall (excluding fridge space, goes up to the corner)
    counter1_x = inner_room_x # Against the left inner wall
    counter1_y_start = fridge_y + FRIDGE_W + 0.1 # Starts after fridge + small gap
    counter1_length = kitchen_height - (counter1_y_start - inner_room_y) # Length up to top inner wall
    draw_kitchen_counter_segment(ax, counter1_x, counter1_y_start, COUNTER_DEPTH, counter1_length, is_vertical=True)

    # Counter 2: Along the top wall (excluding the corner piece used by counter1's depth)
    counter2_x_start = inner_room_x + COUNTER_DEPTH # Starts from the inner corner after counter1's depth
    counter2_y = inner_room_y + kitchen_height - COUNTER_DEPTH # Aligned with top inner wall
    counter2_length = kitchen_width - COUNTER_DEPTH # Extends to the right inner wall

    # Placement of sink, dishwasher, stove on Counter 2 (top wall)
    # Sink under the window
    sink_x = window_pos_x + WINDOW_WIDTH / 2 - SINK_W / 2
    sink_y = counter2_y # Aligned with counter

    # Dishwasher: To the left of the sink
    dishwasher_x = sink_x - DISHWASHER_W - 0.1 # Small gap
    dishwasher_y = counter2_y # Aligned with counter

    # Stove: To the right of the sink
    stove_x = sink_x + SINK_W + 0.1 # Small gap
    stove_y = counter2_y # Aligned with counter

    # Ensure appliances fit within counter2_length
    if dishwasher_x < counter2_x_start:
        dishwasher_x = counter2_x_start # Adjust if too close to corner

    # Draw Counter 2 segment
    draw_kitchen_counter_segment(ax, counter2_x_start, counter2_y, counter2_length, COUNTER_DEPTH, is_vertical=False)

    # Draw appliances on Counter 2
    draw_dishwasher(ax, dishwasher_x, dishwasher_y, DISHWASHER_W, DISHWASHER_D)
    draw_sink_basin(ax, sink_x + SINK_W/2, sink_y + SINK_D/2)
    ax.text(sink_x + SINK_W/2, sink_y + SINK_D/2 - 0.4, "Sink", ha='center', va='center', fontsize=7, color='darkslategray', zorder=6)
    draw_stove(ax, stove_x, stove_y, STOVE_W, STOVE_D)

    # Exhaust Hood above stove
    hood_width = STOVE_W * 0.9 # Slightly narrower than stove
    hood_depth = OVERHEAD_CABINET_DEPTH # Matches overhead cabinet depth
    draw_exhaust_hood(ax, stove_x + (STOVE_W - hood_width)/2, stove_y + STOVE_D - hood_depth, hood_width, hood_depth) # Placed above stove on countertop


    # --- Overhead Cabinets ---
    # Overhead cabinets run above the base cabinets, but are less deep.
    # They are drawn relative to the wall, not the counter edge.

    # --- Optional: Small Microwave on Counter ---
    microwave_x = stove_x + STOVE_W + 0.1 # To the right of stove
    microwave_y = counter2_y + (COUNTER_DEPTH - MICROWAVE_D) / 2 # Centered on counter depth
    if microwave_x + MICROWAVE_W < inner_room_x + kitchen_width: # Ensure it fits on the counter
        draw_microwave(ax, microwave_x, microwave_y, MICROWAVE_W, MICROWAVE_D)

    # --- Optional: Small Dining Table/Island in the center ---
    table_w = 1.0
    table_h = 0.8
    table_x = inner_room_x + (kitchen_width - table_w) / 2
    table_y = inner_room_y + 0.5 # Positioned more centrally, away from door/fridge
    if table_y + table_h < counter1_y_start - 0.2: # Ensure it doesn't overlap fridge/counter
         draw_dining_table(ax, table_x, table_y, table_w, table_h, chairs=2, label="Island")


    # --- 6. Room Label ---
    draw_room_label(ax, inner_room_x, inner_room_y, kitchen_width, kitchen_height, "KITCHEN")

    # --- 7. Plot Settings ---
    ax.set_aspect('equal', adjustable='box')
    ax.set_xlim(room_origin_x - 0.5, room_origin_x + outer_width + 0.5)
    ax.set_ylim(room_origin_y - 0.5, room_origin_y + outer_height + 0.5)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title(f"Detailed Kitchen Floor Plan ({kitchen_width:.1f}x{kitchen_height:.1f}m)", fontsize=16)
    ax.grid(False)

    plt.show()

# --- Call the function to generate the plot ---
generate_kitchen_preset()

# --- Example with different dimensions ---
# generate_kitchen_preset(kitchen_width=3.8, kitchen_height=3.2)