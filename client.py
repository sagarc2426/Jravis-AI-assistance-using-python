import cohere

co = cohere.ClientV2("<ADD YOUR API KEY>")
response = co.chat(
    model="command-r-plus", 
    messages=[
    {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud"},
    {"role": "user", "content": "what is coding"}
    ]
)

print(response.message.content[0].text)


