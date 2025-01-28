# Gemini API Caller

This repository contains a Python script for interacting with the Gemini API. It supports both text-based and image-based requests, leveraging Google's Gemini models for AI-driven responses.

---

## Features

- **Text AI**: Send text prompts to the Gemini API and receive AI-generated responses.
- **Image AI**: Send text prompts alongside image data to the Gemini API and receive AI-generated insights or descriptions about the image.

---

## Requirements

Before running the script, ensure the following:

1. **Python Version**: Python 3.7 or later.
2. **Python Libraries**:
   - `google-generativeai`
   - `os` (built-in, no installation required)

---

## Setup Instructions

### 1. **Obtain a Gemini API Key**

To use the Gemini API, you need a valid API key. Follow these steps:

1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Enable the **Generative AI API** for your project:
   - Navigate to the "APIs & Services" section.
   - Click **Enable APIs and Services**.
   - Search for **Generative AI API** and enable it.
3. Go to the **Credentials** tab.
4. Click **Create Credentials** > **API Key**.
5. Copy the generated API key.

---

### 2. **Install Required Libraries**

Install the necessary library using `pip`:
```bash
pip install google-generativeai
```

---

### 3. **Configure the API Key**

Replace the placeholder `YOUR_GEMINI_API_HERE` in the script with your actual Gemini API key:
```python
genai.configure(api_key='YOUR_GEMINI_API_HERE')
```

---

## Running the Script

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/gemini-api-caller.git
   cd gemini-api-caller
   ```

2. Run the script:
   ```bash
   python script_name.py
   ```

3. Follow the on-screen prompts:
   - For **text requests**, type your question or prompt.
   - For **image requests**, input the path to your image file.

---

## Switching Between Text and Image AI

To toggle between text and image AI, modify these flags in the script:
```python
ImageAI = False  # Set to True to enable Image AI
TextAI = True    # Set to False to disable Text AI
```

---

## Example Usages

### Text AI Example

1. **Input**:
   ```
   What is the tallest mountain in the world?
   ```

2. **Output**:
   ```
   The tallest mountain in the world is Mount Everest, which stands at 8,848.86 meters (29,031.7 feet).
   ```

---

### Image AI Example

1. **Input**:
   - **Image File Path**: `sunset.jpg`
   - **Prompt**: (Automatically sent by the script: "Describe the content of this image")

2. **Output**:
   ```
   --- Gemini Image Response ---
   Response:
   This image features a breathtaking sunset over a serene ocean, with vibrant hues of orange, pink, and purple filling the sky.
   ```

---

### Mixed Example

You can switch between text and image processing by enabling or disabling `TextAI` and `ImageAI` flags.

**Example**:
- **Text Request**: Type a question like "What is AI?"
- **Image Request**: Provide the path to a local image file, e.g., `path/to/image.jpg`.

---

## Troubleshooting

- **Invalid API Key**: Ensure your API key is correct and replace `YOUR_GEMINI_API_HERE` in the script.
- **Image Not Found**: Double-check the file path for the image.
- **Missing Dependencies**: Install the required library using:
  ```bash
  pip install google-generativeai
  ```

---

## Contributing

Contributions are welcome! Feel free to submit pull requests or open issues to improve the script.

---

## License

This project is licensed under the MIT License.

---

## Resources

- [Gemini API Documentation](https://developers.generativeai.google.com/)
- [Google Cloud Console](https://console.cloud.google.com/)

