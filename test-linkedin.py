import streamlit as st
import openai

# Streamlit application
def main():

    st.title('Social Media Post Generator with GPT-4')

    # Input field for user's OpenAI API key
    openai_api_key = st.text_input('Enter your OpenAI API key')

    # Dropdown for selecting the social media platform
    platform = st.selectbox('Choose your social media platform', ['LinkedIn', 'Instagram', 'Facebook', 'YouTube', 'TikTok', 'Snapchat', 'Google Profile Page'])

    # Input field for the desired post topic
    post_topic = st.text_input(f'What do you want your {platform} post to be about?', max_chars=400)

    # Input field for the goal of the post
    post_goal = st.text_input('What is the goal of your post? (e.g., reach, getting leads, etc.)')

    # Dropdown for selecting the hook style
    hook_style = st.selectbox('Choose your hook style', ['Question Hook', 'Fact/Statistic Hook', 'Quotation Hook', 'Personal Story Hook', 'Shocking Statement Hook', 'Humor Hook', 'Challenge Hook', 'Curiosity Hook', 'Prediction Hook', 'Problem Hook'])

    # Dropdown for selecting the target group, with "None selected" as the default option
    target_group_dropdown = st.selectbox('Choose your target group', ['None selected', 'Small Business Owners', 'Tech Startups', 'Healthcare Professionals', 'Educators', 'Freelancers', 'Millennials', 'Parents', 'Senior Citizens', 'Fitness Enthusiasts', 'Travelers'])

    # Input field for entering a custom target group
    target_group_custom = st.text_input('Or enter your own target group')

    # Dropdown for selecting the communication style
    communication_style = st.selectbox('Choose your communication style', [
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
    ])

    # Dropdown for selecting the language
    language = st.selectbox('Language', [
        'Arabic',
        'Bengali',
        'English',
        'French',
        'German',
        'Italian',
        'Portuguese',
        'Russian',
        'Spanish',
        'Turkish',
        'Ukrainian'
    ], index=0)

    target_group = None
    if target_group_dropdown != 'None selected' and target_group_custom:
        st.warning('Please select a target group from the dropdown menu or enter your own, not both.')
    elif target_group_dropdown != 'None selected':
        target_group = target_group_dropdown
    elif target_group_custom:
        target_group = target_group_custom

    if st.button('Generate Post'):
        if openai_api_key and post_topic and post_goal and target_group:
            # Set API key
            openai.api_key = openai_api_key

            # Create the GPT-4 prompt
            prompt_text = f"Act as a highly experienced {platform} professional. The target group is {target_group}. The goal of the post is {post_goal}. The communication style is {communication_style}. The selected language is {language}. Using the {hook_style}, craft a very compelling and interesting {platform} post out of the following information: {post_topic}"

            # Generate the post using GPT-4
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-4.0-turbo",
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
