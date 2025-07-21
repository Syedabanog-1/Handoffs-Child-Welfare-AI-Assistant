
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

@cl.on_chat_start: Greets the user.

@cl.on_message: Processes user input → runs queen_fairy via Runner.run_sync() → shows result.

Output: Sends back the result from the selected sub-agent.




https://github.com/user-attachments/assets/eaa1f242-edb0-46d7-9171-b712ec3bfcb6



https://github.com/user-attachments/assets/1c1b3b5e-fa42-4cf8-99a2-63515ea7ca6b



https://github.com/user-attachments/assets/4aec35d6-803d-41b1-9953-6e83dad0c9e0



https://github.com/user-attachments/assets/2c136e14-332a-432e-a87d-be33e45dd9ca



https://github.com/user-attachments/assets/c84009bd-a265-46a9-ba11-7efb40ffe516



https://github.com/user-attachments/assets/da4ac9e8-a92a-42e1-8f41-64b951f3a950















