import streamlit as st
import openai

# Streamlit application
def main():

    st.title('LinkedIn Post Generator with GPT-4')
    
    # Input field for user's OpenAI API key
    openai_api_key = st.text_input('Enter your OpenAI API key')
    
    # Input field for the desired LinkedIn post topic
    post_topic = st.text_input('What do you want a LinkedIn post about?', max_chars=400)
    
    if st.button('Generate Post'):
        if openai_api_key and post_topic:
            # Set API key
            openai.api_key = openai_api_key
            
            # Create the GPT-4 prompt
            prompt_text = f"Act as a highly experienced LinkedIn professional and craft a very compelling and interesting LinkedIn post out of the following information: {post_topic}"
            
            # Generate the post using GPT-4
            try:
                response = openai.Completion.create(
                    engine="gpt-4-0314",  # Replace with the correct GPT-4 engine ID
                    prompt=prompt_text,
                    max_tokens=200  # You can adjust the max_tokens as needed
                )

                st.write(response.choices[0].text.strip())
            except Exception as e:
                st.write(str(e))
        else:
            st.write('Please enter both your OpenAI API key and the LinkedIn post topic.')
        
if __name__ == "__main__":
    main()
