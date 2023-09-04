from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/sns-webhook', methods=['POST'])
def sns_webhook():
    try:
        # Get the SNS message from the request
        sns_message = request.json

        # Handle the SNS message as needed
        # In this example, we just print it
        print("Received SNS message:")
        print(sns_message)

        # Return a success response
        return jsonify({'message': 'SNS message received successfully'}), 200

    except Exception as e:
        # Handle any exceptions
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run()
#     app.run(host='0.0.0.0', port=5000)