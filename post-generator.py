import streamlit as st
import openai

def check_password():
    """Returns `True` if the user entered the correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if st.session_state["password"] == st.secrets["password"]:
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # don't store the password
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        # First run, show input for password.
        st.title('Social Media Post Generator with GPT-4')
        st.write("Welcome to the Social Media Post Generator with GPT-4! This app helps you effortlessly create engaging and compelling social media posts for platforms like LinkedIn, Instagram, Facebook, YouTube, TikTok, Snapchat, and Google Profile Page. Simply enter the topic of your post, the goal you want to achieve, the target group you're aiming for, and other preferences like content length, hashtags, emojis, list type, hook style, and communication style.")
        st.write("Using the power of GPT-4, the app generates high-quality posts tailored to your specifications. This saves you time and effort, as you no longer need to write each post from scratch. The generated posts capture the desired tone, writing style, and even replicate the author's voice when provided with an example text.")
        st.write("")
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        return False
    elif not st.session_state["password_correct"]:
        # Password not correct, show input + error.
        st.title('Social Media Post Generator with GPT-4')
        st.write("Welcome to the Social Media Post Generator with GPT-4! This app helps you effortlessly create engaging and compelling social media posts for platforms like LinkedIn, Instagram, Facebook, YouTube, TikTok, Snapchat, and Google Profile Page. Simply enter the topic of your post, the goal you want to achieve, the target group you're aiming for, and other preferences like content length, hashtags, emojis, list type, hook style, and communication style.")
        st.write("Using the power of GPT-4, the app generates high-quality posts tailored to your specifications. This saves you time and effort, as you no longer need to write each post from scratch. The generated posts capture the desired tone, writing style, and even replicate the author's voice when provided with an example text.")
        st.write("")
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        st.error("😕 Password incorrect")
        return False
    else:
        # Password correct.
        return True

# Streamlit application
def main():
    if not check_password():
        return

    st.title('Social Media Post Generator with GPT-4')

    # Input field for user's OpenAI API key
    openai_api_key = st.secrets["openai"]["key"]

    # Dropdown for selecting the social media platform
    platform = st.selectbox('Choose your social media platform', ['LinkedIn', 'Instagram', 'Facebook', 'YouTube', 'TikTok', 'Snapchat', 'Google Profile Page'])

    # Input field for the desired post topic
    post_topic = st.text_input(f'In a few words: What is the general topic of your {platform} post?', max_chars=400)

    # Input field for the desired post details: post_details = st.text_input(f'What do you want your {platform} post to be about? You can and should be verx specific here.', max_chars=2000)
    post_details = st.text_area(f'What do you want your {platform} post to be about? You can and should be verx specific here.', max_chars=2000)
    # post_details = st.text_area('Or paste example text to copy the tone of voice & communication style to your post',max_chars=500, key="example_style")

    # Input field for the goal of the post
    post_goal = st.text_input('What is the goal of your post? (e.g., reach, getting leads, etc.)')

    # Input field for the call-to-action
    call_to_action = st.text_input(f'What should the call to action be?', max_chars=400)

    # Dropdown for selecting the content length
    content_length = st.selectbox('Choose your content length', ['Short: less than 80 characters', 'Compact: 80-250 characters', 'Medium: 250-600 characters', 'Long: more than 600 characters'])

    # Dropdown for selecting the hashtags
    hashtags = st.selectbox('Choose your hashtag preference', ['None', 'Just one', 'A few', 'Many'])

    # Dropdown for selecting the emojis
    emojis = st.selectbox('Choose your emoji preference', ['None', 'Just one', 'A few', 'Many'])

    # Dropdown for selecting the list type
    list_type = st.selectbox('Choose your list type', ['None', 'Short list (1-3 points)', 'Compact list (3-5 points)', 'Medium list (5-7 points)', 'Long list (10 points or more)', 'Short list with emojis (1-3 points)', 'Compact list with emojis (3-5 points)', 'Medium list with emojis (5-7 points)', 'Long list with emojis (10 points or more)'])

    # Dropdown for selecting the hook style
    hook_style = st.selectbox('Choose your hook style', ['Question Hook', 'Fact/Statistic Hook', 'Quotation Hook', 'Personal Story Hook', 'Shocking Statement Hook', 'Humor Hook', 'Challenge Hook', 'Curiosity Hook', 'Prediction Hook', 'Problem Hook'])

    # Dropdown for selecting the target group, with "None selected" as the default option
    target_group_dropdown = st.selectbox('Choose your target group', ['None selected', 'Small Business Owners', 'Tech Startups', 'Healthcare Professionals', 'Educators', 'Freelancers', 'Millennials', 'Parents', 'Senior Citizens', 'Fitness Enthusiasts', 'Travelers'])

    # Input field for entering a custom target group
    target_group_custom = st.text_input('Or enter your own target group')

    # Dropdown for selecting the communication style
    communication_style = st.selectbox('Choose your communication style', [
        'None selected',
        'Formal',
        'Informal',
        'Professional',
        'Friendly',
        'Persuasive',
        'Casual',
        'Technical',
        'Inspirational',
        'Educational',
        'Authoritative',
        'Conversational',
        'Direct',
        'Humorous',
        'Empathetic',
        'Motivational',
        'Caring',
        'Serious',
        'Positive',
        'Neutral',
        'Assertive'
    ], index=0)

    # Text area for pasting text for analyzing communication style
    example_text_for_style = st.text_area('Or paste example text to copy the tone of voice & communication style to your post',max_chars=500, key="example_style")

    # Input field for the post structure
    post_structure = st.text_input('How should the post be structured? (e.g., hook, story, important learnings as list, call to action, etc.)')

    # Dropdown for selecting the language
    language = st.selectbox('Language', [
        'German',
        'English (UK)',
        'English (US)',
        'French',
        'Italian',
        'Portuguese',
        'Russian',
        'Spanish'
    ], index=0)

    target_group = None
    if target_group_dropdown != 'None selected' and target_group_custom:
        st.warning('Please select a target group from the dropdown menu or enter your own, not both.')
    elif target_group_dropdown != 'None selected':
        target_group = target_group_dropdown
    elif target_group_custom:
        target_group = target_group_custom

    if example_text_for_style and communication_style != 'None selected':
        st.warning('Please either select a communication style or paste example text, not both.')
        return
    elif example_text_for_style == "" and communication_style == 'None selected':
        st.warning('Please either select a communication style or paste example text.')
        return

    if st.button('Generate Post'):
        if openai_api_key and post_topic and post_goal and target_group:
            # Set API key
            openai.api_key = openai_api_key

            if example_text_for_style:
                # Use example text for style if provided
                prompt_text = f"Act as a highly experienced {platform} professional and craft a very compelling and interesting {platform} post out of the following information: the general topic of the post is: {post_topic}. Here are some specific details about the post content: {post_details}. The call-to-action should be: {call_to_action}. The target group is {target_group}. The goal of the post is {post_goal}. The selected language is {language}. Using the {hook_style}, the desired content length is {content_length}, with a preference for {hashtags} hashtags that suit the target group, {emojis} emojis, and a {list_type}. Please structure the post in the following way {post_structure}. In your response, capture the same tone and writing style and replicate the author's voice and how they express themselves in this text example: {example_text_for_style} - without incorporating any of the examples content."
            else:
                # Use the selected communication style otherwise
                prompt_text = f"Act as a highly experienced {platform} professional and craft a very compelling and interesting {platform} post out of the following information: the general topic of the post is: {post_topic}. Here are some specific details about the post content: {post_details}. The call-to-action should be: {call_to_action}. The target group is {target_group}. The goal of the post is {post_goal}. The communication style is {communication_style}. The selected language is {language}. Using the {hook_style}, the desired content length is {content_length}, with a preference for {hashtags} hashtags that suit the target group, {emojis} emojis, and a {list_type}. Please structure the post in the following way {post_structure}."

            # Generate the post using GPT-4
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-4-0314",
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant."},
                        {"role": "user", "content": prompt_text}
                    ]
                )

                st.write(response['choices'][0]['message']['content'])
            except Exception as e:
                st.write(str(e))
        else:
            st.write('Please enter your OpenAI API key, the topic for your post, the goal of your post, and select or enter a target group.')
    elif target_group is None:
        st.warning('Please select a target group from the dropdown menu or enter your own.')

if __name__ == "__main__":
    main()
