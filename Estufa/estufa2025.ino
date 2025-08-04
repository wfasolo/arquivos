// ESP32 Dev Module
#include <ThingerESP8266.h>

#define USERNAME "wfasolo"
#define DEVICE_ID "Estufa"
#define DEVICE_CREDENTIAL "@#lucas"
ThingerESP8266 thing(USERNAME, DEVICE_ID, DEVICE_CREDENTIAL);

// Constantes do hardware
const int PWM_PIN = 3;  // Pino com suporte a PWM (ESP32)

// Constantes do NTC
const float NTC_BETA = 3950.0;         // Coeficiente Beta
const float NTC_R0 = 5000.0;           // Resistência a 25°C (298.15K)
const float NTC_T0 = 298.15;           // 25°C em Kelvin
const float SERIES_RESISTOR = 4700.0;  // Resistor em série
const float ADC_VOLTAGE = 3.3;         // Tensão de alimentação do ADC
const int ADC_RESOLUTION = 4095;       // Resolução do ADC, 12-bit = 4095

// Variáveis de controle, agora não são mais constantes
float SETPOINT = 35.0;
float Kc = 10.0;
float Pc = 5.0;
float KP = 6.0;
float KI = 2.4;
float KD = 3.75;

// Variáveis de estado do sistema
float currentTemp = 0.0;
float prevTemp = 0.0;
float integral = 0.0;
float proportionalTerm = 0.0;
float derivativeTerm = 0.0;
int outputPID = 0;
unsigned long lastLoopTime = 0;

void setup() {
  Serial.begin(9600);

  pinMode(PWM_PIN, OUTPUT);

  // Configuração do PWM para ESP32
  // ledcSetup(0, 5000, 10);
  // ledcAttachPin(PWM_PIN, 0);

  // Inicialização de variáveis de tempo
  lastLoopTime = millis();

  // Lê a temperatura inicial para evitar um grande "kick" no derivativo
  currentTemp = readTemperature();
  prevTemp = currentTemp;

  // Conexão Wi-Fi
  thing.add_wifi("LAB", "@@lucas@@");

  // Recurso para enviar dados de monitoramento para o Thinger.io
  thing["Parametros"] >> [](pson& out) {
    out["Temp"] = currentTemp;
    out["PWM"] = outputPID;
    out["P"] = proportionalTerm;
    out["I"] = integral;
    out["D"] = derivativeTerm;
  };

  // Recurso para receber e enviar dados de controle (PID) do Thinger.io
  thing["PID"] << [](pson& in) {
    if (in.is_empty()) {
      // Envia os valores atuais para a plataforma na inicialização
      in["Setpoint"] = SETPOINT;
      in["Kc"] = Kc;
      in["Pc"] = Pc;
    } else {
      // Atualiza as variáveis com os novos valores da plataforma
      SETPOINT = in["Setpoint"];
      Kc = in["Kc"];
      Pc = in["Pc"];
    }
  };
}

void loop() {
  thing.handle();
  unsigned long now = millis();

  // Garante que o cálculo PID seja feito em intervalos regulares
  if ((now - lastLoopTime) >= 1000) {
    calculatePID();
    lastLoopTime = now;
  }
}

// Funções de apoio

float readTemperature() {
  int adcValue = 0;
  const int numSamples = 5;

  for (int i = 0; i < numSamples; i++) {
    adcValue += analogRead(A0);
    delay(5);
  }
  adcValue /= numSamples;

  float vOut = (static_cast<float>(adcValue) / ADC_RESOLUTION) * ADC_VOLTAGE;
  float rNtc = SERIES_RESISTOR * (ADC_VOLTAGE - vOut) / vOut;
  float tempK = 1.0 / (1.0 / NTC_T0 + (log(rNtc / NTC_R0) / NTC_BETA));

  return tempK - 273.15;
}

void calculatePID() {
  float dt = (millis() - lastLoopTime) / 1000.0;
  currentTemp = readTemperature();
  float error = SETPOINT - currentTemp;

  if (abs(error) <= 0.1) return;

  KP = 0.6 * Kc;
  KI = 1.2 * Kc / Pc;
  KD = 0.075 * Kc * Pc;

  // Termo Proporcional
  proportionalTerm = KP * error;

  // Termo Integral
  integral += KI * error * dt;
  integral = constrain(integral, 0, 1023);

  // Termo Derivativo
  derivativeTerm = KD * (currentTemp - prevTemp) / dt;
  prevTemp = currentTemp;

  // Soma dos termos para a saída total do PID
  outputPID = proportionalTerm + integral + derivativeTerm;
  outputPID = constrain(outputPID, 0, 1023);

  //ledcWrite(0, outputPID);
  analogWrite(PWM_PIN,outputPID);

  // Depuração no Serial
  Serial.print("Temp: ");
  Serial.print(currentTemp);
  Serial.print(" °C | PID: ");
  Serial.println(outputPID);
}
