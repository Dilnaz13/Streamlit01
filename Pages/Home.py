import streamlit as st


class Home:
    def __init__(self):
        pass

    def app(self):
        st.title('Welcome to My Homepage')

        st.write(
            "Hi, I am **Dilnaz Ayazhanova** :brown_heart:. Welcome to my homepage! I'm passionate about Data Science. Feel free to explore and connect with me!")

        st.subheader("About Me")
        st.write("""
        - **Data Science**: I'm passionate about analyzing data and building models to solve real-world problems.""")

        st.subheader("Connect with Me")
        st.write("You can connect with me through the following platform:")

        if st.button("Visit My Instagram"):
            st.markdown("[Click here to visit my Instagram](https://www.instagram.com/ayazhanovad)",
                        unsafe_allow_html=True)


        st.subheader("Favorite Quote")
        st.write('Raise your words, not your voice. It is rain that grows flowers, not thunder')

if __name__ == "__main__":
    Home().app()
