import openai
import streamlit as st

# Configurarea cheii API OpenAI
openai.api_key = 'sk-proj-egEum9ayCy15JabH9alqT3BlbkFJfDZOf2YwBZU76xYjWcqb'

# Nu mai am credite pe OpenAI, dar merge codul

def generate_text(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Buna dimineata"},
                {"role": "user", "content": prompt}
            ],
            max_tokens=150
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        return f"A apărut o eroare: {str(e)}"

def main():
    st.title("Generare de Text cu GPT-3.5-turbo")
    st.write("Introduceți un text inițial și modelul GPT-3.5-turbo va genera o continuare.")

    prompt = st.text_area("Text inițial", height=150)
    if st.button("Generează text"):
        if prompt:
            with st.spinner("Generând text..."):
                generated_text = generate_text(prompt)
            st.subheader("Text Generat:")
            st.write(generated_text)
        else:
            st.warning("Vă rugăm să introduceți un text inițial.")

if __name__ == "__main__":
    main()

