from keras import Model
from keras.layers import LSTM, Input, Dense, LeakyReLU, BatchNormalization, Dropout


class ChessMovePrediction(Model):
    def __init__(self, input_dim):
        super().__init__(input_dim)
        self.input_dim = input_dim

        self._build()

    def _build(self):
        model_input = Input(input_dim=self.input_dim, name='input')
        x = model_input

        x = Dense(128)(x)
        x = LeakyReLU()(x)

        x = LSTM(128, return_sequences=True)
        x = BatchNormalization()(x)
        x = LeakyReLU()(x)
        x = Dropout(rate=0.25)

        x = Dense(256)(x)
        x = LeakyReLU()(x)

        x = LSTM(256, return_sequences=True)
        x = BatchNormalization()(x)
        x = LeakyReLU()(x)
        x = Dropout(rate=0.25)

        x = Dense(256)(x)
        x = LeakyReLU()(x)

        x = LSTM(256, return_sequences=True)
        x = BatchNormalization()(x)
        x = LeakyReLU()(x)
        x = Dropout(rate=0.25)

        model_output = x

        self.model = Model(model_input, model_output)

