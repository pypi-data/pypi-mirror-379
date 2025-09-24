import time
import serial
import serial.tools.list_ports
import os
import threading
import queue
import math
import cv2

#-------------------------------MODULE EXPORTS---------------------------------------------------------------------------------------------

__all__ = ['move', 'light','light12', 'playSound', 'wait', 'listAvailableSounds','moveStop','wait_sensor','resistance_to_stop','face_smile_detection',
           'lightStop','soundStop','rotations','get_sensor_value','FOREVER', 'algopython_init', 'algopython_exit','start_task','play_btn_pressed']

#-------------------------------GLOBAL VARIABLES---------------------------------------------------------------------------------------------
global ser;
serial_lock = threading.Lock()
serial_command_queue = queue.Queue()
serial_worker_running = False
status_thread = None
serial_thread = None
status_thread_running = False

move_cancel_flag = threading.Event()
rotations_cancel_flag = threading.Event()
led1_cancel_flag = threading.Event()
led2_cancel_flag = threading.Event()
led12_cancel_flag = threading.Event()
sound_cancel_flag = threading.Event()
sound_lock = threading.Lock()

_task_threads = []

FOREVER = math.inf

SOUNDS_MAP = {
        1: "SIREN",
        2: "BELL",
        3: "BIRD",
        4: "BEAT",
        5: "DOG",
        6: "MONKEY",
        7: "ELEPHANT",
        8: "APPLAUSE",
        9: "VIOLINE",
        10: "GUITAR",
        11: "ROBOT_LIFT",
        12: "TRUCK",
        13: "SMASH",
        14: "CLOWN",
        15: "CHEERING"
    }

MOTOR_MAP = {
    'A': 0b001,
    'B': 0b010,
    'C': 0b100,
    'AB': 0b011,
    'AC': 0b101,
    'BC': 0b110,
    'ABC': 0b111
}

ROTATIONS_TO_SECONDS_MAP = {
    'A': 0.63,
    'B': 0.63,
    'C': 0.63,
    'AB': 0.68,
    'ABC' : 0.68,
    'AC': 0.68,
    'BC': 0.68
}

COLOR_MAP = {
    "red":     (255, 0, 0),
    "green":   (0, 255, 0),
    "blue":    (0, 0, 255),
    "yellow":  (255, 255, 0),
    "cyan":    (0, 255, 255),
    "magenta": (255, 0, 255),
    "white":   (255, 255, 255),
    "purple":  (128, 0, 128),
}

#-------------------------------SERIAL COMMANDS---------------------------------------------------------------------------------------------
ALGOPYTHON_CMD_MOVE_REQ         =0x10
ALGOPYTHON_CMD_LIGHT_REQ        =0x11
ALGOPYTHON_CMD_PLAY_SOUND_REQ   =0x12
ALGOPYTHON_CMD_MOVE_STOP_REQ    =0x13
ALGOPYTHON_CMD_LIGHT_STOP_REQ   =0x14
ALGOPYTHON_CMD_SOUND_STOP_REQ   =0x15
ALGOPYTHON_CMD_LIGHT12_REQ      =0x16 
ALGOPYTHON_CMD_WAIT_SENSOR_REQ  =0x17
ALGOPYTHON_CMD_GET_SENSOR_REQ   =0x18
ALGOPYTHON_CMD_GET_STATUS_REQ   =0x19
ALGOPYTHON_CMD_ROTATIONS_REQ    =0x20
ALGOPYTHON_CMD_RESISTANCE_REQ   =0x21

ALGOPYTHON_CMD_MOVE_REP         =0x80
ALGOPYTHON_CMD_LIGHT_REP        =0x81
ALGOPYTHON_CMD_PLAY_SOUND_REP   =0x82
ALGOPYTHON_CMD_MOVE_STOP_REP    =0x83
ALGOPYTHON_CMD_LIGHT_STOP_REP   =0x84
ALGOPYTHON_CMD_LIGHT12_REP      =0x86 
ALGOPYTHON_CMD_WAIT_SENSOR_REP  =0x87
ALGOPYTHON_CMD_GET_SENSOR_REP   =0x88
ALGOPYTHON_CMD_GET_STATUS_REP   =0x89
ALGOPYTHON_CMD_ROTATIONS_REP    =0x90
ALGOPYTHON_CMD_RESISTANCE_REP   =0x91

CMD_REPLY_MAP = {
    0x10: 0x80,  # MOVE_REQ         -> MOVE_REP
    0x11: 0x81,  # LIGHT_REQ        -> LIGHT_REP
    0x12: 0x82,  # PLAY_SOUND_REQ   -> PLAY_SOUND_REP
    0x13: 0x83,  # MOVE_STOP_REQ    -> MOVE_STOP_REP
    0x14: 0x84,  # LIGHT_STOP_REQ   -> LIGHT_STOP_REP
    0x15: 0x85,  # SOUND_STOP_REQ   -> SOUND_STOP_REP 
    0x16: 0x86,  # LIGHT12_REQ      -> LIGHT12_REP 
    0x17: 0x87,  # WAIT_SENSOR_REQ  -> WAIT_SENSOR_REP
    0x18: 0x88,  # GET_SENSOR_REQ   -> GET_SENSOR_REP
    0x19: 0x89,  # GET_STATUS_REQ   -> GET_STATUS_REP
    0x20: 0x90,  # ROTATIONS_REQ    -> ROTATIONS_REP
    0x21: 0x91   # RESISTANCE_REQ   -> RESISTANCE_REP
}
#-------------------------------SERIAL COMMUNICATION AND PROTOCOL-----------------------------------------------
class SerialCommand:
    def __init__(self, cmd, payload, expect_reply=True):
        self.cmd = cmd
        self.payload = payload
        self.expect_reply = expect_reply
        self.response = None
        self.done = threading.Event()

def stop_status_monitor():
    global status_thread_running
    status_thread_running = False
    print("Status monitor stopped.")

class DeviceStatus:
    def __init__(self):
        # Motors
        self.motor1 = False 
        self.motor_reason1 = 0;
        self.motor2 = False 
        self.motor_reason2 = 0;
        self.motor3 = False 
        self.motor_reason3 = 0;

        # LEDs
        self.led1 = False
        self.led2 = False

        # Sound
        self.sound = False

        # Sensors (state and values)
        self.sensor1 = False
        self.sensor2 = False
        self.sensor1_value = 0.0
        self.sensor2_value = 0.0

        #playBtn
        self.play_btn = False

g_algopython_system_status = DeviceStatus()

def serial_thread_task():
    global status_thread_running
    last_status_time = time.time()
    while status_thread_running:
        now = time.time()
        try:
            # poll status every 50 ms
            if (now - last_status_time) >= 0.05:
                serial_get_brain_status()
                last_status_time = now

            try:
                command = serial_command_queue.get_nowait()
                serial_send_command(command)
            except queue.Empty:
                pass

        except (serial.SerialException, ValueError, OSError) as e:
            print(f"[Serial Thread Error] {e}")
            break

        time.sleep(0.001)  # prevent CPU hogging

def serial_thread_start():
    global status_thread_running,serial_thread
    status_thread_running = True
    serial_thread = threading.Thread(target=serial_thread_task, daemon=True)
    serial_thread.start()

def serial_send_next_command(command):
    result = send_packet(
            command.cmd,
            command.payload,
            wait_done=command.expect_reply,
            verbose=True
            )
    command.response = result
    command.done.set()

def start_task(task_func,*args, **kwargs):
    t = threading.Thread(target=task_func, args=args, kwargs=kwargs, daemon=True)
    _task_threads.append(t)
    t.start()
  
    return t

def serial_get_brain_status():
    global g_algopython_system_status
    response = serial_send_command(0x19, b"", expect_reply=True)

    if not response or len(response) < 10:
        return "?, ?, ?, ?, ?, ?, ?, ?, ?, ?"

    g_algopython_system_status.motor1 = response[0] & 0x0F
    g_algopython_system_status.motor_reason1 = (response[0] >> 4) & 0x0F
    g_algopython_system_status.motor2 = response[1] & 0x0F
    g_algopython_system_status.motor_reason2 = (response[1] >> 4) & 0x0F
    g_algopython_system_status.motor3 = response[2] & 0x0F
    g_algopython_system_status.motor_reason3 = (response[2] >> 4) & 0x0F
    g_algopython_system_status.led1 = bool(response[3])
    g_algopython_system_status.led2 = bool(response[4])
    g_algopython_system_status.sound = bool(response[5])
    g_algopython_system_status.sensor1 = bool(response[6])
    g_algopython_system_status.sensor2 = bool(response[7])
    g_algopython_system_status.sensor1_value = response[8]
    g_algopython_system_status.sensor2_value = response[9]
    g_algopython_system_status.play_btn = bool(response[10])

    s = g_algopython_system_status
    
    # print(
    #     f"Motors: {s.motor1}, {s.motor2}, {s.motor3} | "
    #     f"Reasons: {s.motor_reason1}, {s.motor_reason2}, {s.motor_reason3} | "
    #     f"LEDs: {int(s.led1)}, {int(s.led2)} | "
    #     f"Sound: {int(s.sound)} | "
    #     f"Sensors: Trig1={int(s.sensor1)}, Trig2={int(s.sensor2)}, "
    #     f"Value1={s.sensor1_value}, Value2={s.sensor2_value}"
    #     f" | PlayBtn: {int(s.play_btn)}"
    # )

def serial_send_command(cmd, payload, expect_reply=True):
    command = SerialCommand(cmd, payload, expect_reply)
    serial_tx_command(command)
    command.done.wait(timeout = 2.0)
    if not command.done.is_set():
        print(f"[Error] Command 0x{cmd:02X} timed out.")
    return command.response

def serial_tx_command(command):
    result = send_packet(
            command.cmd,
            command.payload,
            wait_done=command.expect_reply,
            verbose=True
            )
    command.response = result
    command.done.set()

def find_usb_serial_port():
    ports = serial.tools.list_ports.comports()
    for p in ports:
        if "USB" in p.description or "CH340" in p.description or "ttyUSB" in p.device:
            return p.device
    return None

def build_packet(cmd: int, payload: bytes) -> bytes:
    if not isinstance(payload, (bytes, bytearray)):
        payload = bytes(payload)
    header = bytes([0xA5, cmd, len(payload)])
    crc = sum(header) % 256
    return header + payload + bytes([crc])

def send_packet(cmd, payload, wait_done=True, delay_after=0.01, retries=2, verbose=True):
    global ser
    if ser is None:
        print("[Error] Serial port is not initialized.")
        return None

    packet = build_packet(cmd, payload)
    expected_reply_cmd = CMD_REPLY_MAP.get(cmd)
    # print(f"Sending packet: {packet.hex()} (CMD: 0x{cmd:02X}, Expected Reply: 0x{expected_reply_cmd:02X})")
    for attempt in range(retries + 1):
        with serial_lock:
            ser.reset_input_buffer()
            # if verbose:
            #     print(f"\n[Try {attempt + 1}] Sending packet: " + ' '.join(f'{b:02X}' for b in packet))
            ser.write(packet)
            time.sleep(delay_after)
            # if wait_done:
            if True:
                reply = wait_for_reply(expected_reply_cmd)
                if reply is not None:
                    return reply
            else:
                return True
    if verbose:
        print(f"[Fail] No reply for CMD 0x{cmd:02X} after {retries + 1} tries.")
    return None

def wait_for_reply(expected_cmd, timeout=1):
    global ser
    start = time.time()
    buffer = bytearray()
    #print(f"Waiting for reply for CMD 0x{expected_cmd:02X}...")
    while time.time() - start < timeout:
        if ser.in_waiting:
            # print("Serianl in waiting: ", ser.in_waiting);
            buffer.extend(ser.read(ser.in_waiting))
        while len(buffer) >= 4:
            # print("Buffer length: ", len(buffer))
            # print("Buffer content: ", buffer.hex())
            if buffer[0] == 0xA5:
                cmd, size = buffer[1], buffer[2]
                total_length = 3 + size + 1
                if len(buffer) >= total_length:
                    crc = buffer[3 + size]
                    # print("CRC: ", crc, "Expected: ", (sum(buffer[:total_length - 1])&0xff) )
                    if cmd == expected_cmd and crc == sum(buffer[:total_length - 1])&0xff:
                        return buffer[3:3+size]
                    buffer = buffer[1:]
                else:
                    break
            else:
                buffer = buffer[1:]
        time.sleep(0.005)
    return None

def algopython_init(port: str = None):
    time.sleep(2) # Allow time for the system to start up and establish the serial connection
    os.system('cls' if os.name == 'nt' else 'clear')
    global ser, status_thread_running
    if not port:
        port = find_usb_serial_port()
        if not port:
            print("USB port not found. Please connect the device and try again.")
            return False
    try:
        ser = serial.Serial(port,115200)
        ser.bytesize = serial.EIGHTBITS #number of bits per bytes
        ser.parity = serial.PARITY_NONE #set parity check: no parity
        ser.stopbits = serial.STOPBITS_ONE #number of stop bits
        ser.xonxoff = False     #disable software flow control
        ser.rtscts = False     #disable hardware (RTS/CTS) flow control
        ser.dsrdtr = False       #disable hardware (DSR/DTR) flow control
        ser.timeout = None          #block read

        if ser.isOpen():
            print("USB ready...")
            time.sleep(2)
            ser.flush()
        else:
            exit() 
        status_thread_running = True
        serial_thread_start()
        time.sleep(2)
        return True
    except serial.SerialException as e:
        print(f"\nError when opening port: {port}: {e}\n")
        return False

def algopython_exit():
    global ser, status_thread_running,serial_thread
    
    for t in _task_threads:
        t.join()
    _task_threads.clear()
    status_thread_running = False
    if serial_thread and serial_thread.is_alive():
        serial_thread.join(timeout=1.0)
        print("Serial thread joined.")
    try:
        if ser and ser.is_open:
            ser.close()
            print("Serial port closed.")
    except Exception as e:
        print(f"Error closing serial port: {e}")
    print("Algopython exited.")

# --------------------------------------------------------------------------------------------------------------
#-----------------Move section----------------------------------------------------------------------------------

def move(port: str, duration: float, power: int, direction: str | int, is_blocking=True):
    global move_cancel_flag

    move_cancel_flag.set()
    move_cancel_flag = threading.Event()

    if port not in MOTOR_MAP:
        raise ValueError("Invalid motor")
    if duration < 0 or duration > 10:   
        raise ValueError("Duration must be between 0 and 10 seconds")
    if not (0 <= power <= 10):
        raise ValueError("Power must be 0-10")

    if direction == 'CW':
        motor_direction = 1
    elif direction == "CCW":
        motor_direction = -1
    else:
        motor_direction = direction

    motor_port = MOTOR_MAP[port.upper()]
    motor_power = int((power * 255) / 10)
    motor_type = 0

    if math.isinf(duration):
        print("x is positive infinity")
        motor_type = 1
        motor_duration = 0
        is_blocking = False
    else:
        motor_duration = int(duration * 100)

    payload = bytearray([
        motor_port & 0xFF,
        motor_type & 0xFF,
        (motor_duration >> 24) & 0xFF,
        (motor_duration >> 16) & 0xFF,
        (motor_duration >> 8) & 0xFF,
        (motor_duration) & 0xFF,
        motor_power & 0xFF,
        motor_direction & 0xFF
    ])

    send_packet(ALGOPYTHON_CMD_MOVE_REQ, payload, wait_done=False)
    # print("Wait for motor to finish...")

    if not is_blocking:
        return

    if motor_port == 0b001: 
        motor_prev_status = g_algopython_system_status.motor1
        while True:
            if move_cancel_flag.is_set():
                print("MotorA cancelled")
                break
            if (motor_prev_status == 1) and (g_algopython_system_status.motor1 == 0):
                print("MotorA completed movement")
                break
            motor_prev_status = g_algopython_system_status.motor1
            time.sleep(0.05)

    elif motor_port == 0b010: 
        motor_prev_status = g_algopython_system_status.motor2
        while True:
            if move_cancel_flag.is_set():
                print("MotorB cancelled")
                break
            if (motor_prev_status == 1) and (g_algopython_system_status.motor2 == 0):
                print("MotorB completed movement")
                break
            motor_prev_status = g_algopython_system_status.motor2
            time.sleep(0.05)

    elif motor_port == 0b100: 
        motor_prev_status = g_algopython_system_status.motor3
        while True:
            if move_cancel_flag.is_set():
                print("MotorC cancelled")
                break
            if (motor_prev_status == 1) and (g_algopython_system_status.motor3 == 0):
                print("MotorC completed movement")
                break
            motor_prev_status = g_algopython_system_status.motor3
            time.sleep(0.05)

    elif motor_port == 0b011:  
        motorA_prev_status = g_algopython_system_status.motor1
        motorB_prev_status = g_algopython_system_status.motor2
        exit_flag = 0
        while True:
            if move_cancel_flag.is_set():
                print("Motors AB cancelled")
                break
            if ((motorA_prev_status == 1)  and (motorA_prev_status != g_algopython_system_status.motor1)):
                exit_flag = exit_flag | 0x01
            if ((motorB_prev_status == 1)  and (motorB_prev_status != g_algopython_system_status.motor2)):
                exit_flag = exit_flag | 0x02
            if exit_flag == 0x03:
                print("Motors AB completed movement")
                break
            motorA_prev_status = g_algopython_system_status.motor1
            motorB_prev_status = g_algopython_system_status.motor2
            time.sleep(0.05)

    elif motor_port == 0b101:  
        motorA_prev_status = g_algopython_system_status.motor1
        motorC_prev_status = g_algopython_system_status.motor3
        exit_flag = 0
        while True:
            if move_cancel_flag.is_set():
                print("Motors AC cancelled")
                break
            if ((motorA_prev_status == 1)  and (motorA_prev_status != g_algopython_system_status.motor1)):
                exit_flag = exit_flag | 0x01
            if ((motorC_prev_status == 1)  and (motorC_prev_status != g_algopython_system_status.motor2)):
                exit_flag = exit_flag | 0x02
            if exit_flag == 0x03:
                print("Motors AC completed movement")
                break
            motorA_prev_status = g_algopython_system_status.motor1
            motorC_prev_status = g_algopython_system_status.motor3
            time.sleep(0.05)

    elif motor_port == 0b110:  
        motorB_prev_status = g_algopython_system_status.motor2
        motorC_prev_status = g_algopython_system_status.motor3
        exit_flag = 0
        while True:
            if move_cancel_flag.is_set():
                print("Motors BC cancelled")
                break
            if ((motorB_prev_status == 1)  and (motorB_prev_status != g_algopython_system_status.motor2)):
                exit_flag = exit_flag | 0x01
            if ((motorC_prev_status == 1)  and (motorC_prev_status != g_algopython_system_status.motor3)):
                exit_flag = exit_flag | 0x02
            if exit_flag == 0x03:
                print("Motors BC completed movement")
                break
            motorB_prev_status = g_algopython_system_status.motor2
            motorC_prev_status = g_algopython_system_status.motor3
            time.sleep(0.05)

    elif motor_port == 0b111:
        motorA_prev_status = g_algopython_system_status.motor1
        motorB_prev_status = g_algopython_system_status.motor2
        motorC_prev_status = g_algopython_system_status.motor3
        exit_flag = 0
        while True:
            if move_cancel_flag.is_set():
                print("Motors ABC cancelled")
                break
            if ((motorA_prev_status == 1)  and (motorA_prev_status != g_algopython_system_status.motor1)):
                exit_flag = exit_flag | 0x01
            if ((motorB_prev_status == 1)  and (motorB_prev_status != g_algopython_system_status.motor2)):
                exit_flag = exit_flag | 0x02
            if ((motorC_prev_status == 1)  and (motorC_prev_status != g_algopython_system_status.motor3)):
                exit_flag = exit_flag | 0x04
            if exit_flag == 0x07:
                print("Motors ABC completed movement")
                break
            motorA_prev_status = g_algopython_system_status.motor1
            motorB_prev_status = g_algopython_system_status.motor2
            motorC_prev_status = g_algopython_system_status.motor3
            time.sleep(0.05)

# --------------------------------------------------------------------------------------------------------------
#-----------------Rotations section-----------------------------------------------------------------------------

def rotations(port: str, rotations: float, power: int, direction: int):
    global rotations_cancel_flag

    rotations_cancel_flag.set()
    rotations_cancel_flag = threading.Event()

    if port not in MOTOR_MAP:
        raise ValueError("Invalid motor")
    if rotations < 0 or rotations > 100:  # fixed 'and' -> 'or'
        raise ValueError("Rotations must be between 0 and 100")
    if not (0 <= power <= 10):
        raise ValueError("Power must be 0-10")
    if direction not in (1, -1):
        raise ValueError("Direction must be 1 (CW) or -1 (CCW)")

    motor_port = MOTOR_MAP[port.upper()]
    motor_power = int((power * 255) / 10)
    motor_rotations_val = int(rotations * 100)
    motor_direction = direction

    payload = bytearray([
        motor_port & 0xFF,
        (motor_rotations_val >> 24) & 0xFF,
        (motor_rotations_val >> 16) & 0xFF,
        (motor_rotations_val >> 8) & 0xFF,
        (motor_rotations_val) & 0xFF,
        motor_power & 0xFF,
        motor_direction & 0xFF
    ])

    send_packet(ALGOPYTHON_CMD_ROTATIONS_REQ, payload, wait_done=False)
    # print("Wait for motor rotations to finish...")

    if motor_port == 0b001: 
        motor_prev_status = g_algopython_system_status.motor1
        while True:
            if move_cancel_flag.is_set():
                print("MotorA cancelled")
                break
            if (motor_prev_status == 1) and (g_algopython_system_status.motor1 == 0):
                print("MotorA completed movement")
                break
            motor_prev_status = g_algopython_system_status.motor1
            time.sleep(0.05)

    elif motor_port == 0b010: 
        motor_prev_status = g_algopython_system_status.motor2
        while True:
            if move_cancel_flag.is_set():
                print("MotorB cancelled")
                break
            if (motor_prev_status == 1) and (g_algopython_system_status.motor2 == 0):
                print("MotorB completed movement")
                break
            motor_prev_status = g_algopython_system_status.motor2
            time.sleep(0.05)

    elif motor_port == 0b100: 
        motor_prev_status = g_algopython_system_status.motor3
        while True:
            if move_cancel_flag.is_set():
                print("MotorC cancelled")
                break
            if (motor_prev_status == 1) and (g_algopython_system_status.motor3 == 0):
                print("MotorC completed movement")
                break
            motor_prev_status = g_algopython_system_status.motor3
            time.sleep(0.05)

    elif motor_port == 0b011:  
        motorA_prev_status = g_algopython_system_status.motor1
        motorB_prev_status = g_algopython_system_status.motor2
        exit_flag = 0
        while True:
            if move_cancel_flag.is_set():
                print("Motors AB cancelled")
                break
            if ((motorA_prev_status == 1)  and (motorA_prev_status != g_algopython_system_status.motor1)):
                exit_flag = exit_flag | 0x01
            if ((motorB_prev_status == 1)  and (motorB_prev_status != g_algopython_system_status.motor2)):
                exit_flag = exit_flag | 0x02
            if exit_flag == 0x03:
                print("Motors AB completed movement")
                break
            motorA_prev_status = g_algopython_system_status.motor1
            motorB_prev_status = g_algopython_system_status.motor2
            time.sleep(0.05)

    elif motor_port == 0b101:  
        motorA_prev_status = g_algopython_system_status.motor1
        motorC_prev_status = g_algopython_system_status.motor3
        exit_flag = 0
        while True:
            if move_cancel_flag.is_set():
                print("Motors AC cancelled")
                break
            if ((motorA_prev_status == 1)  and (motorA_prev_status != g_algopython_system_status.motor1)):
                exit_flag = exit_flag | 0x01
            if ((motorC_prev_status == 1)  and (motorC_prev_status != g_algopython_system_status.motor2)):
                exit_flag = exit_flag | 0x02
            if exit_flag == 0x03:
                print("Motors AC completed movement")
                break
            motorA_prev_status = g_algopython_system_status.motor1
            motorC_prev_status = g_algopython_system_status.motor3
            time.sleep(0.05)

    elif motor_port == 0b110:  
        motorB_prev_status = g_algopython_system_status.motor2
        motorC_prev_status = g_algopython_system_status.motor3
        exit_flag = 0
        while True:
            if move_cancel_flag.is_set():
                print("Motors BC cancelled")
                break
            if ((motorB_prev_status == 1)  and (motorB_prev_status != g_algopython_system_status.motor2)):
                exit_flag = exit_flag | 0x01
            if ((motorC_prev_status == 1)  and (motorC_prev_status != g_algopython_system_status.motor3)):
                exit_flag = exit_flag | 0x02
            if exit_flag == 0x03:
                print("Motors BC completed movement")
                break
            motorB_prev_status = g_algopython_system_status.motor2
            motorC_prev_status = g_algopython_system_status.motor3
            time.sleep(0.05)

    elif motor_port == 0b111:
        motorA_prev_status = g_algopython_system_status.motor1
        motorB_prev_status = g_algopython_system_status.motor2
        motorC_prev_status = g_algopython_system_status.motor3
        exit_flag = 0
        while True:
            if move_cancel_flag.is_set():
                print("Motors ABC cancelled")
                break
            if ((motorA_prev_status == 1)  and (motorA_prev_status != g_algopython_system_status.motor1)):
                exit_flag = exit_flag | 0x01
            if ((motorB_prev_status == 1)  and (motorB_prev_status != g_algopython_system_status.motor2)):
                exit_flag = exit_flag | 0x02
            if ((motorC_prev_status == 1)  and (motorC_prev_status != g_algopython_system_status.motor3)):
                exit_flag = exit_flag | 0x04
            if exit_flag == 0x07:
                print("Motors ABC completed movement")
                break
            motorA_prev_status = g_algopython_system_status.motor1
            motorB_prev_status = g_algopython_system_status.motor2
            motorC_prev_status = g_algopython_system_status.motor3
            time.sleep(0.05)

def resistance_to_stop(port: str, treshold: float, is_blocking = False):
    if port not in MOTOR_MAP:
        raise ValueError("Invalid motor")
    motor_port = MOTOR_MAP[port.upper()];
    treshold_val = int((treshold * 100) / 10)

    payload = bytes([
        motor_port & 0xFF,
        (treshold_val >> 24) & 0xFF,
        (treshold_val >> 16) & 0xFF,
        (treshold_val >> 8) & 0xFF,
        (treshold_val) & 0xFF,
        ])
    
    send_packet(ALGOPYTHON_CMD_RESISTANCE_REQ, payload, wait_done=False)

    # print("Wait for motor to stop due to resistance...")

    if not is_blocking:
            return
    
    if motor_port == 0b001: 
        motor_prev_status = g_algopython_system_status.motor1
        while True:
            if move_cancel_flag.is_set():
                print("MotorA cancelled")
                break
            if (motor_prev_status == 1) and (g_algopython_system_status.motor1 == 0):
                print("MotorA stopped due to resistance")
                break
            motor_prev_status = g_algopython_system_status.motor1
            time.sleep(0.05)

    elif motor_port == 0b010: 
        motor_prev_status = g_algopython_system_status.motor2
        while True:
            if move_cancel_flag.is_set():
                print("MotorB cancelled")
                break
            if (motor_prev_status == 1) and (g_algopython_system_status.motor2 == 0):
                print("MotorB stopped due to resistance")
                break
            motor_prev_status = g_algopython_system_status.motor2
            time.sleep(0.05)

    elif motor_port == 0b100: 
        motor_prev_status = g_algopython_system_status.motor3
        while True:
            if move_cancel_flag.is_set():
                print("MotorC cancelled")
                break
            if (motor_prev_status == 1) and (g_algopython_system_status.motor3 == 0):
                print("MotorC stopped due to resistance")
                break
            motor_prev_status = g_algopython_system_status.motor3
            time.sleep(0.05)

    elif motor_port == 0b011:  
        motorA_prev_status = g_algopython_system_status.motor1
        motorB_prev_status = g_algopython_system_status.motor2
        exit_flag = 0;
        while True:
            if move_cancel_flag.is_set():
                print("Motors AB cancelled")
                break
            if ((motorA_prev_status == 1)  and (motorA_prev_status != g_algopython_system_status.motor1)):
                exit_flag = exit_flag | 0x01;
            if ((motorB_prev_status == 1)  and (motorB_prev_status != g_algopython_system_status.motor2)):
                exit_flag = exit_flag | 0x02;
            if exit_flag == 0x03:
                print("Motors AB stopped due to resistance")
                break
            motorA_prev_status = g_algopython_system_status.motor1
            motorB_prev_status = g_algopython_system_status.motor2
            time.sleep(0.05)

    elif motor_port == 0b101:  
        motorA_prev_status = g_algopython_system_status.motor1
        motorC_prev_status = g_algopython_system_status.motor3
        exit_flag = 0;
        while True:
            if move_cancel_flag.is_set():
                print("Motors AC cancelled")
                break
            if ((motorA_prev_status == 1)  and (motorA_prev_status != g_algopython_system_status.motor1)):
                exit_flag = exit_flag | 0x01;
            if ((motorC_prev_status == 1)  and (motorC_prev_status != g_algopython_system_status.motor2)):
                exit_flag = exit_flag | 0x02;
            if exit_flag == 0x03:
                print("Motors AC stopped due to resistance")
                break
            motorA_prev_status = g_algopython_system_status.motor1
            motorC_prev_status = g_algopython_system_status.motor3
            time.sleep(0.05)

    elif motor_port == 0b110:  
        motorB_prev_status = g_algopython_system_status.motor2
        motorC_prev_status = g_algopython_system_status.motor3
        exit_flag = 0;
        while True:
            if move_cancel_flag.is_set():
                print("Motors BC cancelled")
                break
            if ((motorB_prev_status == 1)  and (motorB_prev_status != g_algopython_system_status.motor2)):
                exit_flag = exit_flag | 0x01;
            if ((motorC_prev_status == 1)  and (motorC_prev_status != g_algopython_system_status.motor3)):
                exit_flag = exit_flag | 0x02;
            if exit_flag == 0x03:
                print("Motors BC stopped due to resistance")
                break
            motorB_prev_status = g_algopython_system_status.motor2
            motorC_prev_status = g_algopython_system_status.motor3
            time.sleep(0.05)

    elif motor_port == 0b111:
        motorA_prev_status = g_algopython_system_status.motor1
        motorB_prev_status = g_algopython_system_status.motor2
        motorC_prev_status = g_algopython_system_status.motor3
        exit_flag = 0;
        while True:
            if move_cancel_flag.is_set():
                print("Motors ABC cancelled")
                break
            if ((motorA_prev_status == 1)  and (motorA_prev_status != g_algopython_system_status.motor1)):
                exit_flag = exit_flag | 0x01;
            if ((motorB_prev_status == 1)  and (motorB_prev_status != g_algopython_system_status.motor2)):
                exit_flag = exit_flag | 0x02;
            if ((motorC_prev_status == 1)  and (motorC_prev_status != g_algopython_system_status.motor3)):
                exit_flag = exit_flag | 0x04;
            if exit_flag == 0x07:
                print("Motors ABC stopped due to resistance")
                break
            motorA_prev_status = g_algopython_system_status.motor1
            motorB_prev_status = g_algopython_system_status.motor2
            motorC_prev_status = g_algopython_system_status.motor3
            time.sleep(0.05)

def moveStop(stop_port: str):
    if stop_port not in MOTOR_MAP:
        raise ValueError("Invalid motor")
    motor_stop_port = MOTOR_MAP[stop_port.upper()];
    print(f"Stopping motor {stop_port}...")
    payload = bytes([
        motor_stop_port & 0xFF
        ])
    send_packet(ALGOPYTHON_CMD_MOVE_STOP_REQ, payload)

# --------------------------------------------------------------------------------------------------------------
#-----------------Light section---------------------------------------------------------------------------------

def light(port: int, duration: float , power: int, color: str | tuple[int, int, int], is_blocking = True):
    global led1_cancel_flag, led2_cancel_flag

    if port == 1:
        led1_cancel_flag.set()
        led1_cancel_flag = threading.Event()
    elif port == 2:
        led2_cancel_flag.set()
        led2_cancel_flag = threading.Event()

    if port != 1 and port != 2:
        raise ValueError("Invalid LED")
    if not (0 <= power <= 10):
        raise ValueError("Power must be 0-10")

    if isinstance(color, str):
        color = color.lower()
        if color not in COLOR_MAP:
            raise ValueError(f"Unsupported color: {color}")
        r, g, b = COLOR_MAP[color]
    elif isinstance(color, (tuple, list)) and len(color) == 3:
        r, g, b = color
    else:
        raise ValueError("Color must be string or RGB tuple/list")

    led_port = port
    led_power = int((power * 255) / 10)
    led_r, led_g, led_b = r, g, b
    led_type = 0

    if math.isinf(duration):
        print("x is positive infinity")
        led_type = 1
        led_duration = 0
        is_blocking = False
    else:
        led_duration = int(duration * 100)

    payload = bytearray([
        led_port & 0xFF,
        led_type & 0xFF,
        (led_duration >> 24) & 0xFF,
        (led_duration >> 16) & 0xFF,
        (led_duration >> 8) & 0xFF,
        (led_duration) & 0xFF,
        led_power & 0xFF,
        led_r & 0xFF,
        led_g & 0xFF,
        led_b & 0xFF
    ])

    send_packet(ALGOPYTHON_CMD_LIGHT_REQ, payload, wait_done=False)
    # print("Wait for led to finish...")

    if port == 1:
        prev_status = g_algopython_system_status.led1
        while is_blocking:
            if led1_cancel_flag.is_set():
                print("Led1 cancelled")
                break
            if prev_status == 1 and g_algopython_system_status.led1 == 0:
                print("Led1 completed")
                break
            prev_status = g_algopython_system_status.led1
            time.sleep(0.05)
    elif port == 2:
        prev_status = g_algopython_system_status.led2
        while is_blocking:
            if led2_cancel_flag.is_set():
                print("Led2 cancelled")
                break
            if prev_status == 1 and g_algopython_system_status.led2 == 0:
                print("Led2 completed")
                break
            prev_status = g_algopython_system_status.led2
            time.sleep(0.05)

def light12(duration: float , power: int, color: str | tuple[int, int, int],is_blocking = True):
    global led12_cancel_flag

    led12_cancel_flag.set()
    led12_cancel_flag = threading.Event()

    if not (0 <= power <= 10):
        raise ValueError("Power must be 0-10")

    if isinstance(color, str):
        color = color.lower()
        if color not in COLOR_MAP:
            raise ValueError(f"Unsupported color: {color}")
        r, g, b = COLOR_MAP[color]
    elif isinstance(color, (tuple, list)) and len(color) == 3:
        r, g, b = color
    else:
        raise ValueError("Color must be string or RGB tuple/list")
    led_power = int((power * 255) / 10)
    led_r, led_g, led_b = r, g, b
    led_type = 0

    if math.isinf(duration):
        print("x is positive infinity")
        led_type = 1
        led_duration = 0
        is_blocking = False
    else:
        led_duration = int(duration * 100)

    payload = bytearray([
        led_type & 0xFF,
        (led_duration >> 24) & 0xFF,
        (led_duration >> 16) & 0xFF,
        (led_duration >> 8) & 0xFF,
        (led_duration) & 0xFF,
        led_power & 0xFF,
        led_r & 0xFF,
        led_g & 0xFF,
        led_b & 0xFF
    ])

    send_packet(ALGOPYTHON_CMD_LIGHT12_REQ, payload, wait_done=False)
    # print("Wait for both leds to finish...")
    
    prev_status1 = g_algopython_system_status.led1
    prev_status2 = g_algopython_system_status.led2
    while is_blocking:
        if led12_cancel_flag.is_set():
            print("Led12 cancelled")
            break
        if (prev_status1 == 1 and g_algopython_system_status.led1 == 0) and (prev_status2 == 1 and g_algopython_system_status.led2 == 0):
            print("Led12 completed")
            break
        prev_status1 = g_algopython_system_status.led1
        prev_status2 = g_algopython_system_status.led2
        time.sleep(0.05)

def lightStop(stop_port: int):
    if stop_port not in (1, 2):
        raise ValueError("LED port must be 1 or 2")

    payload = bytes([
        stop_port & 0xFF
        ])
    send_packet(ALGOPYTHON_CMD_LIGHT_STOP_REQ, payload)

# --------------------------------------------------------------------------------------------------------------
#-----------------Play sound section----------------------------------------------------------------------------

def playSound(sound_id: int, volume: int, is_blocking=True):
    global sound_cancel_flag

    if not (0 <= volume <= 10):
        raise ValueError("Volume must be between 0 and 10")
    if sound_id not in SOUNDS_MAP:
        raise ValueError(f"Invalid sound ID: {sound_id}. Available sounds: {list(SOUNDS_MAP.keys())}")

    volume_val = int((volume / 10.0) * 255)
    payload = bytes([sound_id & 0xFF, volume_val & 0xFF])

    with sound_lock:
        sound_cancel_flag.set()
        send_packet(ALGOPYTHON_CMD_SOUND_STOP_REQ, b"") 
        time.sleep(0.05)  

        sound_cancel_flag.clear()
        send_packet(ALGOPYTHON_CMD_PLAY_SOUND_REQ, payload, wait_done=False)

    if is_blocking:
        prev_status = g_algopython_system_status.sound
        while True:
            if sound_cancel_flag.is_set():
                print("Sound cancelled")
                break
            if prev_status == 1 and g_algopython_system_status.sound == 0:
                print("Sound completed")
                break
            prev_status = g_algopython_system_status.sound
            time.sleep(0.05)

def soundStop(): 
    # print("Stopping sound...")
    send_packet(ALGOPYTHON_CMD_SOUND_STOP_REQ, b"")

def listAvailableSounds():
    sounds = SOUNDS_MAP
    print("Available Sounds:")
    for sound_id, name in sounds.items():
        print(f"{sound_id}: {name}")

# --------------------------------------------------------------------------------------------------------------
#-----------------Sensor section--------------------------------------------------------------------------------

def get_sensor_value(sensor_port: int) -> int:

    if sensor_port not in (1, 2):
        raise ValueError("Port must be 1 or 2")

    payload = bytes([sensor_port])

    send_packet(ALGOPYTHON_CMD_GET_SENSOR_REQ, payload, wait_done=False)

def wait_sensor(sensor_port: int, min: int, max: int):

    if sensor_port not in (1, 2):
        raise ValueError("sensorPort mora biti 1 ili 2")

    print(f"Waiting for sensor {sensor_port} to detect value in range [{min}, {max}]")

    payload = bytes([
        sensor_port & 0xFF, 
        min & 0xFF, 
        max & 0xFF
        ])

    send_packet(ALGOPYTHON_CMD_WAIT_SENSOR_REQ, payload, wait_done=False)

    # print("Wait for sensor to finish..."); 
    if sensor_port == 1:
        sensor1_prev_status = g_algopython_system_status.sensor1;
        while True:
            if(sensor1_prev_status == 1) and (g_algopython_system_status.sensor1 == 0): 
                print("Sensor 1 done ")
                break;
            sensor1_prev_status = g_algopython_system_status.sensor1;
    elif sensor_port == 2:
        sensor2_prev_status = g_algopython_system_status.sensor2;
        while True:
            if(sensor2_prev_status == 1) and (g_algopython_system_status.sensor2 == 0): 
                print("Sensor 2 done ")
                break;
            sensor2_prev_status = g_algopython_system_status.sensor2;
    
# --------------------------------------------------------------------------------------------------------------
#-----------------Other section---------------------------------------------------------------------------------

def wait(duration: float):
    duration = max(0.01, min(duration, 10.0))  
    print(f"Waiting for {duration:.2f} seconds...")
    time.sleep(duration)

def play_btn_pressed() -> bool:
    return g_algopython_system_status.play_btn

#--------------------------------AI section---------------------------------------------------------------------------------

# Load Haar cascades
face_cascade = cv2.CascadeClassifier('src/algopython/haarcascade_face.xml')
eye_cascade = cv2.CascadeClassifier('src/algopython/haarcascade_eye.xml')
smile_cascade = cv2.CascadeClassifier('src/algopython/haarcascade_smile.xml')

# Smile detection function
def detect(gray, frame):
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    smiles = []
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 22)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
        smiles = smile_cascade.detectMultiScale(roi_gray, 1.7, 25)
        for (sx, sy, sw, sh) in smiles:
            cv2.rectangle(roi_color, (sx, sy), (sx+sw, sy+sh), (0, 0, 255), 2)
    return frame, smiles

def face_smile_detection():
    video_capture = cv2.VideoCapture(0)
    led_state = 0
    smile_cnt = 0

    # Initial CLAHE params
    clip_limit = 3.5
    tile_size = 8

    print("""
Controls:
  q - Quit
  w/s - Increase/Decrease clipLimit (%.1f)
  e/d - Increase/Decrease tileGridSize (%d x %d)
""" % (clip_limit, tile_size, tile_size))

    while True:
        ret, frame = video_capture.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

        # Apply CLAHE with current parameters
        clahe = cv2.createCLAHE(clipLimit=clip_limit, tileGridSize=(tile_size, tile_size))
        gray_clahe = clahe.apply(gray)

        # Detect faces/smiles
        canvas, smile_det = detect(gray_clahe, frame)

        # Show result
        cv2.imshow('Smile Detection with CLAHE (Press q to quit)', canvas)

        # Handle keyboard input
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('w'):
            clip_limit = min(clip_limit + 0.1, 10.0)
        elif key == ord('s'):
            clip_limit = max(0.1, clip_limit - 0.1)
        elif key == ord('e'):
            tile_size = min(32, tile_size + 1)
        elif key == ord('d'):
            tile_size = max(1, tile_size - 1)

        # Print current CLAHE settings live
        print(f"\rclipLimit: {clip_limit:.1f}, tileGridSize: ({tile_size}, {tile_size})", end="")

        # Smile detection logic
        if len(smile_det) > 0:
            if led_state == 0:
                led_state = 1
                print("\nSmile detected, turning on light")
                light12(duration=1, power=5, color="white", is_blocking=True)
            smile_cnt = 0
        else:
            if led_state == 1 and smile_cnt > 10:
                led_state = 0
                print("\nNo smile detected, turning off light")
                lightStop(1)
                lightStop(2)
            smile_cnt += 1

    video_capture.release()
    cv2.destroyAllWindows()