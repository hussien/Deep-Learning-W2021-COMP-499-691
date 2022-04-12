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
<br>
<h1> project Conclusion </h1>
From this project, the team realized that learning from
limited data is a very interesting but challenging experience.
In challenge 1, our team was able to perform well with
the top result submission on CodaLab, as well as developed
and implemented 2 models which give quite similar perfor-
mance, although there are still things to be improve further
if time allows (such as making the SVM classifier in the
third approach fully differentiable as in [30]).
Learning with limited data without pre-trainning like
in the challenge 1’s context showed that regardless of the
model and approach, the achieved performance is still be-
low 50% test accuracy, which proved than transfer learn-
ing approaches in challenge 2 are the proper way to con-
quer this kind of limited data challenge (excepted when
the data in new domain has too much different character-
istics compared to the source domain, where pre-trained
approach would not help and the challenge 1’s context is
un-avoidable).
For challenge 2, the objective is to show how deep mod-
els like VGG16, ResNet and EfficientNetB0 can be used on
very small size data without large margin of overfitting and
with great performance. All of the models are pre-trained
on ImageNet. According to the experiments, most of the
models had performed well, specially when apply data aug-
mentation, dropout, and fine-tuning.
Overall, the experiments proved that deep models can be used to generalize well very small datasets with proper
modifications and limited resources.
