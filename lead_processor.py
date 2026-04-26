import json

# Sample rule-based classification
def classify_lead(data):
    message = data.get("message", "").lower()
    budget = data.get("budget", "")
    timeline = data.get("timeline", "").lower()

    if budget and "immediate" in timeline:
        return {"category": "Hot", "reason": "Budget and urgency present"}
    elif "price" in message or "demo" in message:
        return {"category": "Warm", "reason": "Interest shown"}
    else:
        return {"category": "Cold", "reason": "Low intent"}

# Generate response
def generate_response(data, category):
    name = data.get("name", "User")
    message = data.get("message", "")

    if category == "Hot":
        return f"Hi {name}, thanks for your interest! Based on your requirements, let’s quickly connect to get you started."
    elif category == "Warm":
        return f"Hi {name}, thanks for reaching out! I can share more details. Let me know what you’d like to explore."
    else:
        return f"Hi {name}, thanks for your message! Could you share more details so I can assist you better?"

# Main pipeline
def process_lead(data):
    classification = classify_lead(data)
    response = generate_response(data, classification["category"])

    return {
        "input": data,
        "output": {
            "category": classification["category"],
            "reason": classification["reason"],
            "response": response
        }
    }

# Example run
if __name__ == "__main__":
    sample = {
        "name": "John",
        "message": "I want pricing details",
        "budget": "1000 USD",
        "timeline": "Immediate"
    }

    result = process_lead(sample)
    print(json.dumps(result, indent=2))
