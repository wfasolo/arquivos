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

ThingerESP8266 thing(USERNAME, DEVICE_ID, DEVICE_CREDENTIAL);

float temp = 5,
      temp_in = 0,
      pwm = 1020,
      setpoint = 10,
      setpoint_ant = 10,
      dt = 0,
      dt2 = 2000,
      tempo = 0,
      tempo_fim = 0;

String mens = "Conectando";
String mens2 = "Conectando";

// --- Função média ---
float media()

{ int cm = 0;
  temp = 0;

  for (int im = 0; im <= 10; im++) {
    sensors.requestTemperatures();//REQUISITA A TEMPERATURA DO SENSOR
    float tp = sensors.getTempCByIndex(0);
    if (tp !=  -127) {
      temp += tp;
      cm++;
    }
    delay(10);
    yield();
  }
  temp = temp / cm;
 
}

void setup()
{
  sensors.begin(); // INICIA O SENSOR DS18B20

  media();

  thing.add_wifi("LAB", "@@lucas@@");

  thing["Temp"] >> [](pson & out) {
    out = temp;
  };

  thing["PWM"] >> [](pson & out) {
    out = pwm;
  };
  thing["Tempo"] >> [](pson & out) {
    out = tempo;
  };
  thing["Mens"] >> [](pson & out) {
    out = mens;
  };
  thing["Mens2"] >> [](pson & out) {
    out = mens2;
  };

  thing["Ajustes"] << [](pson & in) {
    if (in.is_empty())
    {
      in["Setpoint"] = setpoint;
      in["PWM_SP"] = pwm;

    }
    else
    {
      setpoint = in["Setpoint"];
      pwm = in["PWM_SP"];

    }
  };
  dt = millis() / 1000;
  analogWrite(saida, pwm);
}

void loop()
{
  thing.handle();
  if (setpoint != setpoint_ant)
  {

    media();
    temp_in = temp;
    tempo = 0;
    dt = millis() / 1000;
    setpoint_ant = setpoint;
    mens = "Novo Setpoint";

    thing.stream(thing["Tempo"]);
    thing.stream(thing["Temp"]);
    thing.stream(thing["PWM"]);
    thing.stream(thing["Mens"]);

  }

  else {
    if (millis() - dt2 >= 3000)
    {
      analogWrite(saida, pwm);
      dt2 = millis();
      media();
      mens = "SetPoint: " + String(setpoint);
      mens2 = "dTemp: " + String(temp - temp_in) + " dTempo: " + String(tempo_fim);
      tempo = millis() / 1000 - dt;

      thing.stream(thing["Temp"]);
      thing.stream(thing["PWM"]);
      thing.stream(thing["Tempo"]);
      thing.stream(thing["Mens"]);
      thing.stream(thing["Mens2"]);

      if (temp >= setpoint)
      { pwm = 1000;
      }
      else {
        tempo_fim = tempo;
      }
    }
  }

}
