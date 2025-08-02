import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Arc, Circle
from matplotlib.lines import Line2D

# --- Constants for dimensions and appearance ---
WALL_THICKNESS = 0.15 # meters
DOOR_WIDTH = 0.9
WINDOW_WIDTH = 2.0 # Wider for living room

# Colors
WALL_COLOR = '#b0b0b0' # Gray
FLOOR_COLOR = 'white'
SOFA_COLOR = '#4682b4' # SteelBlue
ACCENT_CHAIR_COLOR = '#8b4513' # SaddleBrown
TABLE_COLOR = '#d2b48c' # Tan
RUG_COLOR = '#f0f8ff' # AliceBlue (light for contrast)
TV_COLOR = '#1c1c1c' # Dark gray/black
DOOR_COLOR = 'white'
WINDOW_COLOR = '#add8e6'
BOOKSHELF_COLOR = '#8b4513' # Same as accent chair for wood consistency

# --- Helper Functions (Reused and Adapted) ---

def draw_door(ax, x, y, door_leaf_length, wall_thickness, orientation='h', swing_direction='in_cw'):
    """Draws a door opening with swing. x,y: bottom-left of the opening."""
    if orientation == 'h':
        ax.add_patch(Rectangle((x, y), door_leaf_length, wall_thickness, facecolor=FLOOR_COLOR, edgecolor=FLOOR_COLOR, linewidth=0, zorder=2))
    else: # 'v'
        ax.add_patch(Rectangle((x, y), wall_thickness, door_leaf_length, facecolor=FLOOR_COLOR, edgecolor=FLOOR_COLOR, linewidth=0, zorder=2))

    door_leaf_color = 'black'
    door_leaf_linewidth = 1.5
    arc_linewidth = 0.8
    arc_linestyle = ':'

    if orientation == 'h':
        if swing_direction == 'in_cw':
            hinge_x, hinge_y = x, y + wall_thickness
            ax.add_line(Line2D([hinge_x, hinge_x], [hinge_y, hinge_y + door_leaf_length], color=door_leaf_color, linewidth=door_leaf_linewidth, zorder=3))
            ax.add_patch(Arc((hinge_x, hinge_y), 2*door_leaf_length, 2*door_leaf_length, angle=0, theta1=0, theta2=90, color=door_leaf_color, linestyle=arc_linestyle, linewidth=arc_linewidth, zorder=3))
        elif swing_direction == 'in_ccw':
            hinge_x, hinge_y = x + door_leaf_length, y + wall_thickness
            ax.add_line(Line2D([hinge_x, hinge_x], [hinge_y, hinge_y + door_leaf_length], color=door_leaf_color, linewidth=door_leaf_linewidth, zorder=3))
            ax.add_patch(Arc((hinge_x, hinge_y), 2*door_leaf_length, 2*door_leaf_length, angle=0, theta1=90, theta2=180, color=door_leaf_color, linestyle=arc_linestyle, linewidth=arc_linewidth, zorder=3))
    else: # 'v'
        if swing_direction == 'in_cw':
            hinge_x, hinge_y = x + wall_thickness, y + door_leaf_length
            ax.add_line(Line2D([hinge_x, hinge_x - door_leaf_length], [hinge_y, hinge_y], color=door_leaf_color, linewidth=door_leaf_linewidth, zorder=3))
            ax.add_patch(Arc((hinge_x, hinge_y), 2*door_leaf_length, 2*door_leaf_length, angle=0, theta1=180, theta2=270, color=door_leaf_color, linestyle=arc_linestyle, linewidth=arc_linewidth, zorder=3))
        elif swing_direction == 'in_ccw':
            hinge_x, hinge_y = x + wall_thickness, y
            ax.add_line(Line2D([hinge_x, hinge_x - door_leaf_length], [hinge_y, hinge_y], color=door_leaf_color, linewidth=door_leaf_linewidth, zorder=3))
            ax.add_patch(Arc((hinge_x, hinge_y), 2*door_leaf_length, 2*door_leaf_length, angle=0, theta1=270, theta2=360, color=door_leaf_color, linestyle=arc_linestyle, linewidth=arc_linewidth, zorder=3))

def draw_window(ax, x, y, length, thickness, orientation='h'):
    """Draws a window as a thin rectangle over the wall area. x,y is bottom-left of window opening."""
    if orientation == 'h':
        ax.add_patch(Rectangle((x, y), length, thickness, facecolor=WINDOW_COLOR, edgecolor='black', linewidth=0.5, zorder=2))
        ax.add_line(Line2D([x, x + length], [y + thickness / 2, y + thickness / 2], color='black', linewidth=1, zorder=3))
    else:
        ax.add_patch(Rectangle((x, y), thickness, length, facecolor=WINDOW_COLOR, edgecolor='black', linewidth=0.5, zorder=2))
        ax.add_line(Line2D([x + thickness / 2, x + thickness / 2], [y, y + length], color='black', linewidth=1, zorder=3))

def draw_room_label(ax, x_inner, y_inner, width_inner, height_inner, label):
    ax.text(x_inner + width_inner / 2, y_inner + height_inner / 2,
            label, ha='center', va='center', fontsize=16, color='darkslategray', alpha=0.7)

# --- LIVING ROOM SPECIFIC HELPER FUNCTIONS ---

def draw_sofa(ax, x, y, width, height, label="Sofa"):
    """
    Draws a sofa with cushions. x,y is bottom-left.
    width: length of the sofa along the wall.
    height: depth of the sofa into the room.
    """
    ax.add_patch(Rectangle((x, y), width, height, facecolor=SOFA_COLOR, edgecolor='black', linewidth=0.8, zorder=5))
    # Cushions
    num_cushions = max(1, int(width / 0.7)) # Roughly one cushion per 0.7m
    cushion_width = (width - 0.1 * (num_cushions + 1)) / num_cushions # Distribute with small gaps
    cushion_depth = height * 0.8 # Cushions are slightly less deep than sofa
    cushion_offset_y = height * 0.1 # Small offset from back
    for i in range(num_cushions):
        ax.add_patch(Rectangle(
            (x + 0.05 + i * (cushion_width + 0.05), y + cushion_offset_y),
            cushion_width, cushion_depth, facecolor=SOFA_COLOR, edgecolor='darkblue', linewidth=0.5, zorder=6, alpha=0.8
        ))
    ax.text(x + width / 2, y + height / 2, label, ha='center', va='center', fontsize=9, color='white', weight='bold', zorder=7)

def draw_armchair(ax, x, y, size_x, size_y, label="Armchair"):
    """Draws an armchair. x,y is bottom-left."""
    ax.add_patch(Rectangle((x, y), size_x, size_y, facecolor=ACCENT_CHAIR_COLOR, edgecolor='black', linewidth=0.8, zorder=5))
    # Simple armrests
    ax.add_patch(Rectangle((x, y), size_x*0.15, size_y, facecolor=ACCENT_CHAIR_COLOR, edgecolor='black', linewidth=0.5, zorder=6))
    ax.add_patch(Rectangle((x + size_x*0.85, y), size_x*0.15, size_y, facecolor=ACCENT_CHAIR_COLOR, edgecolor='black', linewidth=0.5, zorder=6))
    ax.text(x + size_x / 2, y + size_y / 2, label, ha='center', va='center', fontsize=8, color='white', weight='bold', zorder=7)

def draw_coffee_table(ax, x, y, width, depth, label="Coffee Table"):
    """Draws a coffee table. x,y is bottom-left."""
    ax.add_patch(Rectangle((x, y), width, depth, facecolor=TABLE_COLOR, edgecolor='black', linewidth=1, zorder=5))
    ax.text(x + width / 2, y + depth / 2, label, ha='center', va='center', fontsize=8, color='black', weight='bold', zorder=6)

def draw_tv_stand(ax, x, y, width, depth, label="TV"):
    """Draws a TV stand with a TV screen. x,y is bottom-left."""
    ax.add_patch(Rectangle((x, y), width, depth, facecolor=TABLE_COLOR, edgecolor='black', linewidth=1, zorder=5))
    # TV Screen (on top of stand)
    tv_screen_w = width * 0.7
    tv_screen_h = depth * 0.5 # Proportionate height on floor plan
    ax.add_patch(Rectangle(
        (x + (width - tv_screen_w)/2, y + depth - tv_screen_h - 0.05), # Positioned at back of stand
        tv_screen_w, tv_screen_h, facecolor=TV_COLOR, edgecolor='gray', linewidth=1, zorder=6
    ))
    ax.text(x + width / 2, y + depth * 0.8, label, ha='center', va='center', fontsize=9, color='white', weight='bold', zorder=7)

def draw_area_rug(ax, x, y, width, height, color=RUG_COLOR, label="Rug"):
    """Draws an area rug. x,y is bottom-left."""
    ax.add_patch(Rectangle((x, y), width, height, facecolor=color, edgecolor='darkgray', linewidth=0.5, linestyle='--', zorder=4))
    ax.text(x + width/2, y + height/2, label, ha='center', va='center', fontsize=10, color='darkslategray', alpha=0.6, zorder=5)

def draw_bookshelf(ax, x, y, width, depth, label="Bookshelf", orientation='v'):
    """Draws a bookshelf. x,y is bottom-left."""
    if orientation == 'v': # Along a vertical wall, depth into room
        ax.add_patch(Rectangle((x, y), depth, width, facecolor=BOOKSHELF_COLOR, edgecolor='black', linewidth=0.8, zorder=5))
        # Shelves (horizontal lines)
        num_shelves = max(2, int(width / 0.8)) # At least 2, roughly every 0.8m
        for i in range(1, num_shelves):
            ax.add_line(Line2D([x, x + depth], [y + i * (width / num_shelves), y + i * (width / num_shelves)], color='black', linewidth=0.5, linestyle='-', zorder=6))
        ax.text(x + depth/2, y + width/2, label, rotation=90, ha='center', va='center', fontsize=8, color='white', weight='bold', zorder=7)
    else: # Along a horizontal wall, depth into room
        ax.add_patch(Rectangle((x, y), width, depth, facecolor=BOOKSHELF_COLOR, edgecolor='black', linewidth=0.8, zorder=5))
        num_shelves = max(2, int(width / 0.8))
        for i in range(1, num_shelves):
            ax.add_line(Line2D([x + i * (width / num_shelves), x + i * (width / num_shelves)], [y, y + depth], color='black', linewidth=0.5, linestyle='-', zorder=6))
        ax.text(x + width/2, y + depth/2, label, ha='center', va='center', fontsize=8, color='white', weight='bold', zorder=7)


# --- Main Living Room Preset Generator ---

def generate_living_room_preset(
    room_width=5.5,  # Inner width of the room (e.g., along TV wall)
    room_height=4.5  # Inner height of the room (e.g., along sofa wall)
):
    fig, ax = plt.subplots(figsize=(10, 8))

    # --- 1. Define Room Boundaries ---
    room_origin_x = 0
    room_origin_y = 0

    outer_width = room_width + 2 * WALL_THICKNESS
    outer_height = room_height + 2 * WALL_THICKNESS

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
        room_width, room_height,
        facecolor=FLOOR_COLOR, edgecolor='black', linewidth=0, zorder=1
    ))
    '''
    # --- 3. Door ---
    # Placed on the bottom wall, near the right corner
    door_pos_x = inner_room_x + room_width - DOOR_WIDTH - 0.5 # Offset from right wall
    door_pos_y = room_origin_y
    draw_door(ax, door_pos_x, door_pos_y, DOOR_WIDTH, WALL_THICKNESS, 'h', 'in_ccw') # Swings into the room
    '''
    # --- 4. Window ---
    # Placed on the left wall, centered
    window_pos_x = room_origin_x # Outer edge of left wall
    window_pos_y = inner_room_y + (room_height - WINDOW_WIDTH) / 2
    draw_window(ax, window_pos_x, window_pos_y, WINDOW_WIDTH, WALL_THICKNESS, 'v')


    # --- 5. Living Room Furniture Layout ---
    SOFA_W = 3.0 # Width (length) of sofa
    SOFA_D = 1.0 # Depth of sofa
    ARMCHAIR_S = 0.9 # Size of armchair (square)
    COFFEE_TABLE_W = 1.2
    COFFEE_TABLE_D = 0.7
    TV_STAND_W = 2.0
    TV_STAND_D = 0.4
    RUG_W = 4.0 # Rug width (across room)
    RUG_H = 3.0 # Rug height (along room)
    BOOKSHELF_W = 1.5
    BOOKSHELF_D = 0.35
    
    # Area Rug: Defines the main seating zone, centered
    rug_x = inner_room_x + (room_width - RUG_W) / 2
    rug_y = inner_room_y + (room_height - RUG_H) / 2
    #draw_area_rug(ax, rug_x, rug_y, RUG_W, RUG_H)
    
    # Main Sofa: Placed against the top wall, centered on the rug
    sofa_x = rug_x + (RUG_W - SOFA_W) / 2
    sofa_y = rug_y + RUG_H - SOFA_D # Aligned with top edge of rug
    draw_sofa(ax, sofa_x, sofa_y, SOFA_W, SOFA_D, "3-Seater Sofa")

    # Coffee Table: In front of the sofa, centered on the rug
    coffee_table_x = rug_x + (RUG_W - COFFEE_TABLE_W) / 2
    coffee_table_y = sofa_y - COFFEE_TABLE_D - 0.2 # Small gap between sofa and table
    draw_coffee_table(ax, coffee_table_x, coffee_table_y, COFFEE_TABLE_W, COFFEE_TABLE_D)

    # Armchairs: Two armchairs, one on each side of the coffee table, facing the TV.
    # Armchair 1 (left of coffee table)
    armchair1_x = rug_x # Aligned with left edge of rug
    armchair1_y = coffee_table_y + (COFFEE_TABLE_D - ARMCHAIR_S) / 2 # Centered with coffee table depth
    draw_armchair(ax, armchair1_x, armchair1_y, ARMCHAIR_S, ARMCHAIR_S, "Armchair")

    # Armchair 2 (right of coffee table)
    armchair2_x = rug_x + RUG_W - ARMCHAIR_S # Aligned with right edge of rug
    armchair2_y = coffee_table_y + (COFFEE_TABLE_D - ARMCHAIR_S) / 2 # Centered with coffee table depth
    draw_armchair(ax, armchair2_x, armchair2_y, ARMCHAIR_S, ARMCHAIR_S, "Armchair")


    # TV Stand: On the bottom wall, opposite the sofa, centered.    
    tv_stand_x = inner_room_x + (room_width - TV_STAND_W) / 2
    tv_stand_y = inner_room_y # Aligned with bottom inner wall
    draw_tv_stand(ax, tv_stand_x, tv_stand_y, TV_STAND_W, TV_STAND_D)
    '''
    # Bookshelf: On the right wall, away from the door.
    bookshelf_x = inner_room_x + room_width - BOOKSHELF_D # Aligned with right inner wall
    bookshelf_y = inner_room_y + room_height - BOOKSHELF_W - 0.2 # Offset from top corner
    draw_bookshelf(ax, bookshelf_x, bookshelf_y, BOOKSHELF_W, BOOKSHELF_D, orientation='v')
    '''

    # --- 6. Room Label ---
    draw_room_label(ax, inner_room_x, inner_room_y, room_width, room_height, "LIVING\nROOM")

    # --- 7. Plot Settings ---
    ax.set_aspect('equal', adjustable='box')
    ax.set_xlim(room_origin_x - 0.5, room_origin_x + outer_width + 0.5)
    ax.set_ylim(room_origin_y - 0.5, room_origin_y + outer_height + 0.5)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title(f"Detailed Living Room Floor Plan ({room_width:.1f}x{room_height:.1f}m)", fontsize=16)
    ax.grid(False)

    plt.show()

# --- Call the function to generate the plot ---
generate_living_room_preset()

# --- Example with different dimensions ---
# generate_living_room_preset(room_width=6.0, room_height=5.0)