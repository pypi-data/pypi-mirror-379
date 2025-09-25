from optycode_sdk import OptycodeAPI

client = OptycodeAPI(auth_token="test_token")
response = client.send_model_data_async(question="sdk_legit_test", answer="sdk_legit_answer", model_id=2)
# response = client.send_model_data(question="sdk_test_normal_new", answer="sdk_test_answer_normal_new", model_id=2)
print(response)