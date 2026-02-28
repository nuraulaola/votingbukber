import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Voting Bukber AEON", layout="centered")

DATA_FILE = "votes.csv"

restaurants = [
    ("Oseng Bistro", "Nusantara | Lt. 3A", "https://www.instagram.com/s/aGlnaGxpZ2h0OjE4MDUyMjczOTY0NDE2MTI3?story_media_id=3806657906050496184_77933270258"),
    ("Gyu-Kaku", "AYCE 90 menit | Lt. 2", "https://menu.gyu-kaku.id/"),
    ("Seirock-Ya", "Ramen | Lt. 1", "https://www.instagram.com/stories/highlights/17903240633680261/?hl=en"),
    ("Chadol Gujeolpan", "Korea | Lt. 1", "https://www.instagram.com/stories/highlights/17998792436150097/?hl=en"),
    ("Gokana", "Ramen, Bento | Lt. 3A", "https://drive.google.com/file/d/1WJYcsTnWRRcVwmv7oW5RZcDhuHoPVvVa/view"),
    ("Raa Cha", "Suki, BBQ | Lt. 3A", "https://www.instagram.com/stories/highlights/18197530090310250/?hl=en"),
    ("Legend of Noodle", "Korea | Lt. 3", "https://drive.google.com/file/d/13MtdLEm7VonCbjA-hIZbymqOPDmDHBhN/view"),
    ("Solaria", "Chinese, Nusantara | Lt. 3A", "https://tr.ee/yl7g2xUq6Z"),
    ("Steak 21", "Steak, Pasta | Lt. 3A", "https://www.instagram.com/s/aGlnaGxpZ2h0OjE4MDcxNDI5NDI4NjY2ODUz?story_media_id=3840194822133614287_2261196269"),
    ("Umaqita", "Bali | Lt. 1", "https://tr.ee/URWfL_YT3y"),
    ("Little Red Dot", "Singapore | Lt. 1", "https://tr.ee/StNiRCFTNy"),
]

# init data
if not os.path.exists(DATA_FILE):
    pd.DataFrame(columns=["name", "vote"]).to_csv(DATA_FILE, index=False)

df = pd.read_csv(DATA_FILE)

st.title("🍽️ Voting Bukber AEON Tanjung Barat")

st.subheader("🗳️ Pilih restoran")

user_name = st.text_input("Masukkan nama kamu")

# simpan pilihan di session
if "choice" not in st.session_state:
    st.session_state.choice = None

# render opsi custom
for i, (name, desc, link) in enumerate(restaurants):
    col1, col2 = st.columns([4,1])

    with col1:
        if st.radio(
            label=f"{name} ({desc})",
            options=[i],
            key=f"radio_{i}",
            label_visibility="visible"
        ):
            st.session_state.choice = i

    with col2:
        st.markdown(f"[Menu]({link})")

# submit
if st.button("Submit Vote"):
    if user_name.strip() == "":
        st.warning("Nama wajib diisi")
    elif st.session_state.choice is None:
        st.warning("Pilih restoran dulu")
    else:
        if user_name in df["name"].values:
            st.error("Kamu sudah vote sebelumnya")
        else:
            selected_name = restaurants[st.session_state.choice][0]

            new_data = pd.DataFrame(
                [[user_name, selected_name]],
                columns=["name", "vote"]
            )

            df = pd.concat([df, new_data], ignore_index=True)
            df.to_csv(DATA_FILE, index=False)

            st.success("Vote berhasil disimpan!")

# hasil
st.divider()
st.subheader("📊 Hasil Voting")

if not df.empty:
    st.bar_chart(df["vote"].value_counts())
else:
    st.info("Belum ada vote masuk")