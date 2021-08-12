//https://4.bp.blogspot.com/-8ez2w_os0sA/WudzMs5oOWI/AAAAAAAAChU/Hsgg7Yf9vNou9NRjWW4LsFoFuzvZ9lI2gCLcBGAs/s1600/7.png
//esptool.py --chip ESP8266 --port /dev/ttyUSB1 --baud 115200 --before default_reset --after hard_reset  write_flash --flash_mode dio --flash_freq 40m --flash_size 4MB-c1  --no-compress 0x0 est.bin

//sudo chmod 666 /dev/ttyUSB0

#include <OneWire.h>           //BIBLIOTECA NECESSÁRIA PARA O DS18B20
#include <DallasTemperature.h> //BIBLIOTECA NECESSÁRIA PARA O DS18B20

#define DS18B20 4
#define saida 12

OneWire ourWire(DS18B20);            //CONFIGURA UMA INSTÂNCIA ONEWIRE PARA SE COMUNICAR COM DS18B20
DallasTemperature sensors(&ourWire); //PASSA A TEMPERATURA PARA O DallasTemperature

#include <ThingerESP8266.h>

#define USERNAME "wfasolo"
#define DEVICE_ID "Estufa"
#define DEVICE_CREDENTIAL "@#lucas"

ThingerESP8266 thing(USERNAME, DEVICE_ID, DEVICE_CREDENTIAL);

float kp = 250,
      ki = 50,
      kd = 200,
      p = 0,
      i = 0,
      d = 0,
      pid = 0,
      erro = 0,
      tempo = 99,
      t_env = 0,
      dt = 5,
      temp_ant = 25,
      temp = 30,
      valor = 0,
      pwm = 10,
      setpoint = 35;

void setup()
{
  pinMode(LED_BUILTIN, OUTPUT);
  analogWrite(saida, pwm);
  delay(10000);
  pwm = 500;
  yield();

  sensors.begin(); // INICIA O SENSOR DS18B20

  thing.add_wifi("LAB", "@@lucas@@");

  thing["Parametros"] >> [](pson & out) {
    out["Temp"] = temp;
    out["PWM"] = pwm;
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
  temp = media();

  if (millis() / 1000 - t_env >= 9 || abs(temp - temp_ant) >= 0.05)
  {
    t_env = millis() / 1000;
    {
      temp_ant = temp;
      controle();
      testePWM();
      enviar();
      yield();
      digitalWrite(LED_BUILTIN, LOW);

    }
  }
  analogWrite(saida, pwm);
  delay(100);
  yield();
  digitalWrite(LED_BUILTIN, HIGH);


}

void enviar()
{
  // enviar dados
  thing.stream(thing["Parametros"]);
  thing.handle();
}

// --- Função média ---
float media()

{
  int cm = 0;
  valor = 0;


  for (int im = 0; im <= 10; im++)
  {
    sensors.requestTemperatures(); //REQUISITA A TEMPERATURA DO SENSOR
    float tp = sensors.getTempCByIndex(0);
    if (tp != -127)
    {
      valor += tp;
      cm++;
    }
    delay(10);
  }
  valor = valor / cm;
  yield();
  return valor;
}

// --- Funcao teste do PWM ---
float testePWM()
{
  if (pwm >= 1022)
  {
    pwm = 900;
    p, i, d = 0;
  }
  else if (pwm <= 0)
  {
    pwm = 100;
    p, i, d = 0;
  }
}

// --- Função controle ---
void controle()
{
  erro = ((setpoint - temp) / (setpoint));
  dt = (millis() - tempo) / 1000;
  tempo = millis();
  p = (setpoint * kp * erro) / 100;
  i = (setpoint * (ki * erro) * dt) / 100;
  d += (setpoint * (kd * erro) / dt) / 100;
  pid = p + i + d;

  pwm = pwm - pid, 0;
}
