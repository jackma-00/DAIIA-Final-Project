from autogen import (
    AssistantAgent,
    UserProxyAgent,
    GroupChat,
    GroupChatManager,
    config_list_from_json,
)


# Set up LLM configuration
config_list = config_list_from_json(env_or_file="OAI_CONFIG_LIST")
llm_config = {"config_list": config_list, "seed": 42, "timeout": 120}

# Loading prompts
with open("./src/prompts/auctioneer/auctioneer_context.txt", "r") as f_in:
    auctioneer_context = f_in.read()

with open("./src/prompts/auctioneer/auctioneer_prompt.txt", "r") as f_in:
    auctioneer_prompt = f_in.read()

with open("./src/prompts/participant/participant_context.txt", "r") as f_in:
    participant_context = f_in.read()

with open("./src/prompts/participant/participant_prompt.txt", "r") as f_in:
    participant_prompt = f_in.read()

with open("./src/prompts/proxy/proxy_prompt.txt", "r") as f_in:
    proxy_prompt = f_in.read()

# Initialize agents
user_proxy = UserProxyAgent(
    name="user_proxy",
    human_input_mode="NEVER",
    max_consecutive_auto_reply=20,
    is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
    llm_config=llm_config,
    system_message=proxy_prompt,
)

auctioneer = AssistantAgent(
    name="auctioneer",
    llm_config=llm_config,
    system_message=auctioneer_context.format(
        asking_price=1000, percentage="5%", reserve_price=700
    )
    + auctioneer_prompt,
)

participant1 = AssistantAgent(
    name="participant1",
    llm_config=llm_config,
    system_message=participant_context.format(price=920) + participant_prompt,
)

participant2 = AssistantAgent(
    name="participant2",
    llm_config=llm_config,
    system_message=participant_context.format(price=900) + participant_prompt,
)

"""participant3 = AssistantAgent(
    name="participant3",
    llm_config=llm_config,
    system_message=participant_context.format(price=890) + participant_prompt,
)"""

# Instantiate the groupchat
groupchat = GroupChat(
    agents=[user_proxy, auctioneer, participant1, participant2],
    messages=[],
)

manager = GroupChatManager(groupchat=groupchat, llm_config=llm_config)

# Initiate chat
user_proxy.initiate_chat(manager, message="Run a dutch auction.")
