// ESP32 Dev Module

#include <ThingerESP8266.h>

#define USERNAME       "wfasolo"
#define DEVICE_ID      "Estufa"
#define DEVICE_CREDENTIAL  "@#lucas"

ThingerESP8266 thing(USERNAME, DEVICE_ID, DEVICE_CREDENTIAL);

// Constantes do hardware
const int PWM_PIN = 3;  // Pino com suporte a PWM (ESP32)

// Constantes do NTC
const float NTC_BETA        = 3950.0;   // Coeficiente Beta
const float NTC_R0          = 5000.0;   // Resistência a 25°C (298.15K)
const float NTC_T0          = 298.15;   // 25°C em Kelvin
const float SERIES_RESISTOR = 4700.0;   // Resistor em série
const float ADC_VOLTAGE     = 3.3;      // Tensão de alimentação do ADC
const int   ADC_RESOLUTION  = 4095;     // Resolução do ADC, 12-bit = 4095

// Variáveis de controle, agora não são mais constantes
float SETPOINT = 35.0;
float Kc       = 10.0;
float Pc       = 5.0;
float KP       = 6.0;
float KI       = 2.4;
float KD       = 3.75;

// Variáveis de estado do sistema
float currentTemp       = 0.0;
float prevTemp          = 0.0;
float integral          = 0.0;
float proportionalTerm  = 0.0;
float derivativeTerm    = 0.0;
int   outputPID         = 0;
unsigned long lastLoopTime = 0;

// Declaração da nova função
void updateKcPc(float error);

void setup() {
  Serial.begin(9600);
  pinMode(PWM_PIN, OUTPUT);

  // Inicialização de variáveis de tempo
  lastLoopTime = millis();

  // Lê a temperatura inicial para evitar um grande “kick” no derivativo
  currentTemp = readTemperature();
  prevTemp    = currentTemp;

  // Conexão Wi-Fi
  thing.add_wifi("LAB", "@@lucas@@");

  // Recurso para enviar dados de monitoramento para o Thinger.io
  thing["Parametros"] >> [](pson& out) {
    out["Temp"] = currentTemp;
    out["PWM"]  = outputPID;
    out["P"]    = proportionalTerm;
    out["I"]    = integral;
    out["D"]    = derivativeTerm;
  };

  // Recurso para receber e enviar dados de controle (PID) do Thinger.io
  thing["PID"] << [](pson& in) {
    if (in.is_empty()) {
      in["Setpoint"] = SETPOINT;
      in["Kc"]       = Kc;
      in["Pc"]       = Pc;
    } else {
      SETPOINT = in["Setpoint"];
      Kc       = in["Kc"];
      Pc       = in["Pc"];
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

// Leitura de temperatura via NTC
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

// Cálculo do PID, com atualização de Kc e Pc a cada cruzamento do setpoint
void calculatePID() {
  float dt = (millis() - lastLoopTime) / 1000.0;
  currentTemp = readTemperature();
  float error = SETPOINT - currentTemp;

  // Atualiza Kc e Pc observando o maior deltaT e seu instante até o próximo cruzamento
  updateKcPc(error);

  if (abs(error) <= 0.1) return;

  // Recalcula ganhos com base em Kc e Pc atualizados
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
  prevTemp       = currentTemp;

  // Saída total do PID
  outputPID = proportionalTerm + integral + derivativeTerm;
  outputPID = constrain(outputPID, 0, 1023);

  analogWrite(PWM_PIN, outputPID);

  // Depuração no Serial
  Serial.print("Temp: ");
  Serial.print(currentTemp);
  Serial.print(" °C | PID: ");
  Serial.println(outputPID);
}

// Implementação da função que redefine Kc e Pc a cada cruzamento do setpoint
void updateKcPc(float error) {
  static float lastError      = 0.0;
  static float maxError       = 0.0;
  static unsigned long tStart = 0;
  static unsigned long tMax   = 0;
  static bool firstCycle      = true;

  unsigned long now = millis();

  // Detecta cruzamento para cima ou para baixo
  if ((error > 0 && lastError <= 0) || (error < 0 && lastError >= 0)) {
    if (!firstCycle) {
      // Ajusta Kc e Pc baseados no ciclo anterior
      Kc = maxError;
      Pc = (tMax - tStart) / 1000.0;  // converte ms para s
    }
    firstCycle = false;
    // Reinicia para o novo ciclo
    tStart   = now;
    maxError = 0.0;
    tMax     = now;
  }

  // Acompanha o ΔT máximo (em módulo) e registra quando ocorreu
  if (abs(error) > maxError) {
    maxError = abs(error);
    tMax     = now;
  }

  lastError = error;
}
