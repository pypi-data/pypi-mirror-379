# nova_cli/keys.py

import os
from dotenv import load_dotenv

load_dotenv()  # Load .env file

# Define all providers and the number of keys per provider
PROVIDERS = {
    "GROQ": 10,
    "OPENROUTER": 10,
    "HUGGINGFACE": 10,
    "COHERE": 10,
    "REPLICATE": 1,
    "GITHUB": 1,
    "NVIDIA": 10,
    "SAMBANOVA": 10,
    "CHUTES": 1,
    "DEEPSEEK": 10,
    "AI21": 10,
    "CEREBRAS": 10,
    "SCALEWAY": 10,
    "GOOGLE": 10,
    "MISTRAL": 10,
    "AIMLAPI": 10,
    "FIREWORKS": 10,
    "AZURE_SPEECH": 1,
    "OPENWEATHER": 1,
    "OPENAI": 1,  # optional
}

# Load keys from environment variables
API_KEYS = {}
for provider, count in PROVIDERS.items():
    keys = []
    for i in range(1, count + 1):
        key_name = f"{provider}_API_KEY_{i}" if count > 1 else f"{provider}_API_KEY"
        key_value = os.getenv(key_name)
        if key_value:
            keys.append(key_value)
    if keys:
        API_KEYS[provider] = keys

# Initialize round-robin state
current_index = {provider: 0 for provider in API_KEYS.keys()}

def get_next_key(provider: str):
    """Return the next key for the provider in round-robin fashion"""
    if provider not in API_KEYS:
        raise ValueError(f"No keys found for provider: {provider}")
    keys = API_KEYS[provider]
    idx = current_index[provider]
    key = keys[idx]
    # Update index for next call
    current_index[provider] = (idx + 1) % len(keys)
    return key
