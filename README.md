# 🎬 Telegram Post Movie Info Generator

এই প্রজেক্টটি একটি সহজ Python স্ক্রিপ্ট যা TMDB API ব্যবহার করে মুভির তথ্য সংগ্রহ করে এবং একটি সুন্দর ফরম্যাটে সাজিয়ে দেয়।  
আপনি সহজেই Termux বা যেকোনো Linux environment-এ এটি ব্যবহার করতে পারবেন।  

---

## 📂 রিপোজিটরি
রিপোজিটরির নাম: **telegram-post**  
ফাইলের নাম: **movie_info.py**  
GitHub অ্যাকাউন্ট: **nihabali**  

👉 [ডাউনলোড লোকেশন](https://github.com/nihabali/telegram-post/blob/main/movie_info.py)

---

## ⚙️ সেটআপ গাইড (Termux এর জন্য)

একজন একেবারে নতুন ব্যবহারকারীও যেন সেটআপ করতে পারে তাই ধাপে ধাপে দেখানো হলো:

### 1️⃣ Termux ইনস্টল করুন
- Termux অ্যাপ [F-Droid](https://f-droid.org/en/packages/com.termux/) থেকে ডাউনলোড করুন।  

### 2️⃣ আপডেট করুন
```bash
pkg update && pkg upgrade -y
```

### 3️⃣ Python ইনস্টল করুন
```bash
pkg install python -y
```

### 4️⃣ `git` ইনস্টল করুন
```bash
pkg install git -y
```

### 5️⃣ রিপোজিটরি ক্লোন করুন
```bash
git clone https://github.com/nihabali/telegram-post.git
```

### 6️⃣ ডিরেক্টরিতে প্রবেশ করুন
```bash
cd telegram-post
```

### 7️⃣ প্রয়োজনীয় লাইব্রেরি ইন্সটল করুন
```bash
pip install requests
```

### 8️⃣ স্ক্রিপ্ট রান করুন
```bash
python movie_info.py
```

---

## 🖥️ ব্যবহারবিধি
1. স্ক্রিপ্ট রান করার পর আপনাকে একটি TMDB মুভি লিঙ্ক দিতে হবে। যেমন:
   ```
   https://www.themoviedb.org/movie/603-the-matrix
   ```
2. এরপর আপনি পছন্দমতো **Format (MP4, MKV, AVI ইত্যাদি)** এবং **Quality (480P, 720P, 1080P)** বেছে নিতে পারবেন।  
3. শেষে একটি সুন্দর ফরম্যাট করা মুভি ইনফো জেনারেট হবে।  

---

## 📌 উদাহরণ আউটপুট
```
╭─────────────────────
│ 🎬  Title     : The Matrix
│ 📅  Year      : 1999
│ 📺  Quality   : 1080P FHD
│ 💽  Format    : MKV
│ ⏱️  Runtime   : 2h 16m
│ 🎭  Genre     : Action, Science Fiction
│ ⭐ Rating    : 8.7/10 (TMDB)
╰─────────────────────
```

---

## 📝 নোট
- এই প্রজেক্টটি শুধু মুভির তথ্য জেনারেট করার জন্য, ডাউনলোড করার জন্য নয়।  
- স্ক্রিপ্ট রান করার জন্য **ইন্টারনেট কানেকশন আবশ্যক**।  
- যদি কোনো এরর পান তবে নিশ্চিত করুন আপনার API key সঠিকভাবে সেট করা আছে।  

---

## 👨‍💻 ক্রিয়েটর
GitHub: [nihabali](https://github.com/nihabali)
