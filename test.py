import time
from cannet import steppercontroller, bot
import can
from cannet.steppercontroller import WorkMode, CalibrationMode

bus = can.interface.Bus(channel="can0", bustype='socketcan_native')
robot = bot.Robot(bus)
robot.online = True
step = steppercontroller.StepperController(robot, 0x230)
robot.addDevice(step)
robot.start()


# параметры для двигателя 0
step.setParamRequest(0x02, 160)  # Calibrate step length
step.setParamRequest(0x03, 30)  # Min step length
step.setParamRequest(0x04, 60)  # Max step length
step.setParamRequest(0x05, 2)  # Accel brake step

# параметры для двигателя 1
step.setParamRequest(0x0F, 80)  # Calibrate step length
step.setParamRequest(0x10, 10)  # Min step length
step.setParamRequest(0x11, 80)  # Max step length
step.setParamRequest(0x12, 2)  # Accel brake step

# параметры для двигателя 2
step.setParamRequest(0x1C, 80)  # Calibrate step length
step.setParamRequest(0x1D, 10)  # Min step length
step.setParamRequest(0x1E, 80)  # Max step length
step.setParamRequest(0x1F, 2)  # Accel brake step

step.setWorkMode(0, WorkMode.CONTROL_POSITION)
step.setWorkMode(1, WorkMode.CONTROL_POSITION)
step.setWorkMode(2, WorkMode.CONTROL_POSITION)

step.calibrate(0, CalibrationMode.FULL)
step.calibrate(1, CalibrationMode.FULL)
step.calibrate(2, CalibrationMode.FULL)

time.sleep(10)
print(step.getParamByNum(0x0D))
step.setPosition(0, 1000)

try:
    while True:
        time.sleep(2)
        #print(step.isConnected)
        #step.checkConnectionRequest()

except KeyboardInterrupt:
    bus.flush_tx_buffer()
    bus.stop_all_periodic_tasks()
    bus.shutdown()
    print(bus.state)
