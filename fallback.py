def call_model(primary_func, fallback_func, prompt):
    try:
        return primary_func(prompt)
    except Exception:
        return fallback_func(prompt)
