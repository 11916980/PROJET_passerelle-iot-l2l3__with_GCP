// A COMPLETER...


// Reception commande
String commande = "";
String commande_precedente = "";

// Gestion du temps
unsigned long t0 = 0;
unsigned long intervalle = 0;

void setup() {
  Serial.begin(9600);
  // A compléter
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
    // A COMPLETER...
    // Allumer la LED rouge 
    // Activer le buzzer
    // Eteindre la LED verte
    commande_precedente = commande;
  }
  else{  // NO RISK
    // A COMPLETER...
    // Allumer la LED verte 
    // Eteindre la LED rouge
    // Désactiver le buzzer
    commande_precedente = commande;
  }

  // A chaque intervalle de 60s
  intervalle = millis() - t0;
  if (intervalle >= 60000){
    t0 = millis();
    // A COMPLETER...
    // Lecture temperature et humidite DHT11 
    // Envoyer les mesures vers la passerelle via Serial.println()
  }
}
