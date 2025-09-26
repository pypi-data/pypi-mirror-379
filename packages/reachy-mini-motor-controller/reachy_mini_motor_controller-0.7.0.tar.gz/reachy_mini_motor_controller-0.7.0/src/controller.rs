use std::time::Duration;

use rustypot::servo::{dynamixel::xl330, feetech::sts3215};

pub struct ReachyMiniMotorController {
    dph_v1: rustypot::DynamixelProtocolHandler,
    dph_v2: rustypot::DynamixelProtocolHandler,
    serial_port: Box<dyn serialport::SerialPort>,
}

impl ReachyMiniMotorController {
    pub fn new(serialport: &str) -> Result<Self, Box<dyn std::error::Error>> {
        let dph_v1 = rustypot::DynamixelProtocolHandler::v1();
        let dph_v2 = rustypot::DynamixelProtocolHandler::v2();

        let serial_port = serialport::new(serialport, 1_000_000)
            .timeout(Duration::from_millis(10))
            .open()?;

        Ok(Self {
            dph_v1,
            dph_v2,
            serial_port,
        })
    }

    pub fn check_missing_ids(&mut self) -> Result<Vec<u8>, Box<dyn std::error::Error>> {
        let mut missing_ids = Vec::new();

        for id in [11, 21, 22] {
            if sts3215::read_id(&self.dph_v1, self.serial_port.as_mut(), id).is_err() {
                missing_ids.push(id);
            }
        }
        for id in [1, 2, 3, 4, 5, 6] {
            if xl330::read_id(&self.dph_v2, self.serial_port.as_mut(), id).is_err() {
                missing_ids.push(id);
            }
        }

        Ok(missing_ids)
    }

    pub fn read_all_positions(&mut self) -> Result<[f64; 9], Box<dyn std::error::Error>> {
        let mut pos = Vec::new();

        pos.extend(sts3215::sync_read_present_position(
            &self.dph_v1,
            self.serial_port.as_mut(),
            &[11, 21, 22],
        )?);
        pos.extend(xl330::sync_read_present_position(
            &self.dph_v2,
            self.serial_port.as_mut(),
            &[1, 2, 3, 4, 5, 6],
        )?);

        Ok(pos.try_into().unwrap())
    }

    pub fn set_all_goal_positions(
        &mut self,
        positions: [f64; 9],
    ) -> Result<(), Box<dyn std::error::Error>> {
        sts3215::sync_write_goal_position(
            &self.dph_v1,
            self.serial_port.as_mut(),
            &[11, 21, 22],
            &positions[0..3],
        )?;
        xl330::sync_write_goal_position(
            &self.dph_v2,
            self.serial_port.as_mut(),
            &[1, 2, 3, 4, 5, 6],
            &positions[3..9],
        )?;

        Ok(())
    }

    pub fn set_antennas_positions(
        &mut self,
        positions: [f64; 2],
    ) -> Result<(), Box<dyn std::error::Error>> {
        sts3215::sync_write_goal_position(
            &self.dph_v1,
            self.serial_port.as_mut(),
            &[21, 22],
            &positions,
        )?;

        Ok(())
    }

    pub fn set_stewart_platform_position(
        &mut self,
        position: [f64; 6],
    ) -> Result<(), Box<dyn std::error::Error>> {
        xl330::sync_write_goal_position(
            &self.dph_v2,
            self.serial_port.as_mut(),
            &[1, 2, 3, 4, 5, 6],
            &position,
        )?;

        Ok(())
    }
    pub fn set_body_rotation(&mut self, position: f64) -> Result<(), Box<dyn std::error::Error>> {
        sts3215::sync_write_goal_position(
            &self.dph_v1,
            self.serial_port.as_mut(),
            &[11],
            &[position],
        )?;

        Ok(())
    }

    pub fn is_torque_enabled(&mut self) -> Result<bool, Box<dyn std::error::Error>> {
        let sts_torque = sts3215::sync_read_torque_enable(
            &self.dph_v1,
            self.serial_port.as_mut(),
            &[11, 21, 22],
        )?;
        let xl_torque = xl330::sync_read_torque_enable(
            &self.dph_v2,
            self.serial_port.as_mut(),
            &[1, 2, 3, 4, 5, 6],
        )?;

        Ok(sts_torque.iter().all(|&x| x) && xl_torque.iter().all(|&x| x))
    }

    pub fn enable_torque(&mut self) -> Result<(), Box<dyn std::error::Error>> {
        self.set_torque(true)
    }
    pub fn disable_torque(&mut self) -> Result<(), Box<dyn std::error::Error>> {
        self.set_torque(false)
    }

    fn set_torque(&mut self, enable: bool) -> Result<(), Box<dyn std::error::Error>> {
        sts3215::sync_write_torque_enable(
            &self.dph_v1,
            self.serial_port.as_mut(),
            &[11, 21, 22],
            &[enable; 3],
        )?;
        xl330::sync_write_torque_enable(
            &self.dph_v2,
            self.serial_port.as_mut(),
            &[1, 2, 3, 4, 5, 6],
            &[enable; 6],
        )?;

        Ok(())
    }

    pub fn set_stewart_platform_goal_current(
        &mut self,
        current: [i16; 6],
    ) -> Result<(), Box<dyn std::error::Error>> {
        xl330::sync_write_goal_current(
            &self.dph_v2,
            self.serial_port.as_mut(),
            &[1, 2, 3, 4, 5, 6],
            &current,
        )?;

        Ok(())
    }

    pub fn read_stewart_platform_current(
        &mut self,
    ) -> Result<[i16; 6], Box<dyn std::error::Error>> {
        let currents = xl330::sync_read_present_current(
            &self.dph_v2,
            self.serial_port.as_mut(),
            &[1, 2, 3, 4, 5, 6],
        )?;

        Ok(currents.try_into().unwrap())
    }

    pub fn set_stewart_platform_operating_mode(
        &mut self,
        mode: u8,
    ) -> Result<(), Box<dyn std::error::Error>> {
        xl330::sync_write_operating_mode(
            &self.dph_v2,
            self.serial_port.as_mut(),
            &[1, 2, 3, 4, 5, 6],
            &[mode; 6],
        )?;

        Ok(())
    }

    pub fn read_stewart_platform_operating_mode(
        &mut self,
    ) -> Result<[u8; 6], Box<dyn std::error::Error>> {
        let modes = xl330::sync_read_operating_mode(
            &self.dph_v2,
            self.serial_port.as_mut(),
            &[1, 2, 3, 4, 5, 6],
        )?;

        Ok(modes.try_into().unwrap())
    }

    pub fn set_antennas_operating_mode(
        &mut self,
        mode: u8,
    ) -> Result<(), Box<dyn std::error::Error>> {
        sts3215::sync_write_mode(
            &self.dph_v1,
            self.serial_port.as_mut(),
            &[21, 22],
            &[mode; 2],
        )?;

        Ok(())
    }

    pub fn set_body_rotation_operating_mode(
        &mut self,
        mode: u8,
    ) -> Result<(), Box<dyn std::error::Error>> {
        sts3215::sync_write_mode(&self.dph_v1, self.serial_port.as_mut(), &[11], &[mode])?;

        Ok(())
    }

    pub fn enable_body_rotation(&mut self, enable: bool) -> Result<(), Box<dyn std::error::Error>> {
        sts3215::sync_write_torque_enable(
            &self.dph_v1,
            self.serial_port.as_mut(),
            &[11],
            &[enable],
        )?;

        Ok(())
    }

    pub fn enable_antennas(&mut self, enable: bool) -> Result<(), Box<dyn std::error::Error>> {
        sts3215::sync_write_torque_enable(
            &self.dph_v1,
            self.serial_port.as_mut(),
            &[21, 22],
            &[enable; 2],
        )?;

        Ok(())
    }

    pub fn enable_stewart_platform(
        &mut self,
        enable: bool,
    ) -> Result<(), Box<dyn std::error::Error>> {
        xl330::sync_write_torque_enable(
            &self.dph_v2,
            self.serial_port.as_mut(),
            &[1, 2, 3, 4, 5, 6],
            &[enable; 6],
        )?;

        Ok(())
    }
}
