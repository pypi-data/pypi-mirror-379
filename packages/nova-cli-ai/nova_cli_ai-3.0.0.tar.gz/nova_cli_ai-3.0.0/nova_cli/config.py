# ============================================================================
# nova_cli/config.py - API Keys Configuration
# ============================================================================
import os

# All your API keys embedded in the package
DEFAULT_API_KEYS = {
    # GROQ API Keys (10 keys)
    "GROQ_API_KEY_1": "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",
    "GROQ_API_KEY_2": "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",
    "GROQ_API_KEY_3": "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",
    "GROQ_API_KEY_4": "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",
    "GROQ_API_KEY_5": "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",
    "GROQ_API_KEY_6": "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",
    "GROQ_API_KEY_7": "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",
    "GROQ_API_KEY_8": "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",
    "GROQ_API_KEY_9": "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",
    "GROQ_API_KEY_10": "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",

    # OpenRouter API Keys (10 keys)
    "OPENROUTER_API_KEY_1": "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",
    "OPENROUTER_API_KEY_2": "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",
    "OPENROUTER_API_KEY_3": "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",
    "OPENROUTER_API_KEY_4": "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",
    "OPENROUTER_API_KEY_5": "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",
    "OPENROUTER_API_KEY_6": "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",
    "OPENROUTER_API_KEY_7": "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",
    "OPENROUTER_API_KEY_8": "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",
    "OPENROUTER_API_KEY_9": "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",
    "OPENROUTER_API_KEY_10": "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",

    # HuggingFace API Keys (10 keys)
    "HUGGINGFACE_API_KEY_1": "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",
    "HUGGINGFACE_API_KEY_2": "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",
    "HUGGINGFACE_API_KEY_3": "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",
    "HUGGINGFACE_API_KEY_4": "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",
    "HUGGINGFACE_API_KEY_5": "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",
    "HUGGINGFACE_API_KEY_6": "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",
    "HUGGINGFACE_API_KEY_7": "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",
    "HUGGINGFACE_API_KEY_8": "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",
    "HUGGINGFACE_API_KEY_9": "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",
    "HUGGINGFACE_API_KEY_10": "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",

    # Cohere API Keys (10 keys)
    "COHERE_API_KEY_1": "8IvYIuvz5ctDVpoAhIVOwm1y2uDHEubSRGZqnFvw",
    "COHERE_API_KEY_2": "Ge8YwfGuHW9zCSOy9MQ9WZNLSlW3wCo9RmTqkV98",
    "COHERE_API_KEY_3": "cLWNdGfro4YSdFywnGqptUam87WqgsdGGGkJWkG6",
    "COHERE_API_KEY_4": "ASBUBrv9sbxm1LTjQhbPSYNbLkyeprhaieleUqcw",
    "COHERE_API_KEY_5": "myqOxBEQdDrJIk6H3LUrg16TbWzmjzfMDd62YdlZ",
    "COHERE_API_KEY_6": "qHUzliX2iJcSGd5s9mWH6evPrT9t7i8LSQ8MbgDL",
    "COHERE_API_KEY_7": "ff2WplZWlNUjtyTe1bbWeehBg0rHVsgJDLMzX7LF",
    "COHERE_API_KEY_8": "weqpY8aEKiiFRZbNqW9t30Kg00MuOYj4zRDXhBGX",
    "COHERE_API_KEY_9": "FSPXpIkSHgqxAgPmeCOq9ywbutcDFmZ3iAm7dfBM",
    "COHERE_API_KEY_10": "DyO4TIPqLeOEL4YKq81f580ftgFvkB4wTaeOyeiL",

    # NVIDIA API Keys (10 keys)
    "NVIDIA_API_KEY_1": "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",
    "NVIDIA_API_KEY_2": "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",
    "NVIDIA_API_KEY_3": "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",
    "NVIDIA_API_KEY_4": "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",
    "NVIDIA_API_KEY_5": "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",
    "NVIDIA_API_KEY_6": "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",
    "NVIDIA_API_KEY_7": "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",
    "NVIDIA_API_KEY_8": "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",
    "NVIDIA_API_KEY_9": "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",
    "NVIDIA_API_KEY_10": "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",

    # SambaNova API Keys (10 keys)
    "SAMBANOVA_API_KEY_1": "27942d98-dd1d-49d5-98a5-3720962b03a9",
    "SAMBANOVA_API_KEY_2": "6135da99-d970-492d-9899-4a42704c228d",
    "SAMBANOVA_API_KEY_3": "8ce44aa4-9730-4cfd-9eec-856b02eb1d52",
    "SAMBANOVA_API_KEY_4": "f472581a-6a69-40c9-882d-735bc53f2bd2",
    "SAMBANOVA_API_KEY_5": "8e79ab7e-71af-4021-a02c-e108bfd567e5",
    "SAMBANOVA_API_KEY_6": "34ad7be4-fc93-4a77-a975-a01aec2c45b6",
    "SAMBANOVA_API_KEY_7": "a8a73da8-b249-4366-afa6-04e39ef05b89",
    "SAMBANOVA_API_KEY_8": "c83968e8-4774-4166-9024-1ab4f0a836f7",
    "SAMBANOVA_API_KEY_9": "fb3f2849-0a28-4cbb-84de-fa624912152b",
    "SAMBANOVA_API_KEY_10": "dd1612b3-ff13-4cf1-b164-885a6dde9418",

    # DeepSeek API Keys (10 keys)
    "DEEPSEEK_API_KEY_1": "sk-121514ca729c4bcda60930117a2f3e8a",
    "DEEPSEEK_API_KEY_2": "sk-489e222b293d457898396fead7348b85",
    "DEEPSEEK_API_KEY_3": "sk-86b20bb2c25d48ee98da0e8b8c1d4da7",
    "DEEPSEEK_API_KEY_4": "sk-78eaa361cabb4e4aa5f0370b74ab94f4",
    "DEEPSEEK_API_KEY_5": "sk-9995cd3094fe45598adaa64fbd7ecec2",
    "DEEPSEEK_API_KEY_6": "sk-813cf15716704f7f93fa591f34cb8b66",
    "DEEPSEEK_API_KEY_7": "sk-3a71cad07c194cbcbb1a4c1e740994e2",
    "DEEPSEEK_API_KEY_8": "sk-c3a6b9be7fc04d40a1db53f17519c39f",
    "DEEPSEEK_API_KEY_9": "sk-504e9a564a4c44a69246bac88ca13148",
    "DEEPSEEK_API_KEY_10": "sk-d2aede3fd5744dac9166b55e92c190b6",

    # AI21 API Keys (10 keys)
    "AI21_API_KEY_1": "e11283e7-57db-474e-a11f-47811e14dd09",
    "AI21_API_KEY_2": "5da96219-2611-477f-8d61-ab6b3717af8c",
    "AI21_API_KEY_3": "b8e3c2c8-07c9-4038-9432-ca2ccb199712",
    "AI21_API_KEY_4": "42c5c916-61f8-4e00-a23f-e27287ff8f78",
    "AI21_API_KEY_5": "7749771f-f8e3-462a-ad1f-83208ec0230d",
    "AI21_API_KEY_6": "ae6208ba-c254-495e-b0f8-accda4ad2574",
    "AI21_API_KEY_7": "d4765ee5-80ae-4284-aee0-1c0fea460384",
    "AI21_API_KEY_8": "00f7fbc8-8c69-43a6-8910-0af5792cf381",
    "AI21_API_KEY_9": "5673cb5f-9bc6-4bf9-badb-500256538e53",
    "AI21_API_KEY_10": "b8fafa68-9709-4d4c-a9a4-a855b31c4c9c",

    # Cerebras API Keys (10 keys)
    "CEREBRAS_API_KEY_1": "csk-n44wyvftrtv4jd49pfwyjv23vv3tr86kvf8fk9dwvvppvk4h",
    "CEREBRAS_API_KEY_2": "csk-9pwxpy9xevnmmtv9hcrvpvv58jme5rtj848y2eyy53hxv5j8",
    "CEREBRAS_API_KEY_3": "csk-3y4rm3rc3n5twtyjk69f489cw2ct9hktpfp384xmh884w99j",
    "CEREBRAS_API_KEY_4": "csk-yty2etf966h5ekcftd92edeyp8mc3cfhw85jdt5xkwtntch5",
    "CEREBRAS_API_KEY_5": "csk-dv962k9hn4hnemj3m5cd2xfmvkde6td88y6em6ree6e22x6t",
    "CEREBRAS_API_KEY_6": "csk-23kmhnwd4chwphxxdpkyy9kvk2j636h2fnrvj4pn54jxrcpn",
    "CEREBRAS_API_KEY_7": "csk-k8334xd462c8fcy38eyydw54jr6ktx4n84t9ttfn2f6pjk2h",
    "CEREBRAS_API_KEY_8": "csk-yhf2kfhje823hmjk6v95jrxtv8jpp6f35mkw5wvfxtjyfjk3",
    "CEREBRAS_API_KEY_9": "csk-wyjvrtp5rm8ck4rchnn93dkx8hp5ej8ph8dehpxptd8mx9fc",
    "CEREBRAS_API_KEY_10": "csk-tccknm3t8chh9krddtfpktrvnfcexyjrmjfk2pvy55e8c2d2",

    # Scaleway API Keys (11 keys)
    "SCALEWAY_API_KEY": "95a8f8f9-4ed9-424c-b244-6c5eb58c085f",
    "SCALEWAY_API_KEY_1": "fb17748c-cb4d-4f6b-9da9-5a3fe1ed5ea3",
    "SCALEWAY_API_KEY_2": "180a73ea-67e2-4eb0-bca4-941aba6a52c2",
    "SCALEWAY_API_KEY_3": "2ddddf9b-4a12-487b-b637-47c28620c091",
    "SCALEWAY_API_KEY_4": "32629d94-93e0-4722-b0e6-0dbfdc357681",
    "SCALEWAY_API_KEY_5": "4e2f1f3b-1f4e-4dcb-8a6b-1c8e4f6e2b7a",
    "SCALEWAY_API_KEY_6": "184e4aba-35a7-4a3d-956a-7a5ff1a9a2a9",
    "SCALEWAY_API_KEY_7": "8aa1fb39-fe37-4add-bafc-d866018a553b",
    "SCALEWAY_API_KEY_8": "8318ca7b-9bc1-4cc1-89c8-6f86ff3e7cd6",
    "SCALEWAY_API_KEY_9": "898385c2-7fbd-41f8-8f97-178168808dd5",
    "SCALEWAY_API_KEY_10": "1029385a-0dcf-4300-8f64-079913f990d5",

    # Google API Keys (11 keys)
    "GOOGLE_API_KEY": "AIzaSyA6RI7AFP-xh3IjGHmn12R-ekisLv1p5L8",
    "GOOGLE_API_KEY_1": "AIzaSyDqv9tEvQQ3R0W6tmfLNwbd3RrFFtslO2A",
    "GOOGLE_API_KEY_2": "AIzaSyD1FaUcvVN7OJQiD91H2ma6z1n1t2fxuf4",
    "GOOGLE_API_KEY_3": "AIzaSyCmptvpL6O16L0sjUTM51QhfHRrNZrP40",
    "GOOGLE_API_KEY_4": "AIzaSyDxw8K-7SbrMiFKkxRTL0NU1L6ZoyqNkbs",
    "GOOGLE_API_KEY_5": "AIzaSyDym25GCfMmU0r_1lrlevDEdTmHaN_gurE",
    "GOOGLE_API_KEY_6": "AIzaSyAg25hg3nDEf1p6lmzxS1p8Sx7td9SzZqM",
    "GOOGLE_API_KEY_7": "AIzaSyByGb1GBc3dZU6zZze8CT0paYFPfxrBPCY",
    "GOOGLE_API_KEY_8": "AIzaSyDrV-x0_1tyBNlkMO2MxahzIY4TpKDeYno",
    "GOOGLE_API_KEY_9": "AIzaSyCqIceyUfYA1cwbZGzYuNME0Om5dp-VxJw",
    "GOOGLE_API_KEY_10": "AIzaSyC0unCNmApd7OawnNWdqfl8_jcUFaui7cU",

    # Mistral API Keys (10 keys)
    "MISTRAL_API_KEY_1": "PSgq58lyy49tLvpK5GTSsLyLp8ypq4o6",
    "MISTRAL_API_KEY_2": "JltqpiYPweMt9dO5ICEpkHaeP5er4Jo1",
    "MISTRAL_API_KEY_3": "REgQgwL91tKCiGWi3VUF9YfSApwEG5az",
    "MISTRAL_API_KEY_4": "6hoNje3cGXRfolUpMFxG3Um1fhK5NcDA",
    "MISTRAL_API_KEY_5": "1JPcYOFjBm5ozO3jkoJ50MNuVVy2MoY1",
    "MISTRAL_API_KEY_6": "NidrES0bKs0ly2lmijkGB1xCnPe9yEgr",
    "MISTRAL_API_KEY_7": "b7pMWgS8W8Bx3yL2xvEUsfq8CY7yrWOn",
    "MISTRAL_API_KEY_8": "XJR6NnrAaJJ0U7Ixq0IKC0uZJeiiJ7Iw",
    "MISTRAL_API_KEY_9": "kcnO9ZAZtf4jNJHuTI809rsuRmwJid22",
    "MISTRAL_API_KEY_10": "GfmtPUgZZr4QpGirclqh8SJzXp1S7qKl",

    # AIMLAPI API Keys (10 keys)
    "AIMLAPI_API_KEY_1": "5e9caeb6c9c64555aa51c9b2969dcb4b",
    "AIMLAPI_API_KEY_2": "6d74972c0d3249769cecf12a5ac76484",
    "AIMLAPI_API_KEY_3": "6bfd3a17158148d9ab77dc6f8d811ea4",
    "AIMLAPI_API_KEY_4": "313c51cfc9034b918cf901ff0dde72ab",
    "AIMLAPI_API_KEY_5": "0b4b040e7d244d5ab51abff13f9aca55",
    "AIMLAPI_API_KEY_6": "b06a1f32196e44bab7e53da4ec7e434e",
    "AIMLAPI_API_KEY_7": "e0a6029202e24012a3b3445a495f78f9",
    "AIMLAPI_API_KEY_8": "7857ffe4a2d548d3934ca716a859bd3f",
    "AIMLAPI_API_KEY_9": "e2612375142f43cbabe533e6ae8dea2e",
    "AIMLAPI_API_KEY_10": "12cd56dc58d2445a8e8b98a1bc94edc0",

    # Fireworks API Keys (10 keys)
    "FIREWORKS_API_KEY_1": "fw_3ZKWY7WTKyd73qkjuBDe9b2K",
    "FIREWORKS_API_KEY_2": "fw_3ZGBPHxqUFGstnk2XpcmYwA4",
    "FIREWORKS_API_KEY_3": "fw_3ZaoQja5hiT75V7muywEzjB3",
    "FIREWORKS_API_KEY_4": "fw_3ZGng3BZ2ZWm68QKSDh9chh7",
    "FIREWORKS_API_KEY_5": "fw_3ZkNVS1BccyuAwEBYJKKJNrk",
    "FIREWORKS_API_KEY_6": "fw_3ZJGckFVMnJiKPmf85TuTcSv",
    "FIREWORKS_API_KEY_7": "fw_3Zo4mjCQZ3ABDdc4nCofAwtc",
    "FIREWORKS_API_KEY_8": "fw_3ZZujgKb7Bv6P1cK6EXsMXGR",
    "FIREWORKS_API_KEY_9": "fw_3ZM14oYnz55Ab4oRvJ9sed3G",
    "FIREWORKS_API_KEY_10": "fw_3ZnX9JXqfR8A9Z7oqSvw9CyG",

    # Single API Keys
    "REPLICATE_API_KEY": "r8_bwW8H2dc7mNtTYSHQt3ZBgilJVtwJiE0GWTub",
    "GITHUB_API_KEY": "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",
    "CHUTES_API_KEY": "cpk_ac6896e542804e6393f7b07c36b169ef.6f6125f5d76b5280a060e761fd0184fd.chT8UKLw1g4VkKrMsRszAUL8TCu01Wg7",

    # Azure Speech Service
    "AZURE_SPEECH_KEY": "4yfASZkLrIEOoDTq8e9Wm7gqUqNYxRcG6pH8no3IctWAl6tn1Ed5JQQJ99BHACYeBjFXJ3w3AAAYACOGD8sa",
    "AZURE_REGION": "eastus",
    "AZURE_ENDPOINT": "https://eastus.api.cognitive.microsoft.com/",

    # Other Services
    "OPENWEATHER_API_KEY": "2db5e1d3241ce567c67e2871cee8",
    
    # System Configuration
    "DEBUG": "true",
    "LOG_LEVEL": "INFO",
    "DATABASE_URL": "sqlite:///./data/nova_memory.db",
    "MAX_CONCURRENT_REQUESTS": "10",
    "REQUEST_TIMEOUT": "30",
}

def setup_environment():
    """Setup API keys automatically when package is imported"""
    print("🔧 Setting up NOVA CLI environment...")
    keys_loaded = 0
    for key, value in DEFAULT_API_KEYS.items():
        if not os.environ.get(key):
            os.environ[key] = value
            keys_loaded += 1
    print(f"✅ Loaded {keys_loaded} API keys automatically!")
    print(f"🚀 NOVA CLI ready with {len(DEFAULT_API_KEYS)} total configurations!")

def get_key_summary():
    """Get summary of available API keys for debugging"""
    summary = {
        "GROQ": len([k for k in DEFAULT_API_KEYS.keys() if k.startswith("GROQ")]),
        "OPENROUTER": len([k for k in DEFAULT_API_KEYS.keys() if k.startswith("OPENROUTER")]),
        "HUGGINGFACE": len([k for k in DEFAULT_API_KEYS.keys() if k.startswith("HUGGINGFACE")]),
        "COHERE": len([k for k in DEFAULT_API_KEYS.keys() if k.startswith("COHERE")]),
        "NVIDIA": len([k for k in DEFAULT_API_KEYS.keys() if k.startswith("NVIDIA")]),
        "SAMBANOVA": len([k for k in DEFAULT_API_KEYS.keys() if k.startswith("SAMBANOVA")]),
        "DEEPSEEK": len([k for k in DEFAULT_API_KEYS.keys() if k.startswith("DEEPSEEK")]),
        "AI21": len([k for k in DEFAULT_API_KEYS.keys() if k.startswith("AI21")]),
        "CEREBRAS": len([k for k in DEFAULT_API_KEYS.keys() if k.startswith("CEREBRAS")]),
        "SCALEWAY": len([k for k in DEFAULT_API_KEYS.keys() if k.startswith("SCALEWAY")]),
        "GOOGLE": len([k for k in DEFAULT_API_KEYS.keys() if k.startswith("GOOGLE")]),
        "MISTRAL": len([k for k in DEFAULT_API_KEYS.keys() if k.startswith("MISTRAL")]),
        "AIMLAPI": len([k for k in DEFAULT_API_KEYS.keys() if k.startswith("AIMLAPI")]),
        "FIREWORKS": len([k for k in DEFAULT_API_KEYS.keys() if k.startswith("FIREWORKS")]),
    }
    total_keys = sum(summary.values())
    return summary, total_keys

def validate_api_keys():
    """Validate that all API keys are properly loaded"""
    missing_keys = []
    invalid_keys = []
    for key, value in DEFAULT_API_KEYS.items():
        if not value or value == "":
            missing_keys.append(key)
        elif len(str(value)) < 10:
            invalid_keys.append(key)
    return {
        "total_keys": len(DEFAULT_API_KEYS),
        "missing_keys": missing_keys,
        "invalid_keys": invalid_keys,
        "valid_keys": len(DEFAULT_API_KEYS) - len(missing_keys) - len(invalid_keys)
    }

def get_provider_info():
    """Get detailed provider information"""
    providers = {
        "GROQ": {
            "keys": [k for k in DEFAULT_API_KEYS.keys() if k.startswith("GROQ")],
            "count": len([k for k in DEFAULT_API_KEYS.keys() if k.startswith("GROQ")]),
            "status": "active"
        },
        "OPENROUTER": {
            "keys": [k for k in DEFAULT_API_KEYS.keys() if k.startswith("OPENROUTER")],
            "count": len([k for k in DEFAULT_API_KEYS.keys() if k.startswith("OPENROUTER")]),
            "status": "active"
        },
        "HUGGINGFACE": {
            "keys": [k for k in DEFAULT_API_KEYS.keys() if k.startswith("HUGGINGFACE")],
            "count": len([k for k in DEFAULT_API_KEYS.keys() if k.startswith("HUGGINGFACE")]),
            "status": "active"
        },
        "COHERE": {
            "keys": [k for k in DEFAULT_API_KEYS.keys() if k.startswith("COHERE")],
            "count": len([k for k in DEFAULT_API_KEYS.keys() if k.startswith("COHERE")]),
            "status": "active"
        },
        "NVIDIA": {
            "keys": [k for k in DEFAULT_API_KEYS.keys() if k.startswith("NVIDIA")],
            "count": len([k for k in DEFAULT_API_KEYS.keys() if k.startswith("NVIDIA")]),
            "status": "active"
        },
        "SAMBANOVA": {
            "keys": [k for k in DEFAULT_API_KEYS.keys() if k.startswith("SAMBANOVA")],
            "count": len([k for k in DEFAULT_API_KEYS.keys() if k.startswith("SAMBANOVA")]),
            "status": "active"
        },
        "DEEPSEEK": {
            "keys": [k for k in DEFAULT_API_KEYS.keys() if k.startswith("DEEPSEEK")],
            "count": len([k for k in DEFAULT_API_KEYS.keys() if k.startswith("DEEPSEEK")]),
            "status": "active"
        },
        "AI21": {
            "keys": [k for k in DEFAULT_API_KEYS.keys() if k.startswith("AI21")],
            "count": len([k for k in DEFAULT_API_KEYS.keys() if k.startswith("AI21")]),
            "status": "active"
        },
        "CEREBRAS": {
            "keys": [k for k in DEFAULT_API_KEYS.keys() if k.startswith("CEREBRAS")],
            "count": len([k for k in DEFAULT_API_KEYS.keys() if k.startswith("CEREBRAS")]),
            "status": "active"
        },
        "SCALEWAY": {
            "keys": [k for k in DEFAULT_API_KEYS.keys() if k.startswith("SCALEWAY")],
            "count": len([k for k in DEFAULT_API_KEYS.keys() if k.startswith("SCALEWAY")]),
            "status": "active"
        },
        "GOOGLE": {
            "keys": [k for k in DEFAULT_API_KEYS.keys() if k.startswith("GOOGLE")],
            "count": len([k for k in DEFAULT_API_KEYS.keys() if k.startswith("GOOGLE")]),
            "status": "active"
        },
        "MISTRAL": {
            "keys": [k for k in DEFAULT_API_KEYS.keys() if k.startswith("MISTRAL")],
            "count": len([k for k in DEFAULT_API_KEYS.keys() if k.startswith("MISTRAL")]),
            "status": "active"
        },
        "AIMLAPI": {
            "keys": [k for k in DEFAULT_API_KEYS.keys() if k.startswith("AIMLAPI")],
            "count": len([k for k in DEFAULT_API_KEYS.keys() if k.startswith("AIMLAPI")]),
            "status": "active"
        },
        "FIREWORKS": {
            "keys": [k for k in DEFAULT_API_KEYS.keys() if k.startswith("FIREWORKS")],
            "count": len([k for k in DEFAULT_API_KEYS.keys() if k.startswith("FIREWORKS")]),
            "status": "active"
        }
    }
    return providers

# Auto-setup when module is imported
if __name__ != "__main__":
    setup_environment()

# For debugging - run this file directly to see key summary
if __name__ == "__main__":
    print("🔍 NOVA CLI Configuration Summary")
    print("=" * 50)
    setup_environment()
    summary, total = get_key_summary()
    print(f"\n📊 API Keys by Provider:")
    for provider, count in summary.items():
        print(f"  • {provider}: {count} keys")
    print(f"\n✅ Total API Keys: {total}")
    validation = validate_api_keys()
    print(f"\n🔐 Key Validation:")
    print(f"  • Valid Keys: {validation['valid_keys']}")
    print(f"  • Missing Keys: {len(validation['missing_keys'])}")
    print(f"  • Invalid Keys: {len(validation['invalid_keys'])}")
    providers = get_provider_info()
    print(f"\n🚀 Active Providers: {len(providers)}")
    print("\n🎉 Configuration loaded successfully!")
