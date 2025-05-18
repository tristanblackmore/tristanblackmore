import os

# Your GitHub repo info
github_user = "yourusername"
github_repo = "yourrepo"
branch = "main"  # or 'master' or whatever your branch is
folder_path = "assets/images"  # local folder path relative to script
github_folder_path = "assets/images"  # path inside repo

def generate_github_image_list():
    files = os.listdir(folder_path)
    images = [f for f in files if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp'))]
    urls = [
        f'https://raw.githubusercontent.com/{github_user}/{github_repo}/{branch}/{github_folder_path}/{img}'
        for img in images
    ]

    # Format as JS array string
    js_array = "[\n  " + ",\n  ".join(f'"{url}"' for url in urls) + "\n]"
    return js_array

if __name__ == "__main__":
    print("Copy this JS array and paste it into your website code:")
    print(generate_github_image_list())
