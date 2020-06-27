#include <Adafruit_Sensor.h>
#include <Adafruit_BME280.h>
#include <math.h>


Adafruit_BME280 bme;

#include <ThingerESP8266.h>

#define USERNAME "i9pool"
#define DEVICE_ID "teste123"
#define DEVICE_CREDENTIAL "&Ee9tOgwmKb7wB"

#define SSID "FASOLO"
#define SSID_PASSWORD "@@lucas@@"

#define PressaoaNivelDoMar_HPA (1013.25)

float cont = 0,
      cont2 = -1100000,
      pres = 0,
      temp = 0,
      umid = 0;

int chuv = 0;

ThingerESP8266 thing(USERNAME, DEVICE_ID, DEVICE_CREDENTIAL);

void setup()
{
  //Serial.begin(9600);
  pinMode(D5, INPUT);

  bme.begin(0x76);

  thing.add_wifi(SSID, SSID_PASSWORD);

  // resource output example (i.e. reading a sensor value)
  thing["parametros"] >> [](pson & out) {
    out["Chuv"] = chuv;
    out["Pres"] = pres;
    out["Temp"] = temp;
    out["Umid"] = umid;

  };
  thing["Alt"] >> outputValue(bme.readAltitude(PressaoaNivelDoMar_HPA));

}

void loop()
{

  // leitura a cada 20 segundos

  if (millis() - cont > 20000) {

    // mediçao da temperatura
    pres = 0;
    temp = 0;
    umid = 0;

    for (int i = 0; i <= 124; i++) {

      pres = pres + bme.readPressure();
      temp = temp + bme.readTemperature();
      umid = umid + bme.readHumidity();
      delay(25);
    }

    pres = pres / 12500,
    temp = temp / 125,
    umid = umid / 125;
   
    // mediçao da chuva
    int pino = digitalRead(D5);
    if (pino == 0) {
      chuv = 1;
    }
    else {
      chuv = 0;
    }

    cont = millis();
    thing.handle();
    /*Serial.println(pres);
      Serial.println(temp);
      Serial.println(umid);*/
  }


  // gravacao no banco de dados a cada 15 minutos

  if (millis() - cont2 > 1200000) {
    thing.write_bucket("teste", "parametros");

    cont2 = millis();

  }

}
