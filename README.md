
Child Welfare AI Assistant:
**************************
This project is a multi-agent AI assistant for child welfare, built using the OpenAI Agent SDK, Gemini API, and Chainlit for UI
:

🧱 Project Structure Overview

🔹 1. queen_fairy (Main Agent)

Type: Agent

Role: Main routing agent.

Function: Receives user input (like "health", "education", etc.) and routes it to the correct sub-agent (aka caring fairy).

Key Feature: Uses handoffs to connect to 4 sub-agents.

🔹 2. Sub-Agents (Caring Fairies)
Each sub-agent has a focused role based on a child's specific welfare need:

🧚‍♀️ caring_fairy_health

Role: Child health.

Instructions: Talks about vaccines, treatment, and health care.

UNICEF Strategy: Health supplies, immunization, and health worker training.

Current Status: Must provide a real-world 2025 health update from UNICEF or global data.

🧚‍♀️ caring_fairy_education

Role: Child education.

Instructions: Ensures school attendance and quality learning.

UNICEF Strategy: Improve access, train teachers.

Current Status: Gives a brief 2025 update on education globally or via UNICEF.

🧚‍♀️ caring_fairy_safeguard

Role: Child protection.

Instructions: Prevent abuse, labor, and exploitation.

UNICEF Strategy: Legal support and rights advocacy.

Current Status: Summarizes child protection globally in 2025.

🧚‍♀️ caring_fairy_nourishing

Role: Child nutrition.

Instructions: Ensures children receive proper nutrition and avoids malnutrition.

UNICEF Strategy: Feeding programs, food aid, awareness.

Current Status: Gives a real-time 2025 nutrition update with impact from UNICEF.

🔹 3. RunConfig → config

Type: RunConfig

Purpose: Defines model provider, whether tracing is on, etc.

Your Setup:

Uses OpenAIChatCompletionsModel with gemini-2.0-flash

Disables tracing

Config is passed to the Runner.

🔹 4. Runner.run_sync(...)

Module: agents.Runner

Role: Executes agent logic.

Used In: chatbot.py

Function: Calls queen_fairy with user input and handles internal routing + response building.

🔹 5. chatbot.py (Chainlit UI)

Framework: Chainlit

Events:
*******

@cl.on_chat_start: Greets the user.

@cl.on_message: Processes user input → runs queen_fairy via Runner.run_sync() → shows result.

Output: Sends back the result from the selected sub-agent.


https://github.com/user-attachments/assets/eaa1f242-edb0-46d7-9171-b712ec3bfcb6
<img width="1612" height="904" alt="code-run command" src="https://github.com/user-attachments/assets/ab7140c1-a1a2-429c-849e-c8310b06134e" />
<img width="1611" height="905" alt="Health" src="https://github.com/user-attachments/assets/723bc395-4f0a-44d3-8b52-d254135dc205" />
<img width="1611" height="907" alt="Education" src="https://github.com/user-attachments/assets/0ed813d1-177a-43d9-b33e-b58552f4497a" />
<img width="1608" height="909" alt="Protection" src="https://github.com/user-attachments/assets/f2e81c2f-3e18-4fa8-b633-bcd14a430ee0" />
<img width="1615" height="906" alt="Nutrition" src="https://github.com/user-attachments/assets/e39bb27a-9c6f-44f3-8c3b-e4cf638d88d3" />




















