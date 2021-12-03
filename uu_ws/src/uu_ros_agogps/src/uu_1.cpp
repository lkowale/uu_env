#include <ros/ros.h>
#include <std_msgs/Float32.h>
#include <std_msgs/UInt32.h>
#include <std_msgs/Int8.h>

#include "pigpiod_if2.h"

#include <iostream>
#include <cstdlib>
#include <string>
#include <cstring>
#include <cctype>
#include <thread>
#include <chrono>

#define ACCEL_SERVO_PIN 4
#define POWER_SERVO_PIN 18
#define LIFT_SERVO_PIN 17
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
		ros::NodeHandle *_nh;
		    
	void callback_pos(const std_msgs::UInt32 &msg){
	  _servo.set_position(msg.data);
		}

	void callback_state(const std_msgs::UInt32 &msg){
	  state = msg.data;
		}

	public:
	  int state;
	  Servo_ctrl_ROS(ros::NodeHandle *nh,Servo_ctrl servo, std::string pos_sub_topic, std::string state_sub_topic):_servo(servo),_nh(nh){
		pos_sub_ = _nh->subscribe(pos_sub_topic,10,&Servo_ctrl_ROS::callback_pos, this);	
		state_sub_ = _nh->subscribe(state_sub_topic,10,&Servo_ctrl_ROS::callback_state, this);
	}
    void turn_on(){
      _servo.turn_on();
    }
    void turn_off(){
      _servo.turn_off();
    } 

};

/*
class Tractor {
private:
	ros::NodeHandle *_nh;
public:

};
*/

/////////////////////////////////////////////////////////////////////////////

int main(int argc, char** argv)
{



ROS_INFO("%s","Starting uu_1\n");

  ros::init(argc, argv, "uu_1");
  ros::NodeHandle nh;

int pi_fd;
  if ((pi_fd = pigpio_start(0, 0)) < 0)
    ROS_INFO("\ngpioInitialise error - is pigpiod running?");

Servo_ctrl_ROS accel_servo(&nh,Servo_ctrl(ACCEL_SERVO_PIN,pi_fd, MIN_PULSE, MAX_PULSE), "uu_ctl/accel/pos", "uu_ctl/accel/state");
Servo_ctrl_ROS power_servo(&nh,Servo_ctrl(POWER_SERVO_PIN,pi_fd, MIN_PULSE, MAX_PULSE), "uu_ctl/power/pos", "uu_ctl/power/state");
Servo_ctrl_ROS lift_servo(&nh,Servo_ctrl(LIFT_SERVO_PIN,pi_fd, MIN_PULSE, MAX_PULSE), "uu_ctl/lift/pos", "lift_position");
	



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

	if(lift_servo.state==2){
		lift_servo.turn_on();
		accel_servo.turn_off();
}
	else if (lift_servo.state==1){
		lift_servo.turn_off();
		accel_servo.turn_on();
}


  r.sleep();
}

  return 0;
}
