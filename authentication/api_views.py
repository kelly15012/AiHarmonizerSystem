import numpy as np
from tensorflow.keras.models import load_model
import joblib
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Load the trained model and the label encoders
model_path = 'models/lstm_chord_model.keras'
model = load_model(model_path)

label_encoder_chord1 = joblib.load('models/label_encoder_chord1.pkl')
label_encoder_chord2 = joblib.load('models/label_encoder_chord2.pkl')
label_encoder_chord1_type = joblib.load('models/label_encoder_chord1_type.pkl')

# Function to prepare input for the model
def prepare_input(chord1, interval, chord1_type):
    if chord1 not in label_encoder_chord1.classes_:
        raise ValueError(f"Chord '{chord1}' not found in chord1 label encoder.")
    if chord1_type not in label_encoder_chord1_type.classes_:
        raise ValueError(f"Chord type '{chord1_type}' not found in chord1_type label encoder.")
    
    chord1_encoded = label_encoder_chord1.transform([chord1])[0]
    chord1_type_encoded = label_encoder_chord1_type.transform([chord1_type])[0]
    return np.array([[chord1_encoded, interval, chord1_type_encoded]])

# Function to predict the chord2
def predict_chord(chord1, interval, chord1_type):
    X_new = prepare_input(chord1, interval, chord1_type)
    prediction = model.predict(X_new)
    predicted_class = np.argmax(prediction, axis=1)
    predicted_chord = label_encoder_chord2.inverse_transform(predicted_class)
    return predicted_chord[0]

@csrf_exempt
def predict_chord_api(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            chord1 = data['base_chord']
            interval = int(data['interval'])
            chord1_type = data['chord1_type']

            predicted_chord = predict_chord(chord1, interval, chord1_type)
            return JsonResponse({'predicted_chord': predicted_chord})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Invalid request method.'}, status=405)
