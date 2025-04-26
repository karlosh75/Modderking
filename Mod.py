import openai
import os
import subprocess

# Configuration
openai.api_key = 'YOUR-NEW-OPENAI-KEY-HERE'

def interact_with_ai(prompt):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Error contacting AI: {str(e)}"

def decompile_apk():
    apk_path = input("Enter APK file path: ")
    if not os.path.exists(apk_path):
        print("File not found!")
        return
        
    if not os.path.exists('output'):
        os.makedirs('output')
        
    try:
        subprocess.run(['jadx', '-d', 'output', apk_path], check=True)
        print("APK Decompiling Done! Check 'output' folder.")
    except Exception as e:
        print(f"Error: {str(e)}")

def ask_ai():
    prompt = input("Ask AI about modding: ")
    if not prompt.strip():
        print("Please type something.")
        return
    response = interact_with_ai(prompt)
    print("\nAI Response:")
    print(response)

def rebuild_apk():
    output_dir = 'output'
    rebuilt_apk_path = os.path.join(os.getcwd(), 'rebuilt.apk')
    try:
        subprocess.run(['apktool', 'b', output_dir, '-o', rebuilt_apk_path], check=True)
        print("APK Rebuilt Successfully!")
    except Exception as e:
        print(f"Error: {str(e)}")

def sign_apk():
    apk_path = input("Enter APK file path to sign: ")
    if not os.path.exists(apk_path):
        print("File not found!")
        return
        
    try:
        keystore_path = 'my-release-key.keystore'
        alias = 'my-key-alias'
        password = 'my-key-password'
        
        subprocess.run(['jarsigner', '-verbose', '-sigalg', 'SHA1withRSA', '-digestalg', 'SHA-256',
                      '-keystore', keystore_path, apk_path, alias,
                      '-storepass', password, '-keypass', password], check=True)
        print("APK Signed Successfully!")
    except Exception as e:
        print(f"Error: {str(e)}")

def main_menu():
    while True:
        print("\nAI APK Modder Menu:")
        print("1. Decompile APK")
        print("2. Ask AI Modding Help")
        print("3. Rebuild APK")
        print("4. Sign APK")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ")
        
        if choice == '1':
            decompile_apk()
        elif choice == '2':
            ask_ai()
        elif choice == '3':
            rebuild_apk()
        elif choice == '4':
            sign_apk()
        elif choice == '5':
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main_menu()
