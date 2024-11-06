def move_done_check():
    while True:
        status = indy.get_robot_status()
        sleep(0.1)
        if status['movedone'] == True:
            break

def gripper(hold):
    if hold == True:
        indy.set_do(2, True)
        sleep(1)
    elif hold == False:
        indy.set_do(2, False)
        sleep(1)

x_offset = 0.04  # [0] approach
y_offset = 0.04  # [1] target
z_offset = 0.05  # [2] retract
x, y, z = 0, 1, 2

## 5x5 가운데 기준 점 위치
t_pos_temp = [0.18901400774475438, 0.3223276396160324, 0.4106097948240943, -179.8172622630945, -0.03276487114401588, 179.9678431551056]

#슬라이딩 픽업 위치
pick_approach = [0.23745875175855685, 0.5506905556669043, 0.4901385014094857, -179.11780315213286, -22.27065953394359, 179.62075790729745]
pick_target = [0.1806150185683212, 0.5487788854724143, 0.35145679815967396, -179.13138416191956, -22.266422303371044, 179.62579798257372]
pick_retract = [0.23745875175855685, 0.5506905556669043, 0.4901385014094857, -179.11780315213286, -22.27065953394359, 179.62075790729745]

pos = [[t_pos_temp.copy(), t_pos_temp.copy(), t_pos_temp.copy()] for _ in range(25)]

indy.connect()

# y값 보정 함수
def adjust_y(stage, multiplier):
    for i in range(0, 25):
        pos[i][stage][y] += y_offset * multiplier[i // 5]

# x값 보정 함수
def adjust_x(stage, multipliers):
    for i in range(0, 25):
        pos[i][stage][x] += x_offset * multipliers[i % 5]

# 각 stage에 대한 y 보정
y_multipliers = [2, 1, 0, -1, -2]
adjust_y(1, y_multipliers)  # target stage
adjust_y(0, y_multipliers)  # approach stage
adjust_y(2, y_multipliers)  # retract stage

# 각 stage에 대한 x 보정
x_multipliers = [2, 1, 0, -1, -2]
adjust_x(1, x_multipliers)  # target stage
adjust_x(0, x_multipliers)  # approach stage
adjust_x(2, x_multipliers)  # retract stage

# z값 보정 (approach, retract 단계에만 적용)
for i in range(25):
    pos[i][0][z] += z_offset  # approach
    pos[i][2][z] += z_offset  # retract

##동작 기동---------------------------

# 입력할 숫자의 개수
n = int(input("How many item do you want to move? : "))

place_info_org = []

for i in range(n):
    number = int(input(f"Input location btw 1-25| {i+1}th: "))
    place_info_org.append(number)

place_info = [x - 1 for x in place_info_org]

for i in range(len(place_info)):
    indy.task_move_to(pick_approach)
    move_done_check()
    indy.task_move_to(pick_target)
    move_done_check()
    gripper(1)
    indy.task_move_to(pick_retract)
    move_done_check()
    
    indy.task_move_to(pos[place_info[i]][0])
    move_done_check()
    indy.task_move_to(pos[place_info[i]][1])
    move_done_check()
    gripper(0)
    indy.task_move_to(pos[place_info[i]][2])
    move_done_check()

indy.task_move_to(pos[12][2])
move_done_check()

indy.disconnect()
