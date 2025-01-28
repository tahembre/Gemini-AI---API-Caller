
import google.generativeai as genai
import os

genai.configure(api_key='YOUR_GEMINI_API_HERE')

def make_gemini_text_request(prompt, model_name="gemini-2.0-flash-exp"):
    try:
        model = genai.GenerativeModel(model_name)
        response = model.generate_content(prompt)
        return response.text, "success", None
    except Exception as e:
        return None, "failed", str(e)

def make_gemini_image_request(prompt, image_path, model_name="gemini-pro-vision"):
    try:
        if not os.path.exists(image_path):
            return None, "failed", f"Image file not found: {image_path}"

        model = genai.GenerativeModel(model_name)
        with open(image_path, 'rb') as f:
            image_data = f.read()
            response = model.generate_content([prompt, {"mime_type": "image/jpeg", "data": image_data}]) #use image/png if using png

        return response.text, "success", None
    except Exception as e:
        return None, "failed", str(e)



# To switch between Image and Text, simply switch the False / True statements below.
ImageAI = False
TextAI = True

if __name__ == "__main__":
    while True:
        if TextAI is True:
            # --- Text-Only Example ---
            #print('type your question:\n')
            text_prompt = str(input())
            response_text, status, error = make_gemini_text_request(text_prompt)
            if status == "success":
                #print("\n--- Gemini Text Response ---")
                print(f"\n{response_text}")
            else:
                print(f"\n--- Gemini Text Request Failed ---\nError: {error}")

        if ImageAI is True:
            # Image Example (You need to have an image file saved locally)
            image_path = str(input())  # Replace with the path to your image
            image_prompt = "Describe the content of this image"
            response_image_text, status, error = make_gemini_image_request(image_prompt, image_path)
            if status == "success":
                print("\n--- Gemini Image Response ---")
                print(f"Response:\n{response_image_text}")
            else:
                print(f"\n--- Gemini Image Request Failed ---\nError: {error}")