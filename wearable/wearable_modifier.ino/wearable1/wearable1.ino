// Inclure la bibliothèque DHT11
#include <DHT.h>

// Définir les paramètres du capteurs
#define DHTPIN    2     // Pin du capteur DHT11
#define DHTTYPE   DHT11    // Type de capteur DHT11
DHT dht(DHTPIN, DHTTYPE);

// Reception commande
String commande = "";
String commande_precedente = "";

// Gestion du temps
unsigned long t0 = 0;
unsigned long intervalle = 0;

// Créer un objet de type DHT
DHT dht11(DHTPIN, DHTTYPE);

void setup() {
  dht.begin();
  Serial.begin(9600);
}
void loop(){
  // A chaque intervalle de 60s
  intervalle = millis() - t0;
  if (intervalle >= 60000){
    t0 = millis();
    // Lecture temperature et humidite DHT11 
    float humidite = dht.readHumidity();
    float temperature = dht.readTemperature();
  
    if (isnan(temperature) || isnan(humidite)) {
      Serial.println("Failed to read from DHT sensor");
      delay(5000);
      return;
      }
      // Envoyer les mesures vers la passerelle via Serial.println()
      Serial.println("#" + String(humidite) + "," + String(temperature));
}
}
