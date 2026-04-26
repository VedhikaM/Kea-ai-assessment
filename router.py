def route_request(content_type, prompt):
    if content_type == "image":
        return generate_image(prompt)
    elif content_type == "video":
        return generate_video(prompt)
    elif content_type == "voice":
        return generate_voice(prompt)
    else:
        return {"error": "Invalid content type"}

def generate_image(prompt):
    # Simulated response (replace with real API)
    return {
        "type": "image",
        "prompt": prompt,
        "output_url": "https://sample.com/image.png"
    }

def generate_video(prompt):
    return {
        "type": "video",
        "prompt": prompt,
        "output_url": "https://sample.com/video.mp4"
    }

def generate_voice(prompt):
    return {
        "type": "voice",
        "prompt": prompt,
        "output_url": "https://sample.com/audio.mp3"
    }
