# Prompt Injection CTF

## Overview:

This is a local, Ollama-powered prompt injection CTF that has 3 levels for intrepid security researchers to crack:

**Level 1**: Basic defenses; nothing you can't trick with creative jailbreaking prompts.

**Level 2**: Stronger defenses and a specialized use case. Persistence is key; keep trying and something's bound to break eventually.

**Level 3**: The hardest level. It features RAG retrieval and a stronger system prompt. 


**Note**: For level 3, the payload delivery depends heavily on how the LLM weighs retrieved context versus its system prompt. If your injection fails, try different placement, formatting, or wording in your payload. Sometimes, even confidently sending it a fake flag may cause its helpful nature to kick in and correct you.

Your goal is to get the flag from the LLM in each challenge. Use all the tricks in your toolbox. If you get stuck and feel like giving up, you can always inspect the source code, though I encourage you to try your best before looking at the answers. 


In case you get confused during setup, the directory tree looks like this:

```
├── Prompt_Injection_CTF/
│   ├── level1/
│   │   ├── level1.py
│   │   └── Modelfile.one
│   ├── level2/
│   │   └── level2.py
│   │   └── Modelfile.two
│   ├── level3/
│   │   └── level3.py
│   │   └── Modelfile.three
│   ├── requirements.txt
│   └── README.md
│   └── LICENSE
```
## Prerequisites:

In order to successfully run this challenge on your device, you must have a properly configured Ollama installation and at least 10GB of free space on your storage device for the LLMs and all associated software.


## Setup & Installation:

1. Clone the repository and ``cd`` into it.
2. Install all required libraries using ```pip install -r requirements.txt```
3. Pull the ollama model required: ```ollama pull llama3.2:3b```
4. Create the custom bots for levels 1, 2, and 3. Run each command separately: 
- ```ollama create level1 -f level1/Modelfile.one```
- ```ollama create level2 -f level2/Modelfile.two``` 
- ```ollama create level3 -f level3/Modelfile.three```
5. Run ```python level1/level1.py``` and get to hacking!
6. When you're ready to move on to the next level, run: ```python level2/level2.py``` or ```python level3/level3.py``` 


## Disclaimer:

AI is unpredictable. You may have to try several times to successfully prompt inject it. Do not feel discouraged if you are unable to do so after a few tries. If necessary, adjust the system prompt or tweak the temperature settings. This is not cheating; corporate environments change models and LLM settings quite often.

This is a challenge developed using entirely open source and free software. It is not meant to aid anyone attempting illegal hacking. The developer does not condone, endorse, or claim responsibility for any illegal actions performed with this code and openly discourages it. 

