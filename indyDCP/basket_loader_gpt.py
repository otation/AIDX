from indy_utils import indydcp_client as client
import time
from time import sleep

robot_ip = "192.168.3.7"  # Robot (Indy) IP
robot_name = "NRMK-Indy7"  # Robot name (Indy7)

indy = client.IndyDCPClient(robot_ip, robot_name)
sleep(1)
indy.connect()

# Basket zig offset
offset_x = 0.031
offset_y = 0.031
offset_z = 0.03  # Approach point distance

# Item positions with approach points
item_positions = {
    "circle": [
        [0.18590751100902442, 0.36718133245047757, 0.3536054851654807, -180, -23, 180],
        [0.18590751100902442, 0.36718133245047757, 0.3536054851654807 + offset_z, -180, -23, 180],
    ],
    "triangle": [
        [0.181386960075633, 0.5482425497483345, 0.3451090011717526, -180, -23, 180],
        [0.181386960075633, 0.5482425497483345, 0.3451090011717526 + offset_z, -180, -23, 180],
    ],
    "rectangle": [
        [0.22931479626152027, 0.5913640834751501, 0.3543532063254496, 170, -14, 180],
        [0.22931479626152027, 0.5913640834751501, 0.3543532063254496 + offset_z, 170, -14, 180],
    ],
}

# Basket 3x3 grid positions
pos_center = [0.5200724163809812, -0.13001499017914542, 0.3416199448926611, -180, 0, 180]
basket_3x3 = [
    [[pos_center[0] + j * offset_x, pos_center[1] + i * offset_y, pos_center[2], *pos_center[3:]],
     [pos_center[0] + j * offset_x, pos_center[1] + i * offset_y, pos_center[2] + offset_z, *pos_center[3:]]]
    for i in range(3) for j in range(3)
]

def move_done_check():
    while True:
        status = indy.get_robot_status()
        sleep(0.1)
        if status['movedone']:
            break

def gripper(hold):
    indy.set_do(2, hold)
    sleep(1)

def move_item_to_basket(item, basket_idx):
    indy.task_move_to(item[1])  # Move to approach point
    move_done_check()
    indy.task_move_to(item[0])  # Move to pick point
    move_done_check()
    gripper(True)  # Pick up item
    indy.task_move_to(item[1])  # Return to approach point
    move_done_check()

    # Move to basket
    indy.task_move_to(basket_3x3[basket_idx][1])  # Move to basket approach point
    move_done_check()
    indy.task_move_to(basket_3x3[basket_idx][0])  # Move to basket drop point
    move_done_check()
    gripper(False)  # Release item
    indy.task_move_to(basket_3x3[basket_idx][1])  # Return to basket approach point
    move_done_check()

def basket_load(load_plan):
    basket_idx = 0
    for item_name, cycles in load_plan.items():
        item = item_positions[item_name]
        for _ in range(cycles):
            move_item_to_basket(item, basket_idx)
            basket_idx += 1
    print("Robot A done loading")

# Define load plan
load_plan = {
    "circle": 2,
    "triangle": 2,
    "rectangle": 2,
}

# Execute loading sequence
basket_load(load_plan)
indy.disconnect()
