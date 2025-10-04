# -*- coding: utf-8 -*-

# --- কনফিগারেশন ---
# এখানে আপনার GitHub ইউজারনেম এবং রিপোজিটরির নাম দিন
GITHUB_USERNAME = "othersott"
REPOSITORY_NAME = "url"

def generate_github_pages_link():
    """
    ইউজারের কাছ থেকে ফোল্ডার এবং ফাইলের নাম নিয়ে
    GitHub Pages লিংক তৈরি করে।
    """
    
    print("--- GitHub Pages লিংক জেনারেটর ---")
    print(f"ইউজারনেম: {GITHUB_USERNAME}")
    print(f"রিপোজিটরি: {REPOSITORY_NAME}")
    print("-" * 35)

    # --- ধাপ ১: ফোল্ডারের পাথ তৈরি করা ---
    path_parts = []
    print("\n[ফোল্ডারের পাথ তৈরি করুন]")
    
    while True:
        # ইউজারের কাছ থেকে ফোল্ডারের নাম নেওয়া
        folder_name = input("ফোল্ডারের নাম লিখুন: ")
        
        # যদি কিছু লেখা হয়, তবে লিস্টে যোগ করা
        if folder_name.strip():
            path_parts.append(folder_name.strip())

        # পরবর্তী সিদ্ধান্ত নেওয়ার জন্য জিজ্ঞাসা করা
        choice = input("আরেকটি ফোল্ডার যোগ করতে Enter চাপুন, অথবা শেষ করতে 'y' লিখে Enter চাপুন: ")
        
        # যদি 'y' লেখা হয়, লুপ থেকে বেরিয়ে যাওয়া
        if choice.lower() == 'y':
            break
            
    # ফোল্ডারের নামগুলোকে "/" দিয়ে যুক্ত করে একটি স্ট্রিং তৈরি করা
    # যেমন: ['folder', 'subfolder'] -> "folder/subfolder"
    path_string = "/".join(path_parts)

    # --- ধাপ ২: ফাইলের নাম নেওয়া ---
    print("\n[ফাইলের নাম দিন]")
    file_name = input("ফাইলের নাম লিখুন (সহ extension, যেমন: test.html): ").strip()

    # --- ধাপ ৩: সম্পূর্ণ লিংক তৈরি করা ---
    base_url = f"https://{GITHUB_USERNAME}.github.io/{REPOSITORY_NAME}/"
    
    # যদি কোনো ফোল্ডার না থাকে, তাহলে শুধু ফাইলের নাম যুক্ত করা হবে
    if not path_string:
        final_url = f"{base_url}{file_name}"
    else:
        # ফোল্ডার থাকলে, ফোল্ডারের পাথ এবং ফাইলের নাম যুক্ত করা হবে
        final_url = f"{base_url}{path_string}/{file_name}"

    # --- ধাপ ৪: আউটপুট দেখানো ---
    print("\n" + "="*40)
    print("আপনার তৈরি করা GitHub Pages লিংক:")
    print(final_url)
    print("="*40)


# --- প্রোগ্রাম শুরু করার জন্য ---
if __name__ == "__main__":
    generate_github_pages_link()
