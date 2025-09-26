"""Package for scripting the Nanosurf control software.
Copyright (C) Nanosurf AG - All Rights Reserved (2021)
License - MIT"""

import time
import logging
import enum
import typing
import nanosurf.lib.spm as spm
import nanosurf


class MotorID():
    """ Defines the identification parameters of a direct motor control motor.
        Has to be constructed with initial parameters for each motor. Normally the scan head class is doing so.
    """
    def __init__(self, proxy_index: int, lu_index: int, range: float):
        self.ProxyIndex = proxy_index
        self.LUIndex = lu_index
        self.Range = range

class MoveStatus(enum.IntEnum):
    """ Defines motor move status"""
    Undefined = 0
    IdleUnreferenced = 1
    IdleReferenced = 2
    Referencing = 3
    Moving = 4

class LimitStatus(enum.IntEnum):
    """ Defines motor limit switch status"""
    Undefined = 0
    InNoLimit = 1
    InUpperLimit = 2
    InLowerLimit = 3
    InBothLimits = 4
    InMultipleLimits = 5

class Direction(enum.IntEnum):
    """ Defines motor move directions for various functions """
    Forward = 0
    Backward = 1

class MotorState():
    def __init__(self):
        # Axis Status
        self.move_state = MoveStatus.Undefined
        self.limit_state = LimitStatus.Undefined

class StudioMotorControl:
    """ Base class for dealing with Nanosurf Motors. In this base class general motor control functions are used.
        For measurement head specific functions, see the corresponding child classes
    """

    class _MoveMode(enum.IntEnum):
        Absolute = 0
        Relative = 1

    def __init__(self, spm: spm.Spm = None, *args):
        """Base class for dealing with Nanosurf Motors. In this base class general motor control functions are used.
           For measurement head specific functions, see the corresponding child classes
        """
        self.connected = False
        self.spm = spm
        self.logger = logging.getLogger("Motor_Control")
        self.tick_callback = self.default_tick_callback

        self.__sleep_time_after_motor_command = 0.2 # seconds
        self.__motor_speed = 1.0 # full speed
        self.__status_poll_time = 0.0
        self.__max_wait_time = 20.0 # [s]

        self.map_move_status = [
            MoveStatus.IdleUnreferenced,
            MoveStatus.IdleReferenced,
            MoveStatus.Referencing,
            MoveStatus.Moving
        ]
        self.map_limit_status = [
            LimitStatus.InNoLimit,
            LimitStatus.InUpperLimit,
            LimitStatus.InLowerLimit,
            LimitStatus.InBothLimits,
            LimitStatus.InMultipleLimits
        ]

        if self.spm is None:
            self.logger.debug("Test: Need to connect to studio")
            self.studio = nanosurf.Studio()
            self.studio.connect()
            self.spm = self.studio.spm
        else:
            self.logger.debug("Test: Studio link already existing, no need to reconnect")
        
        self.lu_direct_motor_ctrl = self.spm.lu.direct_motor_control.instance
        self.lu_system = self.spm.lu.system.instance

    @property
    def motor_speed(self) -> float:
        """ returns the current set motor speed used far all motor movements"""
        return self.__motor_speed

    @motor_speed.setter
    def motor_speed(self, speed: float):
        """ Set all motor speeds.
        Parameter
        ----------
            val: float
                speed values range is: 0.01 > value <=1.0.
                1.0 means full speed
        """
        self.__motor_speed = min(max(0.01, speed), 1.0)

    @property
    def sleep_time_after_motor_command(self):
        """ Current sleep time in [s] after each COM motor command.  """
        return self.__sleep_time_after_motor_command

    @sleep_time_after_motor_command.setter
    def sleep_time_after_motor_command(self, val):
        """ Sleep time in [s] after each COM motor command.
            It already happened, when two motor move command to separate axes were sent through the COM interface in a row,
            there was a race condition and the same axis got twice the same command.
            Therefore it is suggested to set this parameter to 200ms, or to zero; when you don't want to wait.
        """
        self.__sleep_time_after_motor_command = min(max(0.0, val), 1.0)

    @property
    def status_poll_time(self):
        """ Sleep time in [s] during status polling. """
        return self.__status_poll_time

    @status_poll_time.setter
    def status_poll_time(self, val):
        """ Sleep time in [s] during status polling.
        """
        self.__status_poll_time = min(max(0.0, val), 1.0)

    @property
    def max_wait_time(self):
        """ Maximal time in [s] to wait for end of movement is reached. """
        return self.__max_wait_time

    @max_wait_time.setter
    def max_wait_time(self, val):
        """ Maximal time in [s] to wait for end of movement is reached.
        """
        self.__max_wait_time = min(max(0.0, val), 120.0)

    def get_motor_status(self, motor_id: MotorID) -> MotorState:
        """ collects current axis states for a motor"""
        status = MotorState()
        self.lu_direct_motor_ctrl.attribute.current_axis.value_raw = motor_id.LUIndex
        axis_status = self.lu_direct_motor_ctrl.attribute.axis_status.value_raw
        limit_switch_status = self.lu_direct_motor_ctrl.attribute.axis_limit_status.value_raw
        status.move_state = self.map_move_status[int(axis_status)]
        status.limit_state = self.map_limit_status[int(limit_switch_status)]
        return status

    def start_move_relative(self, motor_id: MotorID | list[MotorID], step_size: float | list[float]):
        """ Start a relative move from current position

        Parameters
        ---------
        motor_id:  single motorID or list of motorIDs
        step_size: float or list of float
            travel length. can be positive or negative

        """
        self.logger.debug("start motor(s) relative move")
        motor_list = [motor_id] if isinstance(motor_id, MotorID) else motor_id
        self._move_command(motor_list, step_size, StudioMotorControl._MoveMode.Relative, wait_for_end=False)

    def do_move_relative(self, motor_id: MotorID | list[MotorID], step_size: float | list[float]) -> bool:
        """ start and wait a relative move from current position

        Parameters
        ---------
        motor_id:  single motorID or list of motorIDs
        step_size: float or list of float
            travel length. can be positive or negative

        """
        self.logger.debug("do motor(s) relative move")
        motor_list = [motor_id] if isinstance(motor_id, MotorID) else motor_id
        return self._move_command(motor_list, step_size, StudioMotorControl._MoveMode.Relative, wait_for_end=True)

    def start_move_absolute(self, motor_id: MotorID | list[MotorID], target_position: float | list[float]):
        """ Start a move to absolute target position(s)

        Parameters
        ---------
        motor_id:  single motorID or list of motorIDs
        target_position: float or list of float
            travel length. can be positive or negative

        """
        self.logger.debug("start motor(s) move to absolute position")
        motor_list = [motor_id] if isinstance(motor_id, MotorID) else motor_id
        self._move_command(motor_list, target_position, StudioMotorControl._MoveMode.Absolute, wait_for_end=False)

    def do_move_absolute(self, motor_id: MotorID | list[MotorID], target_position: float | list[float]) -> bool:
        """ start and wait a move to absolute target position(s)

        Parameters
        ---------
        motor_id:  single motorID or list of motorIDs
        target_position: float or list of float
            target position has to be positive

        """
        self.logger.debug("do motor(s) move to absolute position")
        motor_list = [motor_id] if isinstance(motor_id, MotorID) else motor_id
        return self._move_command(motor_list, target_position, StudioMotorControl._MoveMode.Absolute, wait_for_end=True)

    def overwrite_max_axis_speed(self, motor_id: MotorID | list[MotorID], new_max_speed: float):
        """ update the max speed of motors defined in the hardware.
        WARNING:
        --------
        Please never change the maximum motor speed, without safety checks.
        It can damage the hardware.
        The max speed has no upper limit as it overwrites the software defined dmc max speed
        """
        motor_list = [motor_id] if isinstance(motor_id, MotorID) else motor_id
        for index, motor in enumerate(motor_list):
            self.lu_direct_motor_ctrl.attribute.current_axis.value_raw = motor.LUIndex
            self.lu_direct_motor_ctrl.attribute.axis_max_speed.value = new_max_speed
        time.sleep(self.sleep_time_after_motor_command)

    # ------- implementation ------------------------------------------

    def _move_command(self, motors: list[MotorID], move_positions: float | list[float], move_mode: _MoveMode, wait_for_end: bool) -> bool:
        """ handle the moving command """
        self.lu_direct_motor_ctrl.trigger.reset_transaction()
        for index, motor in enumerate(motors):
            move_pos = move_positions[index] if isinstance(move_positions, list) else move_positions
            self.lu_direct_motor_ctrl.attribute.current_axis.value_raw = motor.LUIndex
            self.lu_direct_motor_ctrl.attribute.axis_speed_factor.value = self._get_lu_motor_speed()
            self.lu_direct_motor_ctrl.attribute.transaction_move_relative.value_raw = move_mode.value
            self.lu_direct_motor_ctrl.attribute.transaction_move_destination.value = move_pos
            self.lu_direct_motor_ctrl.trigger.add_transaction_move()

        self.lu_direct_motor_ctrl.trigger.commit_transaction()
        time.sleep(self.sleep_time_after_motor_command)

        if wait_for_end:
            return self._wait_for_end_of_movement(motors)
        return True

    def _wait_for_end_of_movement(self,  motors: list[MotorID]) -> bool:
        """ Wait until all motors are stopped or a timeout is reached.

        Parameters
        ---------
        motors: list of motorIDs

        Returns
        -------
         done: bool
            return True if all defined motors are stopped in timout time. False if Timeout was reached
        """
        motor_moving = True
        time_out_reached = False
        start_time = time.time()
        already_checked_once = False
        while motor_moving and not time_out_reached and not already_checked_once:
            stopped = [] # list of stop state for each motor
            for motor in motors:
                status = self.get_motor_status(motor)
                if (status.move_state == MoveStatus.IdleReferenced) or (status.move_state == MoveStatus.IdleUnreferenced):
                    stopped.append(True)
                else:
                    stopped.append(False)

            if all(stopped) and already_checked_once:
                motor_moving = False
                self.logger.debug("All motor stopped")
            elif(all(stopped) and not already_checked_once):
                already_checked_once = True # We check once more
                self.logger.debug("Check again whether motors stopped")
            else:
                if (time.time() - start_time) > self.max_wait_time:
                    time_out_reached = True
                    self.logger.debug("Motors where still moving after timeout reached")

            self.tick_callback(time.time() - start_time)
            time.sleep(self.status_poll_time)
        return not time_out_reached

    def _get_lu_motor_speed(self) -> float:
        """ for LU it does not use speed factor between 0 and 1 but between 0 and 100"""
        return self.motor_speed * 100.0

    def default_tick_callback(self, time: float):
        pass