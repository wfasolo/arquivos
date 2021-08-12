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

float kp = 500,
      ki = 50,
      kd = 100,
      p = 0,
      i = 0,
      d = 0,
      pid = 0,
      erro = 0,
      tempo = 99,
      tempo2 = 0,
      dt = 5,
      valor = 10,
      temp = 25,
      temp_ant = 30,
      pwm = 1010,
      setpoint = 30,
      sp_a = setpoint;

int ck = 0;

ThingerESP8266 thing(USERNAME, DEVICE_ID, DEVICE_CREDENTIAL);

void setup()
{
  pinMode(LED_BUILTIN, OUTPUT);
  thing.add_wifi("LAB", "@@lucas@@");
  sensors.begin(); // INICIA O SENSOR DS18B20

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
  thing.handle();
  enviar();
}

void loop()
{
  thing.handle();
  digitalWrite(LED_BUILTIN, HIGH);

  if (millis() - tempo2 >= 3000)
  {
    tempo2 = millis();
    medir();
    calcular();
    checar();
    enviar();
    temp_ant = temp;
  }
}

//--- checar as restricoes ---//
void checar()
{
  //
  if (setpoint != sp_a)
  {
    ck = 0;
    sp_a = setpoint;
  }

  if (ck == 0)
  {
    pwm = 10;
    d = 0;

    if (temp >= (setpoint - 1))
    {
      pwm = 900;
      d = 0;
      ck = 1;
    }
  }

  //
  if (temp > (setpoint + 0.1) && temp < (setpoint + 1) && temp_ant > temp)
  {
    pwm = pwm - (20 * (temp - setpoint));
    digitalWrite(LED_BUILTIN, LOW);
  }
  if (temp > (setpoint - 1) && temp < (setpoint - 0.1) && temp_ant < temp)
  {
    pwm = pwm + (20 * (setpoint - temp));
    digitalWrite(LED_BUILTIN, LOW);
  }

  //
  if (temp < (setpoint - 1))
  {
    pwm = pwm - 50;
    d = 0;
  }
  if (temp > (setpoint + 1))
  {
    pwm = pwm + 50;
    d = 0;
  }

  //
  if (pwm >= 1022)
  {
    pwm = 1010;
    p, i, d = 0;
  }
  else if (pwm <= 0)
  {
    pwm = 10;
    p, i, d = 0;
  }

  analogWrite(saida, int(pwm));

}

//--- enviar os dados ---//
void enviar()
{
  // enviar dados
  thing.stream(thing["Parametros"]);
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
    delay(10);
    yield();
  }
  temp = temp / cm;
}

//--- Calcular PWM ---//
void calcular()
{
  float aberro = abs(erro);

  if ((millis() - tempo) >= (1000 * (5 - (4.99 * aberro))))
  {
    float termo1 = (setpoint - temp) / (setpoint);
    float termo2 = pow(2.7, abs(setpoint - temp));
    erro = (termo2 * termo1);
    dt = (millis() - tempo) / 1000;
    tempo = millis();
    p = (setpoint * kp * erro) / 100;
    i = (setpoint * (ki * erro * dt)) / 100;
    d += (setpoint * (kd * erro) / dt) / 100;
    pid = p + i + d;

    pwm = pwm - pid, 0;

  }
}
