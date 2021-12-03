#include <ros/ros.h>
#include <std_msgs/Float32.h>
#include <std_msgs/UInt32.h>

#include "pigpiod_if2.h"

#include <iostream>
#include <cstdlib>
#include <string>
#include <cstring>
#include <cctype>
#include <thread>
#include <chrono>

#define ACCEL_SERVO_PIN 17
#define POWER_SERVO_PIN 4
#define MIN_PULSE 600
#define MAX_PULSE 2400

class Servo_ctrl{
  private:
    int _servo_pin;
    int _pi_fd;
    int _off_pulse;
    int _on_pulse;
  public:
    Servo_ctrl(int servo_pin, int pi_fd, int off_pulse, int on_pulse):_pi_fd(pi_fd),_servo_pin(servo_pin),_off_pulse(off_pulse), _on_pulse(on_pulse){};
    
    void set_position(int pulse_width)
    {
      set_servo_pulsewidth(_pi_fd, _servo_pin, pulse_width);
    }
    void turn_on(){
      set_position(_on_pulse);
    }
    void turn_off(){
      set_position(_off_pulse);
    }    
};

class Servo_ctrl_ROS{
	private:
	   Servo_ctrl _servo;
	    ros::Subscriber pos_sub_;  
	    ros::Subscriber state_sub_;  
		    
	void callback_pos(const std_msgs::UInt32 &msg){
	  _servo.set_position(msg.data);
		}

	void callback_state(const std_msgs::UInt32 &msg){
	  if(msg.data)
		_servo.turn_on();
	  else
		_servo.turn_off();
		}
	public:
	  Servo_ctrl_ROS(ros::NodeHandle *nh,Servo_ctrl servo, std::string pos_sub_topic, std::string state_sub_topic):_servo(servo){
		pos_sub_ = nh->subscribe(pos_sub_topic,10,&Servo_ctrl_ROS::callback_pos, this);	
		state_sub_ = nh->subscribe(state_sub_topic,10,&Servo_ctrl_ROS::callback_state, this);
	}


};

/////////////////////////////////////////////////////////////////////////////

int main(int argc, char** argv)
{

ROS_INFO("%s","Staring uu_ctrl\n");

  ros::init(argc, argv, "uu_ctrl");
  ros::NodeHandle nh;

int pi_fd;
  if ((pi_fd = pigpio_start(0, 0)) < 0)
    ROS_INFO("\ngpioInitialise error - is pigpiod running?");

Servo_ctrl_ROS accel_servo(&nh,Servo_ctrl(ACCEL_SERVO_PIN,pi_fd, MIN_PULSE, MAX_PULSE), "uu_ctl/accel/pos", "uu_ctl/accel/state");
Servo_ctrl_ROS power_servo(&nh,Servo_ctrl(POWER_SERVO_PIN,pi_fd, MIN_PULSE, MAX_PULSE), "uu_ctl/power/pos", "uu_ctl/power/state");
	
int debug;
//if no argument passed ferquency = 100 hz else set frq
if (!nh.getParam("debug", debug))
  debug = 0;

int frq;
//if no argument passed ferquency = 100 hz else set frq
if (!nh.getParam("frq", frq))
  frq = 100;

////////////////////////////////////////////////////////////////////////

ros::Rate r(frq); // 20 hz - 5ms // 50hz - 2ms // 100hz - 1ms
while (ros::ok())
{
  ros::spinOnce();
  r.sleep();
}

  return 0;
}
