# chatbot.py
import chainlit as cl
from app import queen_fairy, config
from agents import Runner

@cl.on_chat_start
async def on_chat_start():
    await cl.Message(
        content="👑 Welcome to the Child Welfare Assistant!\n\nPlease describe your concern:\n- Health 🏥\n- Education 📚\n- Protection 🛡️\n- Nutrition 🍎"
    ).send()

@cl.on_message
async def on_message(message: cl.Message):
    if message and message.content:
        # 🛠️ Show processing message
        await cl.Message(content="✨ Processing your request...").send()

        # ✅ Synchronous execution of the agent
        result = Runner.run_sync(
            queen_fairy,
            input=message.content,
            run_config=config
        )

        # 📨 Send the result back to the user
        await cl.Message(content=result.final_output).send()
