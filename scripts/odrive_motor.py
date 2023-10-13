import odrive

odrv = odrive.find_any()
odrv.config.dc_bus_overvoltage_trip_level = 27
odrv.config.dc_bus_undervoltage_trip_level = 22
odrv.config.dc_max_positive_current = 5
odrv.axis0.config.motor.motor_type = odrive.enums.MOTOR_TYPE_HIGH_CURRENT
odrv.axis0.config.motor.torque_constant = 0.049520958083832334
odrv.axis0.config.motor.pole_pairs = 2
odrv.axis0.config.motor.current_soft_max = 5
odrv.axis0.config.motor.current_hard_max = 9
odrv.axis0.config.motor.calibration_current = 5
odrv.axis0.controller.config.control_mode = odrive.enums.ControlMode.VELOCITY_CONTROL
odrv.axis0.controller.config.input_mode = odrive.enums.InputMode.VEL_RAMP
odrv.axis0.config.torque_soft_min = -0.049520958083832334
odrv.axis0.config.torque_soft_max = 0.049520958083832334
odrv.axis0.config.enable_watchdog = False
odrv.axis0.config.watchdog_timeout = 1
odrv.axis0.config.encoder_bandwidth = 100
odrv.hall_encoder0.config.enabled = True
odrv.axis0.config.load_encoder = odrive.enums.EncoderId.HALL_ENCODER0
odrv.axis0.config.commutation_encoder = odrive.enums.EncoderId.HALL_ENCODER0

odrv.axis0.config.calibration_lockin.current = 5


odrv.axis0.trap_traj.config.vel_limit = 3.0
odrv.axis0.trap_traj.config.accel_limit = 4.0
odrv.axis0.trap_traj.config.decel_limit = 3.0
odrv.axis0.trap_traj.config.decel_limit = 2.0


'''odrv.axis0.config.encoder_bandwidth = 100
odrv.hall_encoder0.config.enabled = True
odrv.axis0.config.load_encoder = EncoderId.HALL_ENCODER0 #what is the encoder ID
odrv.axis0.config.commutation_encoder = EncoderId.HALL_ENCODER0
odrv.save_configuration()'''

odrv.axis0.controller.config.circular_setpoints = True

# Get the axis object
axis = odrv.axis0

# Set the desired position control mode
axis.controller.config.control_mode = ControlMode.POSITION_CONTROL

# Set the desired position setpoint in turns
axis.controller.input_pos = 10

print(dump_errors(odrv))
'''# [wait for ODrive to reboot]
odrv.axis0.requested_state = AxisState.ENCODER_HALL_POLARITY_CALIBRATION
# [wait for motor to stop]
odrv.axis0.requested_state = AxisState.ENCODER_HALL_PHASE_CALIBRATION
# [wait for motor to stop]'''

'''odrv.axis0.controller.input_pos = 360
odrv.axis0.controller.move_incremental(50, False)
'''

'''odrv.axis0.controller.config.control_mode = VELOCITY_CONTROL
odrv.axis0.controller.input_vel = 2'''


#odrv.controller.ControlMode.Torque_Control.input_torque = 2
'''# Find any ODrive connected to the computer
od = odrive.find_any()

# Access the axis and motor objects
axis = od.axis0
motor = axis.motor
#encoder = axis.encoder

# Get the current position of the encoder
#position = encoder.pos_estimate

# Add a descriptor when calling the command
#print(f"The current position of the encoder is: {position} units.")

# Additional commands:
try:
    # BulkCapture: Capture multiple variables at once
    variables = odrive.utils.bulk_capture(od, ["vbus_voltage", "ibus"])
    #vbus_voltage is the bus voltage
    #ibus is the current on the odrive

    # OperationAbortException: Exception raised when an operation is aborted
    raise odrive.utils.OperationAbortException("Operation aborted due to an error.")

except odrive.utils.OperationAbortException as e:
    # dump_errors(): Print detailed error information
    odrive.utils.dump_errors(od, True)

# fw_version_str_to_tuple(): Convert firmware version string to a tuple
fw_version = odrive.utils.fw_version_str_to_tuple(od.fw_version)
print("firmware")

# print_drv_regs(): Print driver register values
odrive.utils.print_drv_regs(od)

# ram_osci_run(): Run a RAM-based oscilloscope capture
odrive.utils.ram_osci_run(od)

# rate_test(): Test the communication rate with the ODrive
odrive.utils.rate_test(od)

# start a live plotter
#odrive.utils.start_liveplotter()
'''
'''
odrv = odrv0
odrv.config.dc_bus_overvoltage_trip_level = 30
odrv.config.dc_bus_undervoltage_trip_level = 10.5
odrv.config.dc_max_positive_current = 6
odrv.config.dc_max_negative_current = -2
odrv.axis0.controller.config.input_mode = InputMode.PASSTHROUGH
odrv.axis0.controller.config.control_mode = ControlMode.TORQUE_CONTROL
odrv.axis0.config.encoder_bandwidth = 100
odrv.hall_encoder0.config.enabled = True
odrv.axis0.config.load_encoder = EncoderId.HALL_ENCODER0
odrv.axis0.config.commutation_encoder = EncoderId.HALL_ENCODER0'''