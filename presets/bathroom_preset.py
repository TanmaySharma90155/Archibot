import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Arc, Circle
from matplotlib.lines import Line2D

# --- Constants for dimensions and appearance ---
WALL_THICKNESS = 0.15 # meters
DOOR_WIDTH_BATH = 0.7
WINDOW_WIDTH_BATH = 0.6 # Typically smaller for bathrooms

# Colors
WALL_COLOR = '#b0b0b0' # Gray
FLOOR_COLOR = 'white'
FIXTURE_COLOR = '#e0ffff' # Light Cyan (for porcelain look)
APPLIANCE_COLOR = '#696969' # Dim Gray
VANITY_COLOR = '#a0522d' # Sienna (wood look)
SINK_BASIN_COLOR = 'lightgray'
DOOR_COLOR = 'white'
WINDOW_COLOR = '#add8e6'

# --- Helper Functions (Reused) ---

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
            hinge_x, hinge_y = x, y + wall_thickness
            ax.add_line(Line2D([hinge_x, hinge_x], [hinge_y, hinge_y + door_leaf_length], color=door_leaf_color, linewidth=door_leaf_linewidth, zorder=3))
            ax.add_patch(Arc((hinge_x, hinge_y), 2*door_leaf_length, 2*door_leaf_length, angle=0, theta1=0, theta2=90, color=door_leaf_color, linestyle=arc_linestyle, linewidth=arc_linewidth, zorder=3))
        elif swing_direction == 'in_ccw':
            hinge_x, hinge_y = x + door_leaf_length, y + wall_thickness
            ax.add_line(Line2D([hinge_x, hinge_x], [hinge_y, hinge_y + door_leaf_length], color=door_leaf_color, linewidth=door_leaf_linewidth, zorder=3))
            ax.add_patch(Arc((hinge_x, hinge_y), 2*door_leaf_length, 2*door_leaf_length, angle=0, theta1=90, theta2=180, color=door_leaf_color, linestyle=arc_linestyle, linewidth=arc_linewidth, zorder=3))
        elif swing_direction == 'out_cw':
            hinge_x, hinge_y = x, y
            ax.add_line(Line2D([hinge_x, hinge_x], [hinge_y, hinge_y - door_leaf_length], color=door_leaf_color, linewidth=door_leaf_linewidth, zorder=3))
            ax.add_patch(Arc((hinge_x, hinge_y), 2*door_leaf_length, 2*door_leaf_length, angle=0, theta1=270, theta2=360, color=door_leaf_color, linestyle=arc_linestyle, linewidth=arc_linewidth, zorder=3))
        elif swing_direction == 'out_ccw':
            hinge_x, hinge_y = x + door_leaf_length, y
            ax.add_line(Line2D([hinge_x, hinge_x], [hinge_y, hinge_y - door_leaf_length], color=door_leaf_color, linewidth=door_leaf_linewidth, zorder=3))
            ax.add_patch(Arc((hinge_x, hinge_y), 2*door_leaf_length, 2*door_leaf_length, angle=0, theta1=180, theta2=270, color=door_leaf_color, linestyle=arc_linestyle, linewidth=arc_linewidth, zorder=3))
    else: # Door in a vertical wall (wall along y-axis)
        if swing_direction == 'in_cw':
            hinge_x, hinge_y = x + wall_thickness, y + door_leaf_length
            ax.add_line(Line2D([hinge_x, hinge_x - door_leaf_length], [hinge_y, hinge_y], color=door_leaf_color, linewidth=door_leaf_linewidth, zorder=3))
            ax.add_patch(Arc((hinge_x, hinge_y), 2*door_leaf_length, 2*door_leaf_length, angle=0, theta1=180, theta2=270, color=door_leaf_color, linestyle=arc_linestyle, linewidth=arc_linewidth, zorder=3))
        elif swing_direction == 'in_ccw':
            hinge_x, hinge_y = x + wall_thickness, y
            ax.add_line(Line2D([hinge_x, hinge_x - door_leaf_length], [hinge_y, hinge_y], color=door_leaf_color, linewidth=door_leaf_linewidth, zorder=3))
            ax.add_patch(Arc((hinge_x, hinge_y), 2*door_leaf_length, 2*door_leaf_length, angle=0, theta1=270, theta2=360, color=door_leaf_color, linestyle=arc_linestyle, linewidth=arc_linewidth, zorder=3))
        elif swing_direction == 'out_cw':
            hinge_x, hinge_y = x, y + door_leaf_length
            ax.add_line(Line2D([hinge_x, hinge_x + door_leaf_length], [hinge_y, hinge_y], color=door_leaf_color, linewidth=door_leaf_linewidth, zorder=3))
            ax.add_patch(Arc((hinge_x, hinge_y), 2*door_leaf_length, 2*door_leaf_length, angle=0, theta1=90, theta2=180, color=door_leaf_color, linestyle=arc_linestyle, linewidth=arc_linewidth, zorder=3))
        elif swing_direction == 'out_ccw':
            hinge_x, hinge_y = x, y
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

# --- BATHROOM SPECIFIC HELPER FUNCTIONS ---

def draw_toilet(ax, x, y, orientation='N', label="WC"):
    """
    Draws a toilet. x,y is bottom-left corner of its bounding box.
    orientation: 'N' (north/up), 'S' (south/down), 'E' (east/right), 'W' (west/left) for seat direction.
    """
    width_fixture, length_fixture = 0.4, 0.7 # standard toilet dims (width x depth)
    
    if orientation == 'N': # seat facing North (up)
        ax.add_patch(Rectangle((x, y), width_fixture, length_fixture, facecolor=FIXTURE_COLOR, edgecolor='black', linewidth=0.8, zorder=4))
        ax.add_patch(Rectangle((x, y + length_fixture * 0.6), width_fixture, length_fixture * 0.4, facecolor='gray', edgecolor='black', linewidth=0.5, zorder=5)) # Tank
        text_x, text_y = x + width_fixture/2, y + length_fixture/2
    elif orientation == 'S': # seat facing South (down)
        ax.add_patch(Rectangle((x, y), width_fixture, length_fixture, facecolor=FIXTURE_COLOR, edgecolor='black', linewidth=0.8, zorder=4))
        ax.add_patch(Rectangle((x, y), width_fixture, length_fixture * 0.4), facecolor='gray', edgecolor='black', linewidth=0.5, zorder=5) # Tank at bottom
        text_x, text_y = x + width_fixture/2, y + length_fixture/2
    elif orientation == 'E': # seat facing East (right)
        ax.add_patch(Rectangle((x, y), length_fixture, width_fixture, facecolor=FIXTURE_COLOR, edgecolor='black', linewidth=0.8, zorder=4))
        ax.add_patch(Rectangle((x, y), length_fixture * 0.4, width_fixture, facecolor='gray', edgecolor='black', linewidth=0.5, zorder=5)) # Tank at left
        text_x, text_y = x + length_fixture/2, y + width_fixture/2
    elif orientation == 'W': # seat facing West (left)
        ax.add_patch(Rectangle((x, y), length_fixture, width_fixture, facecolor=FIXTURE_COLOR, edgecolor='black', linewidth=0.8, zorder=4))
        ax.add_patch(Rectangle((x + length_fixture * 0.6, y), length_fixture * 0.4, width_fixture, facecolor='gray', edgecolor='black', linewidth=0.5, zorder=5)) # Tank at right
        text_x, text_y = x + length_fixture/2, y + width_fixture/2
    ax.text(text_x, text_y, label, ha='center', va='center', fontsize=7, color='darkslategray', zorder=6)

def draw_vanity_sink(ax, x, y, width, depth, label="Vanity"):
    """Draws a vanity unit with an integrated sink. x,y is bottom-left."""
    # Vanity cabinet
    ax.add_patch(Rectangle((x, y), width, depth, facecolor=VANITY_COLOR, edgecolor='black', linewidth=0.8, zorder=4))
    # Countertop (thin layer on top)
    ax.add_patch(Rectangle((x, y + depth - 0.05), width, 0.05, facecolor=APPLIANCE_COLOR, edgecolor='black', linewidth=0.5, zorder=5))
    # Basin (circular or rectangular)
    basin_r = 0.2
    ax.add_patch(Circle((x + width/2, y + depth/2), basin_r, facecolor=SINK_BASIN_COLOR, edgecolor='black', linewidth=0.5, zorder=6))
    ax.text(x + width/2, y + depth/2 + 0.3, label, ha='center', va='center', fontsize=7, color='white', weight='bold', zorder=6)

def draw_shower(ax, x, y, width, height, label="Shower"):
    """Draws a shower stall. x,y is bottom-left."""
    ax.add_patch(Rectangle((x, y), width, height, facecolor=FIXTURE_COLOR, edgecolor='black', linewidth=0.8, zorder=4))
    ax.add_line(Line2D([x, x + width], [y + height, y], color='blue', linestyle='--', linewidth=0.8, zorder=5)) # Cross-lines for drain
    ax.add_line(Line2D([x, x + width], [y, y + height], color='blue', linestyle='--', linewidth=0.8, zorder=5))
    ax.text(x + width/2, y + height/2, label, ha='center', va='center', fontsize=7, color='darkslategray', zorder=6)

def draw_bathtub(ax, x, y, width, height, label="Tub", orientation='h'):
    """
    Draws a bathtub. x,y is bottom-left.
    orientation: 'h' for horizontal, 'v' for vertical placement.
    """
    if orientation == 'h':
        ax.add_patch(Rectangle((x, y), width, height, facecolor=FIXTURE_COLOR, edgecolor='black', linewidth=0.8, zorder=4))
        # Indicate inner tub shape
        ax.add_patch(Rectangle((x + 0.1, y + 0.1), width - 0.2, height - 0.2, facecolor='white', edgecolor='black', linewidth=0.5, zorder=5))
        # Faucet/Drain
        ax.add_patch(Circle((x + 0.2, y + height - 0.15), 0.05, facecolor='gray', edgecolor='black', zorder=6))
        ax.text(x + width/2, y + height/2, label, ha='center', va='center', fontsize=7, color='darkslategray', zorder=6)
    else: # Vertical
        ax.add_patch(Rectangle((x, y), height, width, facecolor=FIXTURE_COLOR, edgecolor='black', linewidth=0.8, zorder=4))
        ax.add_patch(Rectangle((x + 0.1, y + 0.1), height - 0.2, width - 0.2, facecolor='white', edgecolor='black', linewidth=0.5, zorder=5))
        ax.add_patch(Circle((x + height - 0.15, y + 0.2), 0.05, facecolor='gray', edgecolor='black', zorder=6))
        ax.text(x + height/2, y + width/2, label, ha='center', va='center', fontsize=7, color='darkslategray', zorder=6)


# --- Main Bathroom Preset Generator ---

def generate_bathroom_preset(
    bathroom_width=2.5,  # Inner width of the room
    bathroom_height=3.0, # Inner height of the room
    fixture_layout="shower" # "shower" or "bathtub"
):
    fig, ax = plt.subplots(figsize=(8, 7))

    # --- 1. Define Room Boundaries ---
    room_origin_x = 0
    room_origin_y = 0

    outer_width = bathroom_width + 2 * WALL_THICKNESS
    outer_height = bathroom_height + 2 * WALL_THICKNESS

    inner_room_x = room_origin_x + WALL_THICKNESS
    inner_room_y = room_origin_y + WALL_THICKNESS

    # --- 2. Draw Walls ---
    ax.add_patch(Rectangle(
        (room_origin_x, room_origin_y),
        outer_width, outer_height,
        facecolor=WALL_COLOR, edgecolor='black', linewidth=1, zorder=0
    ))
    ax.add_patch(Rectangle(
        (inner_room_x, inner_room_y),
        bathroom_width, bathroom_height,
        facecolor=FLOOR_COLOR, edgecolor='black', linewidth=0, zorder=1
    ))
    '''
    # --- 3. Door ---
    # Placed on the bottom wall, near right corner (common for small baths)
    door_pos_x = inner_room_x + bathroom_width - DOOR_WIDTH_BATH - 0.2 # Offset from right wall
    door_pos_y = room_origin_y
    draw_door(ax, door_pos_x, door_pos_y, DOOR_WIDTH_BATH, WALL_THICKNESS, 'h', 'in_ccw') # Swings into the bathroom
    '''
    # --- 4. Window ---
    # Placed on the left wall, centered (common placement for privacy)
    window_length = WINDOW_WIDTH_BATH # Use bath specific window width
    window_pos_x = room_origin_x # Outer edge of left wall
    window_pos_y = inner_room_y + (bathroom_height - window_length) / 2
    draw_window(ax, window_pos_x, window_pos_y, window_length, WALL_THICKNESS, 'v')


    # --- 5. Bathroom Fixtures ---
    # Standard fixture dimensions (approximate, meters)
    TOILET_W = 0.4
    TOILET_D = 0.7
    VANITY_W = 0.8
    VANITY_D = 0.5
    SHOWER_W = 0.9
    SHOWER_H = 0.9 # For square shower
    TUB_W = 1.6 # Length of a standard tub
    TUB_H = 0.75 # Width/depth of a standard tub


    # Toilet: Often placed opposite the door or in a corner
    # Place in top-right corner, facing left (East)
    toilet_x = inner_room_x + bathroom_width - TOILET_D - 0.1 # Offset from right wall
    toilet_y = inner_room_y + bathroom_height - TOILET_W - 0.1 # Offset from top wall
    draw_toilet(ax, toilet_x, toilet_y, orientation='W')


    # Vanity and Sink: Along a wall, usually opposite the shower/tub
    # Place on the right wall, near the door
    vanity_x = inner_room_x + bathroom_width - VANITY_D # Aligned with right inner wall
    vanity_y = inner_room_y + 0.1 # Offset from door/bottom wall
    draw_vanity_sink(ax, vanity_x, vanity_y, VANITY_D, VANITY_W, label="Vanity") # Vanity is deeper than wide on plan


    # Shower or Bathtub: Takes up a significant portion of space
    if fixture_layout == "shower":
        # Shower: Place in bottom-left corner
        shower_x = inner_room_x + 0.1 # Offset from left wall
        shower_y = inner_room_y + 0.1 # Offset from bottom wall (away from door)
        # Ensure it fits:
        if shower_x + SHOWER_W > inner_room_x + bathroom_width - (TOILET_D + 0.1) or \
           shower_y + SHOWER_H > inner_room_y + bathroom_height - (TOILET_W + 0.1):
            print("Warning: Shower might overlap with other fixtures or be too large for room.")
            # Adjust or handle error gracefully
        draw_shower(ax, shower_x, shower_y, SHOWER_W, SHOWER_H)
    elif fixture_layout == "bathtub":
        # Bathtub: Typically placed along a longer wall.
        # Place along the left wall, covering the area from bottom up.
        tub_x = inner_room_x # Against left inner wall
        tub_y = inner_room_y + 0.1 # Offset from door
        # Ensure it fits:
        if tub_y + TUB_H > inner_room_y + bathroom_height - (TOILET_W + 0.1):
             print("Warning: Bathtub might overlap with other fixtures or be too large for room.")
             # Adjust or handle error gracefully
        draw_bathtub(ax, tub_x, tub_y, TUB_H, TUB_W, orientation='v') # Tub is usually length along wall, width into room

    # --- 6. Room Label ---
    draw_room_label(ax, inner_room_x, inner_room_y, bathroom_width, bathroom_height, "BATHROOM")

    # --- 7. Plot Settings ---
    ax.set_aspect('equal', adjustable='box')
    ax.set_xlim(room_origin_x - 0.5, room_origin_x + outer_width + 0.5)
    ax.set_ylim(room_origin_y - 0.5, room_origin_y + outer_height + 0.5)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title(f"Detailed Bathroom Floor Plan ({bathroom_width:.1f}x{bathroom_height:.1f}m)", fontsize=16)
    ax.grid(False)

    plt.show()

# --- Call the function to generate the plot with a shower ---
generate_bathroom_preset(fixture_layout="shower")

# --- Call the function to generate the plot with a bathtub ---
# generate_bathroom_preset(fixture_layout="bathtub", bathroom_width=2.5, bathroom_height=3.5)