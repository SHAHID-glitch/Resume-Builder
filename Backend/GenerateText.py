from openai import OpenAI

client=OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key="",
)

def Describe(Prompt):
    if Prompt == "":
        return "No Prompt received"
    
    completion=client.chat.completions.create(
        extra_headers={
            "HTTP-Referer": "https://nishantksingh0.github.io/resume-builder-web-application/", 
            "X-Title": "Resume Builder Web Application",
        },
        extra_body={},
        model="deepseek/deepseek-r1:free",
        messages=[
            {
            "role": "user",
            "content": Prompt
            }
        ]
    )
    return completion.choices[0].message.content
