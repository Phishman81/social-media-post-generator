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
    
    if st.button('Generate Post'):
        if openai_api_key and post_topic and post_goal:
            # Set API key
            openai.api_key = openai_api_key
            
            # Create the GPT-4 prompt
            prompt_text = f"Act as a highly experienced {platform} professional. The goal of the post is {post_goal}. Using the {hook_style}, craft a very compelling and interesting {platform} post out of the following information: {post_topic}"
            
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
            st.write('Please enter your OpenAI API key, the topic for your post, and the goal of your post.')
        
if __name__ == "__main__":
    main()
