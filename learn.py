from flask import Flask, request, jsonify
from openai import OpenAI

app = Flask(__name__)

gpt = OpenAI(
    api_key="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"
)

@app.route('/get_feedback', methods=['POST'])
def get_feedback():
    # Extract question, ideal answer, and student's answer from the request
    data = request.get_json()
    question = data.get('question')
    ideal_answer = data.get('ideal_answer')
    student_answer = data.get('student_answer')
    
    # Prepare the prompt for the GPT model
    prompt = f"Question: {question}\nIdeal Answer: {ideal_answer}\nStudent Answer: {student_answer}\n\nProvide feedback for improvement:"
    
    # Use GPT to generate feedback
    response = gpt.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": prompt
            }
        ]
    )

    # Extract the feedback from the response
    feedback = response.choices[0].message.content

    # Return the feedback as a JSON response
    return jsonify({'feedback': feedback})

if __name__ == '__main__':
    app.run(debug=True)
