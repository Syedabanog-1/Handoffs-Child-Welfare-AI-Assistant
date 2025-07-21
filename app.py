import os
from dotenv import load_dotenv
from agents import Agent, RunConfig, set_tracing_disabled, OpenAIChatCompletionsModel, AsyncOpenAI
from agents.extensions.models.litellm_model import LitellmModel

# 🌍 Load environment variables
load_dotenv()

# 🚫 Disable tracing (optional)
set_tracing_disabled(True)

# 🔐 Load Gemini API key
GEMINI_API_KEY = os.getenv("GOOGLE_API_KEY")

# ✅ Check if API key is loaded
if not GEMINI_API_KEY:
    raise ValueError("GOOGLE_API_KEY not found in environment variables.")
provider = AsyncOpenAI(
    base_url="https://generativelanguage.googleapis.com/v1beta/openai",
    api_key=GEMINI_API_KEY,

)
model = OpenAIChatCompletionsModel(
    openai_client=provider,
    model="gemini-2.0-flash"
)
config = RunConfig(
    model=model,
    model_provider=model,
    tracing_disabled=True
)


# ... [keep your existing imports and setup]

# caring_fairy1 - Health
caring_fairy_health = Agent(
    name="caring_fairy_health",
    model=model,
    instructions="""
You are caring_fairy_health responsible for child health.

1. Responsibility: Ensure children receive vaccinations, treatment for illnesses, and medical care.
2. UNICEF Strategy: Deliver health supplies, immunization, and train health workers.
3. Current Status: After describing duty and strategy, give a short, updated real-world summary (as of 2025) about child health from global or UNICEF sources. Be brief and informative.
"""
)

# caring_fairy2 - Education
caring_fairy_education= Agent(
    name="caring_fairy_education",
    model=model,
    instructions="""
You are caring_fairy_education responsible for child education.

1. Responsibility: Ensure every child attends school and receives quality education.
2. UNICEF Strategy: Improve access to education, learning materials, and teacher training.
3. Current Status: After explaining the role and strategy, give a short 2025-level summary on the current global status of child education using real data from UNICEF reports or global updates.
"""
)

# caring_fairy3 - Protection
caring_fairy_safeguard = Agent(
    name="caring_fairy_safeguard",
    model=model,
    instructions="""
You are caring_fairy_safeguard responsible for child protection.

1. Responsibility: Prevent child abuse, child labor, and exploitation.
2. UNICEF Strategy: Advocate for child rights and support legal frameworks.
3. Current Status: Conclude by giving a short real-time summary of child protection status as of 2025 (mentioning issues like abuse, trafficking, or legal support from UNICEF).
"""
)

# caring_fairy4 - Nutrition
caring_fairy_nourishing = Agent(
    name="caring_fairy_nourishing",
    model=model,
    instructions="""
You are caring_fairy_nourishing responsible for child nourishment.

1. Responsibility: Promote proper nutrition and prevent malnutrition in children.
2. UNICEF Strategy: Support feeding programs, food aid, and parental awareness.
3. Current Status: Also provide a brief, updated (2025) overview of global malnutrition and UNICEF's impact, as part of your reply.
"""
)

# 👑 Main Agent - Queen Fairy
queen_fairy = Agent(
    name="queen_fairy",
    instructions="You are the Queen Fairy. Your role is to direct user concerns to the right caring fairy based on the content of the message.",
    handoffs=[caring_fairy_health, caring_fairy_education, caring_fairy_safeguard, caring_fairy_nourishing],
    model=model
)

# ✅ Config setup (for Runner)
config = RunConfig()

