import tensorflow as tf
from tensorflow.keras import layers

def build_vae(input_dim):
    encoder_inputs = layers.Input(shape=(input_dim,))
    x = layers.Dense(32, activation='relu')(encoder_inputs)
    x = layers.Dense(16, activation='relu')(x)
    z_mean = layers.Dense(8)(x)
    z_log_var = layers.Dense(8)(x)

    encoder = tf.keras.Model(encoder_inputs, [z_mean, z_log_var], name='encoder')

    latent_inputs = layers.Input(shape=(8,))
    x = layers.Dense(16, activation='relu')(latent_inputs)
    x = layers.Dense(32, activation='relu')(x)
    decoder_outputs = layers.Dense(input_dim, activation='sigmoid')(x)

    decoder = tf.keras.Model(latent_inputs, decoder_outputs, name='decoder')

    class VAE(tf.keras.Model):
        def __init__(self, encoder, decoder, **kwargs):
            super(VAE, self).__init__(**kwargs)
            self.encoder = encoder
            self.decoder = decoder

        def call(self, inputs):
            z_mean, z_log_var = self.encoder(inputs)
            z = z_mean + tf.exp(0.5 * z_log_var) * tf.random.normal(tf.shape(z_mean))
            reconstructed = self.decoder(z)
            return reconstructed

    vae = VAE(encoder, decoder)
    vae.compile(optimizer='adam', loss=vae_loss)
    return vae

def vae_loss(inputs, outputs):
    reconstruction_loss = tf.losses.binary_crossentropy(inputs, outputs)
    return reconstruction_loss

def train_vae(vae, X_train, X_test, epochs=100, batch_size=32):
    vae.fit(X_train, epochs=epochs, batch_size=batch_size, validation_data=(X_test, None))
    return vae