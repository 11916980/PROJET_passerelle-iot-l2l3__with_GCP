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

    
    # Query_hypertension 
    query_hypertension = """
     SELECT
       *
     FROM
       ML.PREDICT(MODEL `ml_models_jc2.hypertension_prediction`, (
       SELECT
          CAST(humidite AS FLOAT64) AS humidity,
          CAST(temperature AS FLOAT64) AS temperature,
          EXTRACT(MONTH FROM timestamp) as month
          FROM
            `dataset_iot_jc2.temperature_humidite`
          ORDER BY
            timestamp DESC
          LIMIT 10
       ))
    """
    
    query_job_hypertension = bq_client.query(query_hypertension)
    print()

    predict_hypertension_daily_emergency = 0
    for row in query_job_hypertension:
      print(row)
      if row[0] > predict_hypertension_daily_emergency :
        predict_hypertension_daily_emergency = row[0]
    print(f"predict_hypertension_daily_emergency : {predict_hypertension_daily_emergency}")
    
    # Cas : HYPERTENSION
    mean_hypertension_daily_emergency = 35.81
    hypertension_prescription = None
    if predict_hypertension_daily_emergency  > mean_hypertension_daily_emergency  :
      hypertension_prescription = "HYPERTENSION RISK EXIST : take your inhaler with you, avoid physical exertion, stay in ventilated spaces."
    print(f"hypertension_prescription : {hypertension_prescription}")
    
    # Query_AVC
    query_cerebrovascular = """
     SELECT
       *
     FROM
       ML.PREDICT(MODEL `ml_models_jc2.cerebrovascular_prediction`, (
       SELECT
          CAST(humidite AS FLOAT64) AS humidity,
          CAST(temperature AS FLOAT64) AS temperature,
          EXTRACT(MONTH FROM timestamp) as month
          FROM
            `dataset_iot_jc2.temperature_humidite`
          ORDER BY
            timestamp DESC
          LIMIT 10
       ))
    """
    
    query_job_cerebrovascular = bq_client.query(query_cerebrovascular)
    print()

    predict_cerebrovascular_daily_emergency = 0
    
    for row in query_job_cerebrovascular:
      print(row)
      if row[0] > predict_cerebrovascular_daily_emergency :
        predict_cerebrovascular_daily_emergency = row[0]
    print(f"predict_cerebrovascular_daily_emergency : {predict_cerebrovascular_daily_emergency}")
    
    # Cas : AVC
    mean_cerebrovascular_daily_emergency = 75.20
    cerebrovascular_prescription = None
    if predict_cerebrovascular_daily_emergency  > mean_cerebrovascular_daily_emergency  :
      cerebrovascular_prescription = "AVC RISK EXIST : take your inhaler with you, avoid physical exertion, stay in ventilated spaces."
    print(f"cerebrovascular_prescription : {cerebrovascular_prescription}")
    # Mettre le mot clé AVC dans la prescription à envoyer
    
    # Formatting command
    command = ""
    if cerebrovascular_prescription:
      command = cerebrovascular_prescription
    
    # Sending command
    print("Sending command to device")
    iot_client = iot_v1.DeviceManagerClient()
    device_path = iot_client.device_path(project_id, cloud_region, registry_id, device_id)

    return iot_client.send_command_to_device(
       request={"name": device_path, "binary_data": command.encode("utf-8")}
    )