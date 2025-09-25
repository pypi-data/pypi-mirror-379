from optycode_sdk import OptycodeAPI

client = OptycodeAPI(auth_token=your_token)

response = client.send_model_data_async(question=user_question, answer=model_answer, model_id=your_model_id)
