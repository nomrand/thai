from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import os
import sys

import numpy as np
import tensorflow as tf

from . import label_image
from . import retrain

toppath = os.path.dirname(os.path.dirname(__file__))
model_file = os.path.join(toppath, "model", "trained_model.pb")
label_file = os.path.join(toppath, "model", "trained_label.txt")
modified = os.path.join(toppath, "model", "modified")
train_images = os.path.join(toppath, "train_images")


def predict(imgpath):
    file_name = imgpath
    input_height = 299
    input_width = 299
    input_mean = 0
    input_std = 255
    input_layer = "input"
    output_layer = "InceptionV3/Predictions/Reshape_1"
    if os.path.exists(modified):
        input_layer = "Placeholder"
        output_layer = "final_result"

    graph = label_image.load_graph(model_file)
    t = label_image.read_tensor_from_image_file(
        file_name,
        input_height=input_height,
        input_width=input_width,
        input_mean=input_mean,
        input_std=input_std)

    input_name = "import/" + input_layer
    output_name = "import/" + output_layer
    input_operation = graph.get_operation_by_name(input_name)
    output_operation = graph.get_operation_by_name(output_name)

    with tf.compat.v1.Session(graph=graph) as sess:
        results = sess.run(output_operation.outputs[0], {
            input_operation.outputs[0]: t
        })
    results = np.squeeze(results)

    top_k = results.argsort()[:][::-1]
    labels = label_image.load_labels(label_file)
    results_sorted = []
    for i in top_k:
        results_sorted.append((str(labels[i]), float(results[i])))
        # print(labels[i], results[i])

    return results_sorted


def retain():
    # create modified-flag file
    with open(modified, "w") as f:
        f.write(modified)

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--image_dir',
        type=str,
        default=train_images,
        help='Path to folders of labeled images.'
    )
    parser.add_argument(
        '--output_graph',
        type=str,
        default=model_file,
        help='Where to save the trained graph.'
    )
    parser.add_argument(
        '--intermediate_output_graphs_dir',
        type=str,
        default=os.path.join(toppath, '.result/intermediate_graph'),
        help='Where to save the intermediate graphs.'
    )
    parser.add_argument(
        '--intermediate_store_frequency',
        type=int,
        default=0,
        help="""\
         How many steps to store intermediate graph. If "0" then will not
         store.\
      """
    )
    parser.add_argument(
        '--output_labels',
        type=str,
        default=label_file,
        help='Where to save the trained graph\'s labels.'
    )
    parser.add_argument(
        '--summaries_dir',
        type=str,
        default=os.path.join(toppath, '.result/retrain_logs'),
        help='Where to save summary logs for TensorBoard.'
    )
    parser.add_argument(
        '--how_many_training_steps',
        type=int,
        # default=4000,
        default=400,
        help='How many training steps to run before ending.'
    )
    parser.add_argument(
        '--learning_rate',
        type=float,
        default=0.01,
        help='How large a learning rate to use when training.'
    )
    parser.add_argument(
        '--testing_percentage',
        type=int,
        default=10,
        help='What percentage of images to use as a test set.'
    )
    parser.add_argument(
        '--validation_percentage',
        type=int,
        default=10,
        help='What percentage of images to use as a validation set.'
    )
    parser.add_argument(
        '--eval_step_interval',
        type=int,
        default=10,
        help='How often to evaluate the training results.'
    )
    parser.add_argument(
        '--train_batch_size',
        type=int,
        default=100,
        help='How many images to train on at a time.'
    )
    parser.add_argument(
        '--test_batch_size',
        type=int,
        default=-1,
        help="""\
      How many images to test on. This test set is only used once, to evaluate
      the final accuracy of the model after training completes.
      A value of -1 causes the entire test set to be used, which leads to more
      stable results across runs.\
      """
    )
    parser.add_argument(
        '--validation_batch_size',
        type=int,
        default=100,
        help="""\
      How many images to use in an evaluation batch. This validation set is
      used much more often than the test set, and is an early indicator of how
      accurate the model is during training.
      A value of -1 causes the entire validation set to be used, which leads to
      more stable results across training iterations, but may be slower on large
      training sets.\
      """
    )
    parser.add_argument(
        '--print_misclassified_test_images',
        default=False,
        help="""\
      Whether to print out a list of all misclassified test images.\
      """,
        action='store_true'
    )
    parser.add_argument(
        '--bottleneck_dir',
        type=str,
        default=os.path.join(toppath, '.result/bottleneck'),
        help='Path to cache bottleneck layer values as files.'
    )
    parser.add_argument(
        '--final_tensor_name',
        type=str,
        default='final_result',
        help="""\
      The name of the output classification layer in the retrained graph.\
      """
    )
    parser.add_argument(
        '--flip_left_right',
        default=False,
        help="""\
      Whether to randomly flip half of the training images horizontally.\
      """,
        action='store_true'
    )
    parser.add_argument(
        '--random_crop',
        type=int,
        default=0,
        help="""\
      A percentage determining how much of a margin to randomly crop off the
      training images.\
      """
    )
    parser.add_argument(
        '--random_scale',
        type=int,
        default=0,
        help="""\
      A percentage determining how much to randomly scale up the size of the
      training images by.\
      """
    )
    parser.add_argument(
        '--random_brightness',
        type=int,
        default=0,
        help="""\
      A percentage determining how much to randomly multiply the training image
      input pixels up or down by.\
      """
    )
    parser.add_argument(
        '--tfhub_module',
        type=str,
        default=(
            'https://tfhub.dev/google/imagenet/inception_v3/feature_vector/3'),
        help="""\
      Which TensorFlow Hub module to use. For more options,
      search https://tfhub.dev for image feature vector modules.\
      """)
    parser.add_argument(
        '--saved_model_dir',
        type=str,
        default='',
        help='Where to save the exported graph.')
    parser.add_argument(
        '--logging_verbosity',
        type=str,
        default='INFO',
        choices=['DEBUG', 'INFO', 'WARN', 'ERROR', 'FATAL'],
        help='How much logging output should be produced.')
    parser.add_argument(
        '--checkpoint_path',
        type=str,
        default=os.path.join(toppath, '.result/_retrain_checkpoint'),
        help='Where to save checkpoint files.'
    )
    retrain.FLAGS, unparsed = parser.parse_known_args()
    tf.compat.v1.app.run(main=retrain.main, argv=[sys.argv[0]] + unparsed)
