//sudo chmod 666 /dev/ttyUSB0


#define sensor  A0
#define saida  12

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
      valor_ant = 0,
      temp = 0,
      pwm = 110,
      leitura = 1,
      setpoint = 30.5;



void setup()
{
  pinMode(A0, INPUT);
  analogWrite(saida, pwm);

  thing.add_wifi("LAB", "@@lucas@@");

  thing["parametros"]  >> [](pson & out) {
    out["Temp"] = temp;
    out["PWM"] = pwm;
  };
  thing["Setpoint"] << [](pson & in) {
    if (in.is_empty()) {
      in = setpoint;
    }
    else {
      setpoint = in;
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
  thing.stream(thing["parametros"]);
  thing.stream(thing["Setpoint"]);
  thing.handle();
  yield();
}

// --- Função média ---
int media()
{

  for (int x = 0; x < 50; x++)
  {
    leitura +=  analogRead(sensor);
    delay(5);
  }
  leitura = leitura / 50;
  return leitura;
}

// --- Função controle ---
void controle()
{
  valor_ant = valor;
  int aberro = abs(erro);

  if ((millis() - tempo) >= 1000 * (5 - (4.99 * aberro)))
  {
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
