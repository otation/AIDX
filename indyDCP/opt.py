x_offset = 0.04  # [0] approach
y_offset = 0.04  # [1] target
z_offset = 0.02  # [2] retract
x, y, z = 0, 1, 2

# 초기 위치 설정
t_pos_temp = [0.18901400774475438, 0.3223276396160324, 0.4106097948240943, -179.8172622630945, -0.03276487114401588, 179.9678431551056]
pos = [[t_pos_temp.copy(), t_pos_temp.copy(), t_pos_temp.copy()] for _ in range(25)]

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

print(pos)
