#include <Time.h>
#include <ThingerESP8266.h>
#include <NTPClient.h>
#include <WiFiUdp.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BME280.h>

#define USERNAME "wfasolo"
#define DEVICE_ID "Estacao"
#define DEVICE_CREDENTIAL "@#lucas"

#define SSID "FASOLO"
#define SSID_PASSWORD "@@lucas@@"

WiFiUDP udp;//Cria um objeto "UDP"
NTPClient ntp(udp, "a.st1.ntp.br", -3 * 3600, 60000);
Adafruit_BME280 bme;

float cont = 50000,
      cont2 = 0,
      pres = 0,
      temp = 0,
      umid = 0;
int chuv = 0;
const int pinoSensor = D5;

ThingerESP8266 thing(USERNAME, DEVICE_ID, DEVICE_CREDENTIAL);

void setup()
{
  pinMode(pinoSensor, INPUT);
  ntp.begin();
  bme.begin(0x76);
  thing.add_wifi(SSID, SSID_PASSWORD);

  // resource output example (i.e. reading a sensor value)
  thing["parametros"] >> [](pson & out) {
    out["Chuv"] = chuv;
    out["Pres"] = pres;
    out["Temp"] = temp;
    out["Umid"] = umid;
  };
  //thing["Alt"] >> outputValue(bme.readAltitude(PressaoaNivelDoMar_HPA));
}

void loop()
{
  if (millis() - cont >= 60000) {

    // Atualizacao da hora
    ntp.forceUpdate();

    String hora = ntp.getFormattedTime();
    String a = String(hora[3]);
    String b = String(hora[4]);
    String minu = a + b;
    //
    
    // chuva
    if (digitalRead(pinoSensor) == HIGH) {
      chuv = 0;
    } else {
      chuv = 1;
    }
    //
    
    // medicao da temperatura
    pres = 0;
    temp = 0;
    umid = 0;
    
    for (int i = 0; i <= 124; i++) {

      pres = pres + bme.readPressure();
      temp = temp + bme.readTemperature();
      umid = umid + bme.readHumidity();
      delay(25);
    }

    pres = pres / (12500 * 0.99),
    temp = temp / 125,
    umid = umid / (125 * 0.9);
    //

    // gravacao no banco de dados a cada 15 minutos
    if (minu.toInt() == 00 || minu.toInt() == 15 || minu.toInt() == 30 || minu.toInt() == 45)
    {
      thing.write_bucket("dados_estacao1", "parametros");
    }
    //

    // enviar dados
    thing.stream(thing["parametros"]);
    //thing.stream(thing["Alt"]);

    cont = millis();

  }

  if (millis() - cont2 >= 15000)
  {
    thing.handle();
    cont2 = millis();
  }
}
