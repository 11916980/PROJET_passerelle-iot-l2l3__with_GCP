import functions_framework
import base64
from google.cloud import bigquery
from google.cloud import iot_v1

@functions_framework.cloud_event
def risk_assessment(cloud_event):
    # Parameters - Cloud IoT Core (à indiquer manuellement)
    project_id = "dit-m1ia-nov22"
    cloud_region = "us-central1"
    registry_id = "registre-prenom"  # remplacer prenom par votre propre prenom
    device_id = "hum-temp-device"
    
    # Pub/Sub data : get message from cloud scheduler
    schedule_message = base64.b64decode(cloud_event.data["message"]["data"]).decode("utf-8")
    print(f"Receiving message from Cloud Scheduler : {schedule_message}")
    
    # Predict based on the last 12 hours recorded sensor data (temperature, humidity, month)
    bq_client = bigquery.Client()
    # NB: dans la requête suivante, remplacer prenom par le prenom que vous indiqué dans BigQuery
    query_asthme = """
     SELECT
       *
     FROM
       ML.PREDICT(MODEL `ml_models_prenom.asthme_prediction`, (
       SELECT
          CAST(humidite AS FLOAT64) AS humidity,
          CAST(temperature AS FLOAT64) AS temperature,
          EXTRACT(MONTH FROM timestamp) as month
          FROM
            `dataset_iot_prenom.temperature_humidite`
          ORDER BY
            timestamp DESC
          LIMIT 10
       ))
    """
  
    query_job_asthme = bq_client.query(query_asthme)
    print()

    predict_asthme_daily_emergency = 0
    for row in query_job_asthme:
      print(row)
      if row[0] > predict_asthme_daily_emergency :
        predict_asthme_daily_emergency = row[0]
    print(f"predict_asthme_daily_emergency : {predict_asthme_daily_emergency}")

    # Give prescription (NO RISK, RISK EXIST) based on rules engine
    # Cas ASTHME
    mean_asthme_daily_emergency = 5.62
    asthme_prescription = None
    if predict_asthme_daily_emergency  > mean_asthme_daily_emergency  :
      asthme_prescription = "ASTHME RISK EXIST : take your inhaler with you, avoid physical exertion, stay in ventilated spaces."
    print(f"asthme_prescription : {asthme_prescription}")
    # A COMPLETER...
    # Cas : HYPERTENSION
    # Mettre le mot clé HYPERTENSION dans la prescription à envoyer
    # Cas AVC
    # Mettre le mot clé AVC dans la prescription à envoyer
    
    # Formatting command
    command = ""
    if asthme_prescription:
      command = asthme_prescription
    
    # Sending command
    print("Sending command to device")
    iot_client = iot_v1.DeviceManagerClient()
    device_path = iot_client.device_path(project_id, cloud_region, registry_id, device_id)

    return iot_client.send_command_to_device(
       request={"name": device_path, "binary_data": command.encode("utf-8")}
    )