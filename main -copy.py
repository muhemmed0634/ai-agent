from google import genai
import rich

rich.print(r"""[green]
   _____  .___      _____    ___________________ __________________
  /  _  \ |   |    /  _  \  /  _____/\_   _____/ \      \__    ___/
 /  /_\  \|   |   /  /_\  \/   \  ___ |    __)_  /   |   \|    |   
/    |    \   |  /    |    \    \_\  \|        \/    |    \    |   
\____|__  /___|  \____|__  /\______  /_______  /\____|__  /____|   
        \/               \/        \/        \/         \/         
                           [/green]                                        
                                             [red] 1.0.0[/red]
                                              [blue]powered by genAI[/blue]
                                              [magenta]maked by muhemmed[/magenta]   
""")

client = genai.Client(api_key="enter api key")
chat = client.chats.create(model="gemini-3.5-flash")

while True:
    prompt = input("YOU : ")
    if prompt.lower() == "exit":
        break
    response = chat.send_message(prompt)
    rich.print(f"[blue]AI : [/blue]{response.text}")
