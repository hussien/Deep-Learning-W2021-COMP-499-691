<h1>Course Content</h1>
Jan 18 - Introduction, Definitions, Universal Approx, Depth
<br>
Jan 25 - Backpropagation and AD software, Introduction to Pytorch
<br>
Feb 1 - Optimization for Deep Learning
<br>
Feb 8 - Regularization and Implicit Regularization Methods
<br>
Feb 15 - CNNs and Visual Representation Learning
<br>
Feb 22 - Interpertability of DNN/CNNs (Guest Lecture)
<br>
March 1 - Generalization and Adversarial examples
<br>
March 8 - RNNs, Sequence models, Seq2Seq
<br>
March 15 - Attention and Self-Attention
<br>
March 22 - Multi-task and Transfer Learning
<br>
March 29 - Deep Generative Models
<br>
April 12 - Deep Metric Learning
<br>
April 19 - Self-Supervised Learning
<br>
April 21 - Deep Reinforcement Learning Primer (Time Permitting)

<h1>Course Project</h1>
<br>
<p>Challenge 1: Learning from Limited data</p>
Few-sample learning on the CIFAR-10 dataset. We will consider a dataset with only 100 samples. For testing a larger dataset will be used (e.g. the CIFAR-10 test set).
Your job will be to train on 100 randomly selected (but class balanced) samples from the CIFAR-10 training set. You may not use any model trained on external data or any external data for your answer. On the other hand you may consider any kind of approach without constraint including non-deep learning methods as long as it only utilizes the 100 examples for training.
Final evaluation: In the final evaluation your model will be run on 5 random instances of this problem. Evaluation will occur both on the CIFAR-10 test set and other data which will not be
revaled at the moment. It may also be run on a similar drop in dataset with the same size images and number of output classes.
<br>
<br>
<p>Challenge 2: Learning with Limited Data w/ External Data:</p>
Consider the same exercise but now with the ability to use an external data or models not trained on CIFAR-10 from the pytorch model repository or to train your own model on external data (you may not train a model on CIFAR-10 dataset or any derivative using these images. You may consider for example various forms of finetuning, meta-learning, semi-supervised learning with an external dataset and other related ideas.
