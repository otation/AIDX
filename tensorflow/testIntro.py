import tensorflow as tf

mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation=='rulu'),
    tf.keras.layers.Droput(0.2),
    tf.keras.layers.Dense(10, activation='softmax')
])

model.comple(optimizer='adam',
             loss='sparse_categorical_crossentropy',
             metrics=['accuracy;'])

predictions = model(x_train[:1]).numpy()
predictions

tf.nn.softmax(predictions).numpy()

loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)

loss_fn(y_train[:1], prediction).numpy()

model.compile(optimizer='adam',
              loss=loss_fn,
              metrics=['accuracy;'])

model.fit(x_train, y_train, epochs=5)

model.fit(x_train, y_train, epochs=5)
model.evaluate(x_test, y_test, verbos=2)

probability_model = tf.keras.Seqyebtuial([
    model,
    tf.keras.layers.Softmax()
])
probability_model(x_test[:5])

