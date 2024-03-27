import matplotlib.pyplot as plt

# Define node information
nodes = [
    (1, "Headwater", (70, 100)),
    (42, "Junction", (100, 135)),
    (3, "Headwater", (120, 265)),
    (4, "Headwater", (120, 285)),
    (33, "Junction", (150, 185)),
    (34, "Junction", (185, 215)),
    (5, "Headwater", (195, 320)),
    (59, "Junction", (190,205)),
    (17, "Headwater", (225,295)),
    (35, "Junction", (220,185)),
    (18, "Headwater", (240,140)),
    (19, "Headwater", (330,185)),
    (2, "Junction", (230,190)),
    (36, "Junction", (270, 255)),
    (20, "Headwater", (330, 200)),
    (37, "Junction", (285, 270)),
    (16, "Headwater", (245, 335)),

    (39, "Junction", (320, 290)),
    (55, "Junction", (360, 250)),
    (25, "Headwater", (430, 230)),
    (56, "Junction", (365, 235)),
    (57, "Junction", (370, 220)),
    (58, " Junction", (380, 220)),
    (23, "Headwater", (430, 180)),
    (24, "Headwater", (460, 200)),
    (21, "Headwater", (340, 210)),
    (22, "Headwater", (365, 180)),
    (38, "Junction", (325, 335)),
    (41, "Junction", (295,360)),
    (40, "Junction", (255, 360)),

    (6, "Headwater", (225, 370)),
    (7, "Headwater", (235, 420)),
    (43, "Junction", (355, 385)),
    (8, "Headwater", (260, 465)),
    (9, "Headwater", (315, 460)),
    (49, "Junction", (350, 345)),

    (48, "Junction", (355, 360)),
    (14, "Headwater", (360, 410)),
    (15, "Headwater", (385, 385)),
    (46, "Junction", (380, 360)),
    (45, "Junction", (450, 380)),
    (29, "Junction", (520, 275)),
    (47, "Junction", (415, 445)),
    (13, "Headwater", (380, 370)),
    (44, "Junction", (400, 450)),
    (10, "Headwater", (325, 500)),
    (11, "Headwater", (345, 490)),
    (12, "Headwater", (355, 515)),
    (50, "Junction", (430, 295)),
    (51, "Junction", (435, 280)),
    (27, "Headwater", (425, 260)),
    (28, "Headwater", (410, 275)),
    (52, "Junction", (450, 275)),
    (26, "Headwater", (440, 200)),
    (53, "Junction", (500, 245)),

    (30, "Headwater", (580, 210)),
    (54, "Junction", (540, 155)),
    (31, "Headwater", (560, 120)),
    (32, "Headwater", (580, 90)),
]

edges = [
    (1, 42),
    (42,3),
    (42, 33),
    (33, 34), 
    (33,4),
    (34, 5),
    (34, 59),
    (59, 35),
    (35, 18),
    (35, 2),
    (2, 19),
    (59, 17),
    (2, 36),
    (36, 20),
    (36, 37),
    (37, 16),
    (37, 39),
    (39, 55),
    (39, 38),
    (38, 41),
    (41, 40),
    (40, 6),
    (40, 7),
    (41, 43),
    (43, 8),
    (43, 9),
    (55, 25),
    (55, 56),
    (56, 57),
    (57, 21),
    (56, 58),
    (58, 23),
    (58, 24),
    (38, 49),
    (49, 15),
    (49, 48),
    (48, 14),
    (49, 46),
    (46, 45),
    (45, 29),
    (45, 47),
    (47, 44),
    (47, 13),
    (44, 10),
    (44, 11),
    (44, 12),
    (46, 50),
    (50, 51),
    (51, 28),
    (51, 27),
    (50, 52),
    (52, 26),
    (52, 53),
    (53, 30),
    (53, 54),
    (54, 31),
    (54, 32)
]

# Create the tree plot
plt.figure(figsize=(10, 8))
for parent, child in edges:
    parent_coords = next(coords for id, label, coords in nodes if id == parent)
    child_coords = next(coords for id, label, coords in nodes if id == child)
    plt.plot([parent_coords[0], child_coords[0]], [parent_coords[1], child_coords[1]], '-k')
    
for id, label, (x, y) in nodes:
    plt.text(x, y, f"{id} - {label}", ha='center', va='center', bbox=dict(facecolor='white', edgecolor='black', alpha=0.8))

plt.xlabel('X Coordinate')
plt.ylabel('Y Coordinate')
plt.title('Tree Plot')
plt.gca().invert_yaxis()  # Invert y-axis to match typical coordinate plane
plt.show()