#include <DHT.h>
// Reception commande
String commande = "";
String commande_precedente = "";

// Gestion du temps
unsigned long t0 = 0;
unsigned long intervalle = 0;

// Capteur DHT11
#define DHTPIN 2     // Pin du capteur DHT11
#define DHTTYPE DHT11   // Type de capteur DHT11
DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  // Initialisation des pins
  pinMode(LED_RED, OUTPUT);
  pinMode(LED_GREEN, OUTPUT);
  pinMode(BUZZER, OUTPUT);
  // Initialisation du capteur DHT11
  dht.begin();
}

void loop() {
  // Réception commande (alerte en cas de risque)
  commande = Serial.readString();
  commande.trim();
  delay(10);

  if (commande.length() <= 0 ){
    commande = commande_precedente;
  }

  if (commande == "ASTHME"){
    // Allumer la LED rouge 
    digitalWrite(LED_RED, HIGH);
    // Activer le buzzer
    digitalWrite(BUZZER, HIGH);
    // Eteindre la LED verte
    digitalWrite(LED_GREEN, LOW);
    commande_precedente = commande;
  }
  else{  // NO RISK
    // Allumer la LED verte 
    digitalWrite(LED_GREEN, HIGH);
    // Eteindre la LED rouge
    digitalWrite(LED_RED, LOW);
    // Désactiver le buzzer
    digitalWrite(BUZZER, LOW);
    commande_precedente = commande;
  }

  // A chaque intervalle de 60s
  intervalle = millis() - t0;
  if (intervalle >= 60000){
    t0 = millis();
    // Lecture temperature et humidite DHT11 
    float humidite = dht.readHumidity();
    float temperature = dht.readTemperature();
    // Envoyer les mesures vers la passerelle via Serial.println()
    Serial.println("#" + String(humidite) + "," + String(temperature));
  }
}
