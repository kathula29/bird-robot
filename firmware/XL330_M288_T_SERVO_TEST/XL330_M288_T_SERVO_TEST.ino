#include <Dynamixel2Arduino.h>

#define DXL_SERIAL Serial1

Dynamixel2Arduino dxl(DXL_SERIAL);

const uint8_t DXL_ID = 1;
const float DXL_PROTOCOL_VERSION = 2.0;

void setup()
{
  Serial.begin(115200);

  // Start DYNAMIXEL communication
  dxl.begin(57600);
  dxl.setPortProtocolVersion(DXL_PROTOCOL_VERSION);

  Serial.println("XL330 Continuous Rotation Test");

  // Check servo
  if (!dxl.ping(DXL_ID))
  {
    Serial.println("ERROR: XL330 not detected!");

    while (1)
    {
      delay(1000);
    }
  }

  Serial.println("XL330 detected!");

  // Torque must be OFF before changing operating mode
  dxl.torqueOff(DXL_ID);

  // Velocity Control Mode = continuous rotation
  dxl.setOperatingMode(DXL_ID, OP_VELOCITY);

  // Turn torque back ON
  dxl.torqueOn(DXL_ID);

  Serial.println("Starting continuous rotation...");

  // Low speed for initial test
  dxl.setGoalVelocity(DXL_ID, 30);
}

void loop()
{
  // Nothing required here.
  // XL330 keeps rotating continuously.
}
