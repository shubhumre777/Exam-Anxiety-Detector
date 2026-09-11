import torch
import torch.nn as nn
import torchvision.transforms as transforms
import cv2
from PIL import Image

# Define the Neural Network Architecture
class SimpleEmotionCNN(nn.Module):
    def __init__(self):
        super(SimpleEmotionCNN, self).__init__()
        self.conv1 = nn.Conv2d(in_channels=1, out_channels=16, kernel_size=3, padding=1)
        self.relu = nn.ReLU() 
        self.pool = nn.MaxPool2d(kernel_size=2, stride=2) 
        self.fc1 = nn.Linear(16 * 24 * 24, 7) 

    def forward(self, x):
        x = self.conv1(x)
        x = self.relu(x)
        x = self.pool(x)
        x = x.view(-1, 16 * 24 * 24)  # view() means: Reshape the tensor into a different shape without changing its actual data.
        x = self.fc1(x)
        return x

class EmotionDetector:
    def __init__(self):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        
        # Load the Neural Network into memory
        self.model = SimpleEmotionCNN().to(self.device)
        self.model.eval() # Set to evaluation mode

        self.transform = transforms.Compose([
            transforms.Resize((48, 48)),
            transforms.Grayscale(num_output_channels=1),
            transforms.ToTensor(),
            transforms.Normalize((0.5,), (0.5,))
        ])
        
        self.emotions = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']

    def detect(self, face_crop):
        if face_crop is None or face_crop.size == 0:
            return "No Face"
            
        rgb_face = cv2.cvtColor(face_crop, cv2.COLOR_BGR2RGB)
        pil_img = Image.fromarray(rgb_face)
        tensor_img = self.transform(pil_img).unsqueeze(0).to(self.device)
        
        with torch.no_grad(): 
            output = self.model(tensor_img) # Example output : [-1.2, 0.5, 2.8, 0.4, -0.7, 0.2, 0.1]
            _, predicted_idx = torch.max(output, 1)  # _ means we dont want that value .
            emotion_name = self.emotions[predicted_idx.item()]
            
        return emotion_name