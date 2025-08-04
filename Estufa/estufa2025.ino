#include <ThingerESP32.h>

#define USERNAME "wfasolo"
#define DEVICE_ID "Estufa"
#define DEVICE_CREDENTIAL "@#lucas"

ThingerESP32 thing(USERNAME, DEVICE_ID, DEVICE_CREDENTIAL);

// --- Constantes do Hardware e Controle ---
const int NTC_PIN = 36;
const int PWM_PIN = 32;
const int PWM_CHANNEL = 0;
const int PWM_RESOLUTION = 10;
const int PWM_MAX_DUTY = (1 << PWM_RESOLUTION) - 1;
const unsigned long SAMPLE_TIME_MS = 1000;
const float HYSTERESIS_TEMP = 0.2; // Histerese para detecção de pico/vale

// --- Constantes do NTC ---
const float NTC_BETA = 3950.0;
const float NTC_R0 = 5000.0;
const float NTC_T0 = 298.15;
const float SERIES_RESISTOR = 4700.0;
const float ADC_VOLTAGE = 3.3;
const int ADC_RESOLUTION = 4095;

// --- Variáveis de Controle e Estado ---
float SETPOINT = 35.0;
float Kc = 10.0; // Agora representa a amplitude da oscilação, será auto-ajustado
float Pc = 5.0;  // Agora representa o período da oscilação, será auto-ajustado
float KP, KI, KD;

float currentTemp = 0.0;
float prevTemp = 0.0;
float integral = 0.0;
float outputPID = 0.0;
unsigned long lastLoopTime = 0;

// --- Máquina de Estados para o Auto-Tuner ---
enum AutoTunerState { STABLE, TUNING };
AutoTunerState tunerState = STABLE;

// Variáveis para o processo de sintonia
bool lookingForPeak = true;
float lastPeakTemp = -100;
float lastValleyTemp = 100;
unsigned long timeOfLastPeak = 0;
unsigned long timeOfSetpointCross = 0;
int peakCount = 0;

// Declaração de funções
void updatePIDConstants();
float readTemperature();
void calculatePID();
void handleAutoTuner();

void setup() {
    Serial.begin(115200);

    ledcSetup(PWM_CHANNEL, 5000, PWM_RESOLUTION);
    ledcAttachPin(PWM_PIN, PWM_CHANNEL);

    currentTemp = readTemperature();
    prevTemp = currentTemp;

    updatePIDConstants(); // Calcula os valores iniciais de KP, KI, KD

    thing.add_wifi("LAB", "@@lucas@@");

    // Recurso para monitorar os parâmetros principais
    thing["Parametros"] >> [](pson& out) {
        out["Temp"] = currentTemp;
        out["Setpoint"] = SETPOINT;
        out["PWM"] = outputPID;
        out["TunerState"] = (tunerState == STABLE) ? "ESTAVEL" : "SINTONIZANDO";
    };

    // Recurso para ajustar o Setpoint e observar os parâmetros auto-sintonizados
    thing["PID_Control"] << [](pson& in) {
        if (!in.is_empty() && in.has("Setpoint")) {
            // Permite que o usuário defina um novo Setpoint
            SETPOINT = in["Setpoint"];
        }
        // Envia os valores atuais (incluindo os auto-sintonizados)
        in["Setpoint"] = SETPOINT;
        in["Kc_amplitude"] = Kc;
        in["Pc_periodo"] = Pc;
        in["KP"] = KP;
        in["KI"] = KI;
        in["KD"] = KD;
    };
    
    lastLoopTime = millis();
}

void loop() {
    thing.handle();
    unsigned long now = millis();

    if ((now - lastLoopTime) >= SAMPLE_TIME_MS) {
        prevTemp = currentTemp;
        currentTemp = readTemperature();

        if (currentTemp <= -999) { // Proteção contra falha do sensor
             ledcWrite(PWM_CHANNEL, 0); // Desliga o aquecedor
             return;
        }

        handleAutoTuner(); // Executa a lógica do auto-sintonizador
        calculatePID();    // Calcula a saída do PID

        lastLoopTime = now;
    }
}

void handleAutoTuner() {
    switch (tunerState) {
        case STABLE:
            // Se a temperatura cruzar o setpoint, inicia o processo de sintonia
            if ((prevTemp < SETPOINT && currentTemp >= SETPOINT) || 
                (prevTemp > SETPOINT && currentTemp <= SETPOINT)) {
                
                Serial.println("Cruzou o Setpoint! Iniciando modo de SINTONIA.");
                tunerState = TUNING;
                timeOfSetpointCross = millis();
                peakCount = 0;
                lookingForPeak = (currentTemp > prevTemp); // Se está subindo, procura pico
            }
            break;

        case TUNING:
            // Lógica para encontrar picos e vales
            if (lookingForPeak) {
                if (currentTemp > lastPeakTemp) {
                    lastPeakTemp = currentTemp; // Atualiza o valor do pico
                }
                // Considera que encontrou o pico se a temperatura cair o suficiente
                if (currentTemp < lastPeakTemp - HYSTERESIS_TEMP) {
                    Serial.printf("Pico encontrado: %.2f C\n", lastPeakTemp);
                    peakCount++;
                    if (peakCount == 1) { // Primeiro pico
                        timeOfLastPeak = millis();
                    } else if (peakCount == 2) { // Segundo pico, temos uma oscilação completa
                        // --- CÁLCULO DOS NOVOS PARÂMETROS ---
                        Pc = (millis() - timeOfLastPeak) / 1000.0f; // Período em segundos
                        Kc = lastPeakTemp - lastValleyTemp;         // Amplitude

                        Serial.println("--- AUTO-SINTONIA COMPLETA ---");
                        Serial.printf("Novo Pc (período): %.2f s\n", Pc);
                        Serial.printf("Novo Kc (amplitude): %.2f C\n", Kc);
                        
                        updatePIDConstants(); // Atualiza Kp, Ki, Kd com os novos valores
                        
                        tunerState = STABLE; // Retorna ao modo estável
                        Serial.println("Retornando ao modo ESTAVEL.");
                        return; // Sai da função para usar os novos valores no próximo ciclo
                    }
                    lookingForPeak = false; // Agora procura um vale
                    lastValleyTemp = currentTemp; // Inicializa a busca pelo vale
                }
            } else { // lookingForValley
                if (currentTemp < lastValleyTemp) {
                    lastValleyTemp = currentTemp; // Atualiza o valor do vale
                }
                // Considera que encontrou o vale se a temperatura subir o suficiente
                if (currentTemp > lastValleyTemp + HYSTERESIS_TEMP) {
                    Serial.printf("Vale encontrado: %.2f C\n", lastValleyTemp);
                    lookingForPeak = true; // Agora procura um novo pico
                    lastPeakTemp = currentTemp; // Inicializa a busca pelo pico
                }
            }
            
            // Timeout: se ficar muito tempo sem conseguir sintonizar, desiste.
            if (millis() - timeOfSetpointCross > 30 * 60 * 1000) { // Timeout de 30 minutos
                Serial.println("Timeout do Auto-Tuner. Retornando ao modo ESTAVEL.");
                tunerState = STABLE;
            }
            break;
    }
}

void updatePIDConstants() {
    if (Pc <= 0) return; // Proteção contra divisão por zero
    KP = 0.6 * Kc;
    KI = (1.2 * Kc / Pc); // Para o cálculo discreto, Ki e Kd devem ser escalados pelo tempo de amostragem
    KD = (0.075 * Kc * Pc);
    
    Serial.println("Constantes PID atualizadas:");
    Serial.printf("KP: %.2f, KI: %.2f, KD: %.2f\n", KP, KI, KD);
}

void calculatePID() {
    float error = SETPOINT - currentTemp;
    float dt_sec = SAMPLE_TIME_MS / 1000.0f;

    // Termo Proporcional
    float proportionalTerm = KP * error;

    // Termo Integral com anti-windup
    integral += KI * error * dt_sec;
    integral = constrain(integral, -PWM_MAX_DUTY, PWM_MAX_DUTY); // Permitir integral negativo pode ajudar na recuperação de overshoot

    // Termo Derivativo (sobre a medição para evitar "derivative kick")
    float derivativeTerm = KD * (currentTemp - prevTemp) / dt_sec;
    
    outputPID = proportionalTerm + integral - derivativeTerm;
    outputPID = constrain(outputPID, 0, PWM_MAX_DUTY);

    ledcWrite(PWM_CHANNEL, (int)outputPID);

    // Depuração no Serial
    Serial.printf("Temp: %.2f C | Erro: %.2f | Saida PWM: %d\n", currentTemp, error, (int)outputPID);
}

// Implementação da função readTemperature omitida por brevidade (usar a versão corrigida da resposta anterior)
float readTemperature() {
    int adcValue = 0;
    const int numSamples = 10;
    for (int i = 0; i < numSamples; i++) {
        adcValue += analogRead(NTC_PIN);
        delay(2);
    }
    adcValue /= numSamples;
    if (adcValue == 0) return -999;
    float vOut = (static_cast<float>(adcValue) / ADC_RESOLUTION) * ADC_VOLTAGE;
    if (abs(ADC_VOLTAGE - vOut) < 1e-6) return -999; // Evita divisão por zero
    float rNtc = SERIES_RESISTOR * vOut / (ADC_VOLTAGE - vOut);
    if (rNtc <= 0) return -999;
    float tempK = 1.0 / (1.0 / NTC_T0 + (log(rNtc / NTC_R0) / NTC_BETA));
    return tempK - 273.15;
}
