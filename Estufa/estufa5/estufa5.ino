//https://4.bp.blogspot.com/-8ez2w_os0sA/WudzMs5oOWI/AAAAAAAAChU/Hsgg7Yf9vNou9NRjWW4LsFoFuzvZ9lI2gCLcBGAs/s1600/7.png
//esptool.py --chip ESP8266 --port /dev/ttyUSB1 --baud 115200 --before default_reset --after hard_reset  write_flash --flash_mode dio --flash_freq 40m --flash_size 4MB-c1  --no-compress 0x0 est.bin

//sudo chmod 666 /dev/ttyUSB0

#include <OneWire.h> //BIBLIOTECA NECESSÁRIA PARA O DS18B20
#include <DallasTemperature.h> //BIBLIOTECA NECESSÁRIA PARA O DS18B20
#include <ESP8266WiFi.h>
#include <ESP8266WiFiMulti.h>
ESP8266WiFiMulti multiWiFi;

#define DS18B20 D5
#define saida D6

OneWire ourWire(DS18B20);//CONFIGURA UMA INSTÂNCIA ONEWIRE PARA SE COMUNICAR COM DS18B20
DallasTemperature sensors(&ourWire); //PASSA A TEMPERATURA PARA O DallasTemperature

#include <ThingerESP8266.h>

#define USERNAME "wfasolo"
#define DEVICE_ID "Estufa"
#define DEVICE_CREDENTIAL "@#lucas"

float  kp = 120, ki = 20, kd = 120,
       p = 0, i = 0, d = 0,
       integral = 0, derivada = 0,
       setpoint = 25, pid = 0, erro = 0,
       tempo = 0, tempo1 = 0, tempo2 = 0, tempo3 = 0,
       tempo4 = 0, tempo_rele = 0, minutos = 0,
       temp = 25, temp_ant = 0,
       temp_r1 = 40, temp_r2 = 50, temp_r3 = 60,
       tempo_r1 = 20, tempo_r2 = 20, tempo_r3 = 20;

int ck = 0, tempo_adc = 10;
bool botao = false;
String mens = "Iniciando...";


ThingerESP8266 thing(USERNAME, DEVICE_ID, DEVICE_CREDENTIAL);

void setup()
{
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(saida, OUTPUT);
  digitalWrite(saida, HIGH); //desligar//
  WiFi.mode(WIFI_STA);
  multiWiFi.addAP("FASOLO", "@@lucas@@");
  multiWiFi.addAP("LAB", "@@lucas@@");
  multiWiFi.addAP("a1", "@1234567@");
  WiFi.hostname("Cerveja");
  sensors.begin(); // INICIA O SENSOR DS18B20

  thing["Parametros"] >> [](pson & out) {
    out["Temp"] = temp;
    out["Tempo_Rele"] = tempo_rele;
    out["SetPoint"] = setpoint;
    out["P"] = p;
    out["I"] = i;
    out["D"] = d;
    out["Tempo"] = int(minutos);
    out["Mensagem"] = mens;
  };

  thing["PID"] << [](pson & in) {
    if (in.is_empty())
    {
      in["Tempo_Adc"] = tempo_adc;
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
  thing["RAMPA"] << [](pson & in) {
    if (in.is_empty())
    {
      in["Temp_R1"] = temp_r1;
      in["Temp_R2"] = temp_r2;
      in["Temp_R3"] = temp_r3;
      in["Tempo_R1"] = tempo_r1;
      in["Tempo_R2"] = tempo_r2;
      in["Tempo_R3"] = tempo_r3;
    }
    else
    {
      temp_r1 = in["Temp_R1"];
      temp_r2 = in["Temp_R2"];
      temp_r3 = in["Temp_R3"];
      tempo_r1 = in["Tempo_R1"];
      tempo_r2 = in["Tempo_R2"];
      tempo_r3 = in["Tempo_R3"];
    }
  };

  thing["Botao"] << [](pson & in) {
    botao = in ;
  };
}

void loop()
{
  thing.handle();
  digitalWrite(LED_BUILTIN, HIGH);

  if (botao == false)
  {
    if (millis() - tempo1 >= 1000)
    {
      digitalWrite(saida, HIGH); //desligar//
      tempo1 = millis();
      tempo4 = millis();
      p = 0, i = 0, d = 0;
      minutos = 0;
      setpoint = temp_r1;
      tempo_rele = 0;
      mens = "Desligado";
      medir();
    }
  }
  else
  {
    if (millis() - tempo2 >= 1000)
    { tempo2 = millis();
      medir();
    }
    if (millis() - tempo3 >= 5000 || abs(temp - temp_ant) >= 0.1)
    {
      tempo3 = millis();
      rampa();
      calcular();
      checar();
      temp_ant = temp;
    }
  }
}


//--- checar as restricoes ---//
void checar()
{
  if ((millis() - tempo4) <= (tempo_rele * 1000) && temp < setpoint)
  {
    digitalWrite(saida, LOW);
    mens = "Rele ON";
  }
  else
  { tempo3 = millis();
    digitalWrite(saida, HIGH);
    mens = "Rele OFF";
    p = 0, i = 0, d = 0;
  }

  if (temp < setpoint && temp_ant < temp && temp >= (setpoint - 1))
  {
    digitalWrite(saida, HIGH);
    mens = "Rele OFF";
    tempo_rele = 0;
    p = 0, i = 0, d = 0;
  }
  if (temp >= setpoint)
  {
    mens = "Rele OFF";
    tempo_rele = tempo_adc;
    p = 0, i = 0, d = 0;
  }

  if (temp <= setpoint - 4)
  {
    digitalWrite(saida, LOW);
    mens = "Rele ON";
    tempo_rele = 0;
  }
}

//--- Calcular PWM ---//
void calcular()
{
  float prev_erro = erro;
  erro =  temp - setpoint;

  float dt = (millis() - tempo) / 1000;
  tempo = millis();

  integral = integral + erro * dt;
  derivada = (erro - prev_erro) / dt;

  p = kp * erro * 0.01;
  i = ki * integral * 0.0001;
  d = kd *  derivada * 0.1 ;
  pid = p + i + d;

  tempo_rele -= pid;
}

void rampa()
{ minutos = (millis() - tempo1) / 60000;

  if ( minutos <= tempo_r1)
  {
    setpoint = temp_r1;
  }
  //
  if ( minutos > tempo_r1 && minutos <= (tempo_r1 + tempo_r2))
  {
    setpoint = temp_r2;
  }
  //
  if ( minutos > (tempo_r1 + tempo_r2) && minutos <= (tempo_r1 + tempo_r2 + tempo_r3))
  {
    setpoint = temp_r3;
  }
  //
  if ( minutos > (tempo_r1 + tempo_r2 + tempo_r3) && minutos <= (tempo_r1 + tempo_r2 + tempo_r3 + 10))
  {
    setpoint = 75; // mash out //
  }
  //
  if ( minutos > (tempo_r1 + tempo_r2 + tempo_r3 + 10))
  {
    botao = false;
  }
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
