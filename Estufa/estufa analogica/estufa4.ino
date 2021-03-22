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

float kp = 20, ki = 5, kd = 1,
      p = 0, i = 0, d = 0,
      integral = 0, derivada = 0,
      tempo = 0, tempo2 = 0,
      temp = 25, nova_temp = 26, final_temp = 25,
      temp_ant = 0,
      setpoint = 25, pid = 0, erro = 0;

int ck = 0;


ThingerESP8266 thing(USERNAME, DEVICE_ID, DEVICE_CREDENTIAL);

void setup()
{
  pinMode(LED_BUILTIN, OUTPUT);
  thing.add_wifi("LAB", "@@lucas@@");
  sensors.begin(); // INICIA O SENSOR DS18B20

  thing["Parametros"] >> [](pson & out) {
    out["Temp"] = temp;
    out["Nova_Temp"] = nova_temp;
    out["Final_Temp"] = final_temp;
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
  thing.handle();
}

void loop()
{
  thing.handle();
  digitalWrite(LED_BUILTIN, HIGH);

  if (millis() - tempo2 >= 1000)
  {
    tempo2 = millis();
    medir();
    checar();
  }
}

//--- checar as restricoes ---//
void checar()
{
  //
  if (temp > (setpoint > -1) && temp < (setpoint + 1))
  {
    digitalWrite(LED_BUILTIN, LOW);
  }

  if (temp <= setpoint - 1)
  {
    ck = 0;
    digitalWrite(saida, LOW); //ligar//
  }

  if (temp >= nova_temp || temp >= setpoint)
  {
    digitalWrite(saida, HIGH); //disligar//
  }

  if (temp >= setpoint && temp_ant > temp && ck = 0)
  { ck = 1;
    final_temp = temp;
    calcular();
  }
}

//--- medir temepratura ---//
void medir()
{
  temp_ant = temp;
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
  erro =  final_temp - temp;

  float dt = (millis() - tempo) / 1000;
  tempo = millis();

  integral = integral + erro * dt;
  derivada = (erro - prev_erro) / dt;

  p = kp * erro;
  i = ki * integral;
  d = kd *  derivada;
  pid = p + i + d;

  nova_temp = nova_temp - pid, 0;
}
