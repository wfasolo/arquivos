//https://4.bp.blogspot.com/-8ez2w_os0sA/WudzMs5oOWI/AAAAAAAAChU/Hsgg7Yf9vNou9NRjWW4LsFoFuzvZ9lI2gCLcBGAs/s1600/7.png
//esptool.py --chip ESP8266 --port /dev/ttyUSB1 --baud 115200 --before default_reset --after hard_reset  write_flash --flash_mode dio --flash_freq 40m --flash_size 4MB-c1  --no-compress 0x0 est.bin

//sudo chmod 666 /dev/ttyUSB0

#include <OneWire.h> //BIBLIOTECA NECESSÁRIA PARA O DS18B20
#include <DallasTemperature.h> //BIBLIOTECA NECESSÁRIA PARA O DS18B20

#define DS18B20 4
#define saida 12

OneWire ourWire(DS18B20);//CONFIGURA UMA INSTÂNCIA ONEWIRE PARA SE COMUNICAR COM DS18B20
DallasTemperature sensors(&ourWire); //PASSA A TEMPERATURA PARA O DallasTemperature

#include <ThingerESP8266.h>

#define USERNAME "wfasolo"
#define DEVICE_ID "Estufa"
#define DEVICE_CREDENTIAL "@#lucas"

float kp = 10, ki = 5, kd = 5,
      p = 0, i = 0, d = 0,
      sum_erro = 0,
      pwm = 1020,  erro = 0, pid = 0,
      tempo = 0, tempo1 = 0, tempo2 = 0,
      temp = 27, temp_ant = 27,
      setpoint = 35, sp_a = setpoint;

ThingerESP8266 thing(USERNAME, DEVICE_ID, DEVICE_CREDENTIAL);

void setup()
{
  pinMode(LED_BUILTIN, OUTPUT);
  thing.add_wifi("LAB", "@@lucas@@");
  sensors.begin(); // INICIA O SENSOR DS18B20

  medir();
  temp_ant = sp_a = temp;

  thing["Parametros"] >> [](pson & out) {
    out["Temp"] = temp;
    out["PWM"] = int(pwm);
    out["SetPoint"] = setpoint;
    out["P"] = p;
    out["I"] = i;
    out["D"] = d;
  };

  thing["PID"] << [](pson & in) {
    if (in.is_empty())
    {
      in["Setpoint"] = setpoint;
      in["KP"] = kp;
      in["KI"] = ki;
      in["KD"] = kd;
    }
    else
    {
      setpoint = in["Setpoint"];
      kp = in["KP"];
      ki = in["KI"];
      kd = in["KD"];
    }
  };
}

void loop()
{
  thing.handle();
  digitalWrite(LED_BUILTIN, HIGH);
  if (millis() - tempo1 >= 1000)
  {
    tempo1 = millis();
    medir();
  }

  if (millis() - tempo2 >= 10000 || abs(temp - temp_ant) >= 0.05)
  { tempo2 = millis();
    temp_ant = temp;
    calcular();
    checar();
  }
}

//--- checar as restricoes ---//
void checar()
{
  //
  if (setpoint != sp_a)
  {
    p = i = d = 0;
    integral = derivada = 0;
    sp_a = setpoint;
    pwm=500;
  }

  //
  if (temp > (setpoint - 1) && temp < (setpoint + 1))
  {
    digitalWrite(LED_BUILTIN, LOW);
  }


  if (temp <= (setpoint * 0.9))
  {
    pwm = pwm / 2;
  }
  if (temp >= (setpoint * 1.1))
  {
    pwm = pwm * 2;
  }

  //
  if (pwm >= 1022)
  {
    pwm = 1010;
  }
  else if (pwm <= 0)
  {
    pwm = 10;
  }

  analogWrite(saida, int(pwm));

}

//--- medir temepratura ---//
void medir()
{
  int cm = 1;

  for (int im = 0; im <= 10; im++) {
    sensors.requestTemperatures();//REQUISITA A TEMPERATURA DO SENSOR
    float tp = sensors.getTempCByIndex(0);
    if (tp !=  -127) {
      temp += tp;
      cm++;
    }
    delay(5);
 }
  yield();
  temp = temp / cm;
}

//--- Calcular PWM ---//
void calcular()
{
  float prev_erro = erro;
  erro =  setpoint - temp;

  float dt = (millis() - tempo) / 1000;
  tempo = millis();

  sum_erro = (erro - prev_erro);
 
  p = kp * erro;
  i = ki * sum_erro * dt;
  d = kd * sum_erro * dt;
  pid = p + i + d;

  pwm = pwm - pid, 0;
}
