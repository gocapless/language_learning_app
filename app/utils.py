import os
from google.cloud import texttospeech

def generate_audio(phrase_id, text):
    # Initialize the Text-to-Speech client
    client = texttospeech.TextToSpeechClient()
    
    # Set up the input for synthesis
    synthesis_input = texttospeech.SynthesisInput(text=text)
    
    # Define voice parameters
    voice = texttospeech.VoiceSelectionParams(
        language_code="pt-PT",  # European Portuguese
        ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
    )
    
    # Define audio configuration
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )
    
    # Perform the text-to-speech request
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )
    
    # Define the path where the audio will be saved
    audio_folder = os.path.join("app", "static", "audio")
    os.makedirs(audio_folder, exist_ok=True)  # Ensure the directory exists
    
    # Save the audio file
    audio_filename = os.path.join(audio_folder, f"{phrase_id}.mp3")
    with open(audio_filename, "wb") as out:
        out.write(response.audio_content)
    
    # Return the relative path to serve the file via Flask
    return f"static/audio/{phrase_id}.mp3"
