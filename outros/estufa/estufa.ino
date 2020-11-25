//sudo chmod 666 /dev/ttyUSB0

#include <OneWire.h> //BIBLIOTECA NECESSÁRIA PARA O DS18B20
#include <DallasTemperature.h> //BIBLIOTECA NECESSÁRIA PARA O DS18B20

#define DS18B20 A0
#define saida 12

OneWire ourWire(DS18B20);//CONFIGURA UMA INSTÂNCIA ONEWIRE PARA SE COMUNICAR COM DS18B20
DallasTemperature sensors(&ourWire); //PASSA A TEMPERATURA PARA O DallasTemperature

#include <ThingerESP8266.h>

#define USERNAME "wfasolo"
#define DEVICE_ID "Estufa"
#define DEVICE_CREDENTIAL "@#lucas"

ThingerESP8266 thing(USERNAME, DEVICE_ID, DEVICE_CREDENTIAL);

float kp = 0.05,
      ki = 0.05,
      kd = 0.005,
      p = 0,
      i = 0,
      d = 0,
      pid = 0,
      erro = 0,
      tempo = 1,
      dt = 0,
      valor = 0,
      temp = 0,
      pwm = 110,
      leitura = 1,
      setpoint = 30.5;

void setup()
{

  analogWrite(saida, pwm);
  sensors.begin(); // INICIA O SENSOR DS18B20

  thing.add_wifi("LAB", "@@lucas@@");

  thing["Parametros"] >> [](pson &out) {
    out["Temp"] = temp;
    out["PWM"] = pwm;
  };
  thing["PID"] << [](pson &in) {
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
  controle();
}

void enviar()
{
  // enviar dados
  thing.stream(thing["Parametros"]);
  thing.stream(thing["PID"]);
  thing.handle();
  yield();
}

// --- Função média ---
int media()
{

  for (int x = 0; x < 50; x++)
  {sensors.requestTemperatures();//REQUISITA A TEMPERATURA DO SENSOR
    leitura += sensors.getTempCByIndex(0);
    delay(5);
  }
  leitura = leitura / 50;
  return leitura;
}

// --- Função controle ---
void controle()
{

  if ((millis() - tempo) >= 1000 * (5 - (4.99 * aberro)))
  {
    float valor_ant = valor;
    float aberro = abs(erro);
    valor = media();

    erro = ((setpoint - valor_ant) / (setpoint + valor));
    dt = (millis() - tempo) / 1000;
    tempo = millis();
    p = setpoint * kp * erro;
    i = setpoint * (ki * erro) * dt;
    d += setpoint * (kd * erro) / dt;
    pid = p + i + d;

    pwm = pwm - pid, 0;

    if (pwm >= 1022)
    {
      pwm = 1022;
    }
    else if (pwm <= 0)
    {
      pwm = 1;
    }

    analogWrite(saida, pwm);
    enviar();
    yield();
  }
}
