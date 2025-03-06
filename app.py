import gradio as gr

# Function to process input text
def analyze_sentiment(text):
    result = sentiment_pipeline(text)
    return f"Label: {result[0]['label']}, Confidence: {result[0]['score']:.4f}"

# Create Gradio UI
iface = gr.Interface(
    fn=analyze_sentiment,
    inputs=gr.Textbox(placeholder="Enter text here..."),
    outputs="text",
    title="Sentiment Analysis",
    description="Enter a sentence to analyze its sentiment using a Hugging Face model."
)

# Launch the app
iface.launch()
