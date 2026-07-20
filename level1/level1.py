import ollama 


#starts the AI chat
def initialize_AI():
        #this is the name of the Ollama model
        modelName = "level1"

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
print("Welcome to level 1 of the Prompt Injection CTF. The challenge is simple: Use prompt injection to get the flag from the LLM.\n")
print("Flags look like: FLAG{xxxxxxxx}\n")
print("Type '/bye' to quit chatting with the model.\n")
proceed = True
while proceed == True:
        initialize_AI()

        #checks for user input
        flag = input("What is the flag?")
        if flag is not None:
            if flag == "FLAG{Y0UR_F1ST_PR0M7T_1NJ3CT10N!}":
                   print("Congratulations! You solved the challenge!")
                   proceed = False
               
            else:
                print("That's not it, sorry. Try again.")
        else:
             print("Error. Please try again.")
