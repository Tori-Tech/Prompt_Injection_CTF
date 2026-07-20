import ollama 



#starts the AI chat
def initialize_AI():
        #define Ollama model
        modelName = "level2"

        prompt = True
       #this part keeps the chat running
        while prompt == True:
            #user prompt
            user_prompt = input("Ask the AI anything: ")
            
            if user_prompt == "/bye":
                return 0 
            else: 
                print("\n--- Response ---")
        
            
                # request a streaming response from the local model
                stream = ollama.chat(
                model=modelName,
                    messages=[{'role': 'user', 'content': user_prompt}],
                    stream=True,
                )

                #print tokens as they arrive
                for chunk in stream:
                    print(chunk['message']['content'], end='', flush=True)
                print("\n")



  


#main loop
print("Welcome to level 2 of the Prompt Injection CTF. Just like with level 1, continue to use prompt injection to get the flag from the LLM.\n")
print("Remember: Flags look like: FLAG{xxxxxxxx}\n")
print("Type '/bye' to quit chatting with the model.\n")

proceed = True
while proceed == True:
        initialize_AI()
        flag = input("What is the final flag?")
        if flag == "FLAG{TH1S_0N3_W4S_HARD3R!}":
            print("Congratulations! You solved the challenge!")
            proceed = False
        else:
            print("That's not it, sorry. Try again.")
