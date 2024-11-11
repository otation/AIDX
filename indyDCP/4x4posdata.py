import time

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

## 4x4 기준 점 위치
t_pos_temp = [0.13140896924009746, 0.26421167742081064, 0.4228369730241361, -179.94721095038545, -0.011815043020984132, 179.9355572019889]

#슬라이딩 픽업 위치
pick_approach = [0.23745875175855685, 0.5506905556669043, 0.4901385014094857, -179.11780315213286, -22.27065953394359, 179.62075790729745]
pick_target = [0.1806150185683212, 0.5487788854724143, 0.35145679815967396, -179.13138416191956, -22.266422303371044, 179.62579798257372]
pick_retract = [0.23745875175855685, 0.5506905556669043, 0.4901385014094857, -179.11780315213286, -22.27065953394359, 179.62075790729745]

#슬라이딩 회수 위치
re_turn = [-0.1166314284076608, 0.538785634811134, 0.46757881208606117, 1.1001765324683144, -173.53101937588497, 0.4158159489321837]
re_turn_z = [-0.11598340351921843, 0.5390585981908083, 0.5248272821930534, 0.995244409254611, -177.28337387684957, 0.4364495258757762]

pos = [[t_pos_temp.copy(), t_pos_temp.copy(), t_pos_temp.copy()] for _ in range(16)]

# y값 보정 함수
def adjust_y(stage, multiplier):
    for i in range(0, 16):
        pos[i][stage][y] += y_offset * multiplier[i // 4]

# x값 보정 함수
def adjust_x(stage, multipliers):
    for i in range(0, 16):
        pos[i][stage][x] += x_offset * multipliers[i % 4]

# 각 stage에 대한 y 보정
y_multipliers = [0, 1, 2, 3]
adjust_y(1, y_multipliers)  # target stage
adjust_y(0, y_multipliers)  # approach stage
adjust_y(2, y_multipliers)  # retract stage

# 각 stage에 대한 x 보정
x_multipliers = [0, 1, 2, 3]
adjust_x(1, x_multipliers)  # target stage
adjust_x(0, x_multipliers)  # approach stage
adjust_x(2, x_multipliers)  # retract stage

# z값 보정 (approach, retract 단계에만 적용)
for i in range(16):
    pos[i][0][z] += z_offset  # approach
    pos[i][2][z] += z_offset  # retract

#슬라이딩 아래서 공급
def acheive():
    indy.task_move_to(pick_approach)
    move_done_check()
    indy.task_move_to(pick_target)
    move_done_check()
    gripper(1)
    indy.task_move_to(pick_retract)
    move_done_check()

#슬라이딩 위로 회수
def re_turn_job():
    indy.task_move_to(re_turn_z)
    move_done_check()
    indy.task_move_to(re_turn)
    move_done_check()
    gripper(0)
    indy.task_move_to(re_turn_z)
    move_done_check() 

def init_queue(size=4):
    """Queue 초기화."""
    return [[0, 0.0, 0.0] for _ in range(size)]  # [활성화 상태, 경과 시간, 시작 시간]

def append_queue(queue):
    """Queue에 태스크 추가."""
    for i in range(len(queue)):
        if queue[i][0] == 0:  # 비어 있는 슬롯 찾기
            queue[i][0] = 1  # 활성화 상태로 변경
            queue[i][2] = time.time()  # 등록 시간 기록
            print(f"슬롯 {i}에 태스크 추가됨.")
            break
    else:
        print("Queue가 가득 찼습니다. 추가 불가!")
    return queue

def update_queue(queue, robot_position, return_position):
    """Queue를 업데이트하고, 20초 이상 대기 중인 태스크를 반환."""
    for i in range(len(queue)):
        if queue[i][0] != 0:  # 활성화된 태스크만 처리
            elapsed_time = time.time() - queue[i][2]
            queue[i][1] = elapsed_time
            if elapsed_time >= 20:
                print(f"슬롯 {i}의 태스크가 20초를 초과했습니다. 반환합니다.")
                robot_move(robot_position, return_position)  # 반환 동작
                queue[i] = [0, 0.0, 0.0]  # 슬롯 초기화
    return queue

def auto_queue_process(queue, size=4):
    """Queue 기반으로 자동 작업 처리."""
    while True:
        for i in range(size):
            if queue[i][0] == 1:  # 활성화된 작업
                elapsed_time = time.time() - queue[i][2]
                if elapsed_time >= 20:
                    print(f"슬롯 {i}의 아이템 20초 초과: 반환 처리 시작.")
                    
                    indy.task_move_to(pos[i][0])
                    move_done_check()
                    indy.task_move_to(pos[i][1])
                    move_done_check()
                    gripper(1)
                    indy.task_move_to(pos[i][2])
                    move_done_check()
                    re_turn_job()
                    queue[i] = [0, 0.0, 0.0]  # 작업 초기화
                else:
                    print(f"슬롯 {i} 작업 중: 경과 시간 {elapsed_time:.2f}초")
                    
            elif queue[i][0] == 0:  # 비어 있는 작업
                acheive()
                indy.task_move_to(pos[i][0])
                move_done_check()
                indy.task_move_to(pos[i][1])
                move_done_check()
                gripper(0)
                indy.task_move_to(pos[i][2])
                move_done_check()
                queue[i][0] = 1
                queue[i][2] = time.time()  # 등록 시간 기록
                print(f"슬롯 {i}에 새로운 작업 추가.")
            
##동작 기동---------------------------
indy.connect()

mode = 0
mode = int(input("mode를 입력하세요. 0: 직접입력, 1: csv입력, 3:자동 Queue 할당 :"))

if mode == 3:
    queue = init_queue(size=4)
    auto_queue_process(queue, size=4)
    

# 입력할 숫자의 개수
if mode == 0:

    n = int(input("How many item do you want to move? : "))
    
    place_info_org = []
    
    for i in range(n):
        number = int(input(f"Input location btw 1-25| {i+1}th: "))
        place_info_org.append(number)
    
    place_info = [x - 1 for x in place_info_org]
    
    for i in range(len(place_info)):
        acheive()
        
        indy.task_move_to(pos[place_info[i]][0])
        move_done_check()
        indy.task_move_to(pos[place_info[i]][1])
        move_done_check()
        gripper(0)
        indy.task_move_to(pos[place_info[i]][2])
        move_done_check()

    re_turn_job()

if mode == 1:
    file_path = 'output.csv'
    
    df = pd.read_csv(file_path, encoding='CP949', sep='\t')
    
    for i in range(len(df)):
        achieve()
        
        indy.task_move_to(pos[df['0'][i]][0])
        move_done_check()
        indy.task_move_to(pos[df['0'][i]][1])
        move_done_check()
        gripper(0)
        indy.task_move_to(pos[df['0'][i]][2])
        move_done_check()

    re_turn_job()

indy.go_home()
move_done_check()

indy.disconnect()
