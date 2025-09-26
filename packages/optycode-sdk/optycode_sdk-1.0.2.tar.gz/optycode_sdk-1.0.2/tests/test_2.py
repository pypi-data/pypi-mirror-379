from optycode_sdk import OptycodeAPI

client = OptycodeAPI(auth_token="")

response = client.send_model_data_async(question="a", answer="b", model_id=2)
