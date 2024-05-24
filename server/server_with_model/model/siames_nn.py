from scipy.signal import savgol_filter
import numpy as np
from keras.layers import Input, Dense, Lambda, Conv1D, GlobalMaxPooling1D
from keras.models import Sequential, Model
import keras.backend as K
import os

os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'


class Siames_NN():
    def __init__(self) -> None:
        self.model = self.__load_siames_nn()

    def __load_siames_nn(self):
        def create_inner_network(self):
            model_cnn = Sequential()
            model_cnn.add(Conv1D(512, 5,  padding='valid', activation='relu'))
            model_cnn.add(Conv1D(256, 5,  padding='valid', activation='relu'))
            model_cnn.add(Conv1D(128, 5,  padding='valid', activation='relu'))
            model_cnn.add(Conv1D(64, 5,  padding='valid', activation='relu'))
            model_cnn.add(GlobalMaxPooling1D())
            model_cnn.add(Dense(units=32, activation='relu',
                          kernel_regularizer='l2'))
            model_cnn.add(Dense(16, activation='softmax'))
            return model_cnn

        input_shape = 500
        inner_network = create_inner_network(input_shape)
        input_left = Input(shape=(input_shape, 1))
        input_right = Input(shape=(input_shape, 1))
        left_network = inner_network(input_left)
        right_network = inner_network(input_right)

        def euclidean_distance(vects):
            v1, v2 = vects
            return K.sqrt(K.sum(K.square(v1 - v2), axis=1, keepdims=True))

        def euclidean_distance_output_shape(shapes):
            shape1, shape2 = shapes
            return (shape1[0], 1)
        distance = Lambda(function=euclidean_distance, output_shape=euclidean_distance_output_shape)(
            [left_network, right_network])
        model = Model(inputs=[input_left, input_right], outputs=distance)
        model.load_weights(
            '.\server_with_model\model\weight_v2.h5', skip_mismatch=False)
        return model

    def prepare_ecg(self, ecg):
        arr = list()
        for i in ecg:
            arr.append((i-128)/255)
        # Применение фильтра Савицкого-Голея для сглаживания
        ecg_smooth = savgol_filter(arr, 11, 2)

        return ecg_smooth


def predict(ecg_1, ecg_2):
    siames_NN = Siames_NN()
    ecg_1_arr = list(map(int, ecg_1.split(" ")))
    ecg_2_arr = list(map(int, ecg_2.split(" ")))
    ecg_1_arr = siames_NN.prepare_ecg(ecg_1_arr)
    ecg_2_arr = siames_NN.prepare_ecg(ecg_2_arr)
    arr = list()
    arr.append([ecg_1_arr, ecg_2_arr])
    pair = np.array(arr)
    y_pred_my = siames_NN.model.predict(x=[pair[:, 0], pair[:, 1]])
    if y_pred_my[0] < 0.02:
        return True
    else:
        return False
