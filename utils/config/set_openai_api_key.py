import os
import platform
import logging

logging.basicConfig(level=logging.INFO)

def set_openai_api_key():
    """Sets the OpenAI API key in the environment variables.

    Prompts the user to enter their OpenAI API key if it is not already set in the environment variables.
    The API key is then set using the appropriate system command based on the operating system.

    Note: The user needs to restart their terminal or IDE to apply the changes.
    """
    if 'OPENAI_API_KEY' not in os.environ:
        try:
            api_key = input("Enter your OpenAI API key: ")

            # Detect the operating system
            os_type = platform.system()

            if os_type == "Windows":
                os.system(f'setx OPENAI_API_KEY "{api_key}"')
            elif os_type == "Darwin" or os_type == "Linux":
                # For macOS (Darwin) and Linux
                shell = os.environ.get("SHELL", "sh")
                if "bash" in shell:
                    os.system(f'export OPENAI_API_KEY="{api_key}"')
                    os.system(f'echo \'export OPENAI_API_KEY="{api_key}"\' >> ~/.bashrc')
                elif "zsh" in shell:
                    os.system(f'export OPENAI_API_KEY="{api_key}"')
                    os.system(f'echo \'export OPENAI_API_KEY="{api_key}"\' >> ~/.zshrc')
                else:
                    # Default for other shells
                    os.system(f'export OPENAI_API_KEY="{api_key}"')
                    os.system(f'echo \'export OPENAI_API_KEY="{api_key}"\' >> ~/.profile')

            logging.info("API key set successfully. Please restart your terminal or IDE to apply the changes.")
            exit()
        except Exception as e:
            logging.error(f"Error setting the OpenAI API key: {e}")
    else:
        logging.info("OpenAI API key already exists in environment variables.")

if __name__ == "__main__":
    set_openai_api_key()


