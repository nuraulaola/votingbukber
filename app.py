import streamlit as st
import pandas as pd
import os

# =========================
# CONFIG
# =========================
st.set_page_config(page_title="Voting Bukber AEON Tanjung Barat", layout="centered")

DATA_FILE = "votes.csv"

# =========================
# DATA RESTO
# =========================
restaurants = [
    {
        "name": "Oseng Bistro",
        "desc": "Nusantara | Lt. 3A",
        "link": "https://www.instagram.com/s/aGlnaGxpZ2h0OjE4MDUyMjczOTY0NDE2MTI3?story_media_id=3806657906050496184_77933270258"
    },
    {
        "name": "Gyu-Kaku",
        "desc": "AYCE 90 menit | Lt. 2",
        "link": "https://menu.gyu-kaku.id/"
    },
    {
        "name": "Seirock-Ya",
        "desc": "Ramen | Lt. 1",
        "link": "https://www.instagram.com/stories/highlights/17903240633680261/?hl=en"
    },
    {
        "name": "Chadol Gujeolpan",
        "desc": "Korea | Lt. 1",
        "link": "https://www.instagram.com/stories/highlights/17998792436150097/?hl=en"
    },
    {
        "name": "Gokana",
        "desc": "Ramen, Bento | Lt. 3A",
        "link": "https://drive.google.com/file/d/1WJYcsTnWRRcVwmv7oW5RZcDhuHoPVvVa/view"
    },
    {
        "name": "Raa Cha",
        "desc": "Suki, BBQ | Lt. 3A",
        "link": "https://www.instagram.com/stories/highlights/18197530090310250/?hl=en"
    },
    {
        "name": "Legend of Noodle",
        "desc": "Korea | Lt. 3",
        "link": "https://drive.google.com/file/d/13MtdLEm7VonCbjA-hIZbymqOPDmDHBhN/view"
    },
    {
        "name": "Solaria",
        "desc": "Chinese, Nusantara | Lt. 3A",
        "link": "https://tr.ee/yl7g2xUq6Z"
    },
    {
        "name": "Steak 21",
        "desc": "Steak, Pasta | Lt. 3A",
        "link": "https://www.instagram.com/s/aGlnaGxpZ2h0OjE4MDcxNDI5NDI4NjY2ODUz?story_media_id=3840194822133614287_2261196269"
    },
    {
        "name": "Umaqita",
        "desc": "Bali | Lt. 1",
        "link": "https://tr.ee/URWfL_YT3y"
    },
    {
        "name": "Little Red Dot",
        "desc": "Singapore | Lt. 1",
        "link": "https://tr.ee/StNiRCFTNy"
    }
]

# =========================
# INIT DATA
# =========================
if not os.path.exists(DATA_FILE):
    df_init = pd.DataFrame(columns=["name", "vote"])
    df_init.to_csv(DATA_FILE, index=False)

df = pd.read_csv(DATA_FILE)

# =========================
# UI HEADER
# =========================
st.title("🍽️ Voting Bukber AEON Tanjung Barat")
st.caption("Note: Belum cek ketersediaan resto")

st.divider()

# =========================
# INPUT USER
# =========================
user_name = st.text_input("Masukkan nama kamu")

st.subheader("Pilih restoran:")

options = []
for r in restaurants:
    label = f"{r['name']} ({r['desc']})"
    options.append(label)

choice = st.radio("Daftar resto", options)

# tampilkan link menu
selected_index = options.index(choice)
selected_resto = restaurants[selected_index]

st.markdown(f"🔗 [Lihat menu]({selected_resto['link']})")

# =========================
# VOTING BUTTON
# =========================
if st.button("Submit Vote"):
    if user_name.strip() == "":
        st.warning("Nama wajib diisi")
    else:
        # cek apakah sudah vote
        if user_name in df["name"].values:
            st.error("Kamu sudah vote sebelumnya")
        else:
            new_data = pd.DataFrame([[user_name, selected_resto["name"]]], columns=["name", "vote"])
            df = pd.concat([df, new_data], ignore_index=True)
            df.to_csv(DATA_FILE, index=False)
            st.success("Vote berhasil disimpan!")

# =========================
# HASIL
# =========================
st.divider()
st.subheader("📊 Hasil Voting")

if not df.empty:
    result = df["vote"].value_counts()
    st.bar_chart(result)

    st.write("Detail:")
    st.dataframe(df)
else:
    st.info("Belum ada vote masuk")
