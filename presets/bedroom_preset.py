import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Arc
from matplotlib.lines import Line2D

def draw_bed(ax, x, y, width, length,
             bed_base_color='#d3d3d3',      # Light grey for mattress/frame
             headboard_color='#8b4513',     # Brown for headboard
             blanket_color='#add8e6',       # Light blue for blanket
             pillow_color='#f0f8ff',        # Off-white for pillows
             bed_label="Bed"):
    """
    Draws a detailed bed on the given Matplotlib axes.
    Assumes (x,y) is the bottom-left corner of the bed's bounding box.
    'width' is the width of the bed (e.g., across the sleeping person).
    'length' is the length of the bed (e.g., head to toe).
    """

    # --- Z-orders for layering ---
    # Headboard (behind mattress)
    # Mattress/Base
    # Blanket
    # Pillows (on top)

    # 1. Headboard
    headboard_height = length * 0.08 # Proportionate height
    # Draw headboard slightly behind the mattress 'length'
    ax.add_patch(Rectangle(
        (x, y + length),                 # Positioned at the 'head' end of the bed
        width, headboard_height,
        facecolor=headboard_color, edgecolor='black', linewidth=0.8, zorder=3
    ))

    # 2. Mattress/Bed Base
    ax.add_patch(Rectangle(
        (x, y), width, length,
        facecolor=bed_base_color, edgecolor='black', linewidth=0.8, zorder=4
    ))

    # 3. Blanket/Duvet
    # Covers most of the bed, starting from the foot
    blanket_length = length * 0.7
    ax.add_patch(Rectangle(
        (x, y), width, blanket_length,
        facecolor=blanket_color, edgecolor='black', linewidth=0.5, zorder=5
    ))
    # Optional: Add a small fold line on the blanket
    fold_y = y + blanket_length - (length * 0.05)
    ax.add_line(Line2D([x + width * 0.2, x + width * 0.8], [fold_y, fold_y],
                       color='darkblue', linestyle='--', linewidth=0.8, alpha=0.6, zorder=5))


    # 4. Pillows (two pillows side-by-side)
    pillow_width = (width - 0.1) / 2 # Slightly smaller than half the bed width with a small gap
    pillow_length_actual = length * 0.15 # Actual length of a pillow
    pillow_y_pos = y + length - pillow_length_actual - 0.05 # Positioned near the headboard, slightly inwards

    ax.add_patch(Rectangle(
        (x + 0.05, pillow_y_pos), pillow_width, pillow_length_actual,
        facecolor=pillow_color, edgecolor='black', linewidth=0.5, zorder=6
    ))
    ax.add_patch(Rectangle(
        (x + pillow_width + 0.05, pillow_y_pos), pillow_width, pillow_length_actual,
        facecolor=pillow_color, edgecolor='black', linewidth=0.5, zorder=6
    ))

    # Optional: Bed label
    ax.text(x + width / 2, y + length / 2, bed_label,
            ha='center', va='center', fontsize=9, color='darkslategray', weight='bold', zorder=7)


def generate_bedroom_preset(
    room_width=4.0,       # Inner width of the room (e.g., meters)
    room_height=3.5,      # Inner height of the room
    wall_thickness=0.15,  # Thickness of the walls
    door_width=0.9,       # Width of the door
    window_width=1.5,     # Width of the window
    bed_type="queen",     # "twin", "full", "queen", "king"
    nightstand_size=0.5,  # Side of nightstand (square)
    wardrobe_width=1.8,   # Width of the wardrobe
    wardrobe_depth=0.6,   # Depth of the wardrobe
    furniture_color='peru',
    wall_color='lightgray',
    door_color='white',
    window_color='lightblue'
):
    """
    Generates a Matplotlib plot of a basic bedroom floor plan.
    Includes a more detailed bed.
    """

    fig, ax = plt.subplots(figsize=(10, 8))

    # Define bed dimensions based on type (approximate standard sizes in meters)
    bed_dims = {
        "twin": (0.99, 1.91),
        "full": (1.37, 1.91),
        "queen": (1.52, 2.03),
        "king": (1.93, 2.03)
    }
    if bed_type not in bed_dims:
        print(f"Warning: Bed type '{bed_type}' not recognized. Defaulting to 'queen'.")
        bed_width, bed_length = bed_dims["queen"]
    else:
        bed_width, bed_length = bed_dims[bed_type]

    # --- 1. Define Room Boundaries ---
    outer_width = room_width + 2 * wall_thickness
    outer_height = room_height + 2 * wall_thickness

    room_origin_x = 0
    room_origin_y = 0

    inner_room_x = room_origin_x + wall_thickness
    inner_room_y = room_origin_y + wall_thickness

    # --- 2. Draw Walls ---
    ax.add_patch(Rectangle(
        (room_origin_x, room_origin_y),
        outer_width, outer_height,
        facecolor=wall_color, edgecolor='black', linewidth=1
    ))
    ax.add_patch(Rectangle(
        (inner_room_x, inner_room_y),
        room_width, room_height,
        facecolor='white', edgecolor='black', linewidth=0, zorder=1
    ))

    # --- 3. Door ---
    '''
    Remove doors for now
    door_pos_x = inner_room_x + 0.5
    door_pos_y = room_origin_y

    ax.add_patch(Rectangle(
        (door_pos_x, door_pos_y),
        door_width, wall_thickness,
        facecolor=door_color, edgecolor=door_color, linewidth=0, zorder=2
    ))

    door_hinge_x = door_pos_x + door_width
    door_hinge_y = inner_room_y
    ax.add_line(Line2D(
        [door_hinge_x, door_hinge_x],
        [door_hinge_y, door_hinge_y + door_width],
        color='black', linewidth=1.5, zorder=3
    ))
    ax.add_patch(Arc(
        (door_hinge_x, door_hinge_y),
        2 * door_width, 2 * door_width,
        angle=0, theta1=90, theta2=180,
        color='black', linestyle=':', linewidth=0.8, zorder=3
    ))
'''
    # --- 4. Window ---
    window_pos_x = inner_room_x + (room_width - window_width) / 2
    window_pos_y = inner_room_y + room_height

    ax.add_patch(Rectangle(
        (window_pos_x, window_pos_y),
        window_width, wall_thickness,
        facecolor=window_color, edgecolor='black', linewidth=0.5, zorder=2
    ))
    ax.add_line(Line2D(
        [window_pos_x, window_pos_x + window_width],
        [window_pos_y + wall_thickness / 2, window_pos_y + wall_thickness / 2],
        color='black', linewidth=1, zorder=3
    ))

    # --- 5. Furniture ---
    # Bed: Placed against the top wall, centered
    bed_x = inner_room_x + (room_width - bed_width) / 2
    bed_y = inner_room_y + room_height - bed_length # Aligned with inner top wall
    draw_bed(ax, bed_x, bed_y, bed_width, bed_length, bed_label=f"{bed_type.capitalize()} Bed")

    # Nightstands: Next to the bed
    # Left nightstand
    ax.add_patch(Rectangle(
        (bed_x - nightstand_size - 0.1, bed_y + bed_length - nightstand_size),
        nightstand_size, nightstand_size,
        facecolor=furniture_color, edgecolor='black', linewidth=0.8, zorder=4
    ))
    # Right nightstand
    ax.add_patch(Rectangle(
        (bed_x + bed_width + 0.1, bed_y + bed_length - nightstand_size),
        nightstand_size, nightstand_size,
        facecolor=furniture_color, edgecolor='black', linewidth=0.8, zorder=4
    ))

    # Wardrobe: Placed on the right wall
    wardrobe_x = inner_room_x + room_width - wardrobe_depth
    wardrobe_y = inner_room_y + 0.5
    ax.add_patch(Rectangle(
        (wardrobe_x, wardrobe_y), wardrobe_depth, wardrobe_width,
        facecolor=furniture_color, edgecolor='black', linewidth=1, zorder=4
    ))
    ax.text(wardrobe_x + wardrobe_depth / 2, wardrobe_y + wardrobe_width / 2, "Wardrobe",
            rotation=90, ha='center', va='center', fontsize=9, color='white', weight='bold', zorder=5)

    # --- 6. Room Label ---
    ax.text(inner_room_x + room_width / 2, inner_room_y + room_height / 2,
            "BEDROOM", ha='center', va='center', fontsize=18, color='darkslategray', alpha=0.6)

    # --- 7. Plot Settings ---
    ax.set_aspect('equal', adjustable='box')
    ax.set_xlim(room_origin_x - 0.5, room_origin_x + outer_width + 0.5)
    ax.set_ylim(room_origin_y - 0.5, room_origin_y + outer_height + 0.5)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title(f"Bedroom Floor Plan Preset ({room_width:.1f}x{room_height:.1f}m)", fontsize=16)
    ax.grid(False)

    plt.show()

# --- Call the function to generate the plot with a detailed bed ---
generate_bedroom_preset(bed_type="queen")

# --- Example with a different bed type and room size ---
# generate_bedroom_preset(room_width=3.5, room_height=3.0, bed_type="full", furniture_color='saddlebrown')