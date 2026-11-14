import torch
import torch.nn as nn

# Autoencoder for SMF Type 100/42 anomaly detection
class SMFAnomalyDetector(nn.Module):
    def __init__(self, input_dim):
        super().__init__()
        # Compress high-dimensional SMF data into a latent space
        self.encoder = nn.Sequential(
            nn.Linear(input_dim, 128),
            nn.ReLU(),
            nn.Linear(128, 32)
        )
        # Attempt to reconstruct the original telemetry
        self.decoder = nn.Sequential(
            nn.Linear(32, 128),
            nn.ReLU(),
            nn.Linear(128, input_dim)
        )

    def forward(self, x):
        latent = self.encoder(x)
        reconstructed = self.decoder(latent)
        return reconstructed
