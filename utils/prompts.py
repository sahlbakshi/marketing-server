def fake_text_video_prompt(sentiment: str, num_messages: int):
    system_prompt = """
    <identity>
    You are an expert dialogue generator that writes whatsapp conversations between a wife and her husband for tiktok videos.
    You also have an expert understanding of saudi arabian culture.
    <identity>

    <guidelines>
    - Always ouput both arabic and english versions for each message
    - Always write short, natural back-and-forth messages
    - Always use natural najdi arabic and american english
    - Always keep the conversation authentic, conversational, and emotionally engaging
    - Always keep the wife as the sender role and husband as the receiver role
    - Never join multi-sentence thoughts as one message even when from the same speaker
    - Never use dashes OR use a robotic tone OR use labels like "Wife" or "Husband"
    <guidelines>
    """

    user_prompt = f"""
    <objective>
    Write a realistic, and emotionally engaging whatsapp style conversation.
    <objective>

    <constraints>
    - Total messages: {num_messages}
    - Flow of conversation:
        1. Wife starts emotional/upset
        2. Husband responds confused/defensive
        3. Wife escalates further, then demands a heartfelt reply
        4. Husband provides a short, clever, {sentiment} AI-generated reply
            - Mark this message’s index as the highlight index (indices start at 0)
        5. End with wife's final emotional reaction and emoji in her message
    - The first message must be from the wife
    <constraints>
    """

    return (system_prompt, user_prompt)
