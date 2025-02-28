import os
RUN = "/home/xianglin/git_space/DeepVisualInsight/eval/batch_run.py"
RANKINGS_CORR = "/home/xianglin/projects/git_space/DeepVisualInsight/eval/ranking_corr.py"

# DeepView related
# for i in range(1, 11, 1):
#     os.system("python run.py --content_path E:\\DVI_exp_data\\DeepViewExp\\multi_run\\{}\\cifar10 --epoch_start 40 --epoch_end 200 --epoch_period 40 --resolution 100 --embedding_dim 512 --cuda True -a 0.6 -t 0.3 --num_class 10 --split -1 --temporal 3 --preprocess 0".format(i))
# for i in range(1, 11, 1):
#     os.system("python run.py --content_path E:\\DVI_exp_data\\DeepViewExp\\multi_run\\{}\\mnist --epoch_start 4 --epoch_end 20 --epoch_period 4 --resolution 100 --embedding_dim 512 --cuda True -a 0.5 -t 0.02 --num_class 10 --split -1 --temporal 3 --preprocess 0".format(i))
# for i in range(1, 11, 1):
#     os.system("python run.py --content_path E:\\DVI_exp_data\\DeepViewExp\\multi_run\\{}\\fmnist --epoch_start 10 --epoch_end 50 --epoch_period 10 --resolution 100 --embedding_dim 512 --cuda True -a 0.5 -t 0.1 --num_class 10 --split -1 --temporal 3 --preprocess 0".format(i))
#
# for i in range(1, 11, 1):
#     os.system("python run.py --content_path E:\\DVI_exp_data\\DeepViewExp\\multi_run\\{}\\resnet50 --epoch_start 40 --epoch_end 200 --epoch_period 40 --resolution 100 --embedding_dim 2048 --cuda True -a 0.6 -t 0.15 --num_class 10 --split -1 --temporal 3 --preprocess 0".format(i))

# DVI exp
# cifar10, different strategies:
# non transfer, transfer, step2
# os.system("python run.py --content_path E:\\DVI_exp_data\\TemporalExp\\resnet18_cifar10 --epoch_start 1 --epoch_end 7 --epoch_period 1 --resolution 100 --embedding_dim 512 --cuda True -a 0.6 -t 0.3 --num_class 10 --split -1 --temporal 1 --preprocess 1")
# os.system("python run.py --content_path E:\\DVI_exp_data\\TemporalExp\\resnet18_cifar10 --epoch_start 1 --epoch_end 7 --epoch_period 1 --resolution 100 --embedding_dim 512 --cuda True -a 0.6 -t 0.3 --num_class 10 --split -1 --temporal 2 --preprocess 0")
# os.system("python {} --content_path /home/xianglin/projects/DVI_data/resnet18_cifar10 --epoch_start 1 --epoch_end 200 --epoch_period 1 --resolution 100 --embedding_dim 512 --cuda True -a 0.6 -t 0.3 --num_class 10 --split -1 --temporal 3 --preprocess 0".format(RUN))
#
# os.system("python run.py --content_path E:\\DVI_exp_data\\TemporalExp\\resnet18_mnist --epoch_start 1 --epoch_end 7 --epoch_period 1 --resolution 100 --embedding_dim 512 --cuda True -a 0.5 -t 0.02 --num_class 10 --split -1 --temporal 1 --preprocess 1")
# os.system("python run.py --content_path E:\\DVI_exp_data\\TemporalExp\\resnet18_mnist --epoch_start 1 --epoch_end 7 --epoch_period 1 --resolution 100 --embedding_dim 512 --cuda True -a 0.5 -t 0.02 --num_class 10 --split -1 --temporal 2 --preprocess 0")
# os.system("python {} --content_path /home/xianglin/projects/DVI_data/resnet18_mnist --epoch_start 1 --epoch_end 20 --epoch_period 1 --resolution 100 --embedding_dim 512 --cuda True -a 0.5 -t 0.02 --num_class 10 --split -1 --temporal 3 --preprocess 0".format(RUN))
#
# os.system("python run.py --content_path E:\\DVI_exp_data\\TemporalExp\\resnet18_fmnist --epoch_start 1 --epoch_end 7 --epoch_period 1 --resolution 100 --embedding_dim 512 --cuda True -a 0.5 -t 0.1 --num_class 10 --split -1 --temporal 1 --preprocess 1")
# os.system("python run.py --content_path E:\\DVI_exp_data\\TemporalExp\\resnet18_fmnist --epoch_start 1 --epoch_end 7 --epoch_period 1 --resolution 100 --embedding_dim 512 --cuda True -a 0.5 -t 0.1 --num_class 10 --split -1 --temporal 2 --preprocess 0")
# os.system("python {} --content_path /home/xianglin/projects/DVI_data/resnet18_fmnist --epoch_start 1 --epoch_end 50 --epoch_period 1 --resolution 100 --embedding_dim 512 --cuda True -a 0.5 -t 0.1 --num_class 10 --split -1 --temporal 3 --preprocess 0".format(RUN))
#
# os.system("python run.py --content_path E:\\DVI_exp_data\\TemporalExp\\resnet50_cifar10 --epoch_start 1 --epoch_end 7 --epoch_period 1 --resolution 100 --embedding_dim 2048 --cuda True -a 0.6 -t 0.15 --num_class 10 --split -1 --temporal 1 --preprocess 1")
# os.system("python run.py --content_path E:\\DVI_exp_data\\TemporalExp\\resnet50_cifar10 --epoch_start 1 --epoch_end 7 --epoch_period 1 --resolution 100 --embedding_dim 2048 --cuda True -a 0.6 -t 0.15 --num_class 10 --split -1 --temporal 2 --preprocess 0")
# os.system("python run.py --content_path E:\\DVI_exp_data\\TemporalExp\\resnet50_cifar10 --epoch_start 1 --epoch_end 7 --epoch_period 1 --resolution 100 --embedding_dim 2048 --cuda True -a 0.6 -t 0.15 --num_class 10 --split -1 --temporal 3 --preprocess 0")

# os.system("python run.py --content_path E:\\DVI_exp_data\\TemporalExp\\resnet18_emnist --epoch_start 0 --epoch_end 11 --epoch_period 1 --resolution 100 --embedding_dim 512 --cuda True -a 0. -t 0.02 --num_class 10 --split -1 --temporal 1 --preprocess 1")
# os.system("python run.py --content_path E:\\DVI_exp_data\\TemporalExp\\resnet18_emnist --epoch_start 0 --epoch_end 11 --epoch_period 1 --resolution 100 --embedding_dim 512 --cuda True -a 0. -t 0.02 --num_class 10 --split -1 --temporal 2 --preprocess 0")
# os.system("python run.py --content_path E:\\DVI_exp_data\\TemporalExp\\resnet18_emnist --epoch_start 0 --epoch_end 11 --epoch_period 1 --resolution 100 --embedding_dim 512 --cuda True -a 0.3 -t 0.02 --num_class 10 --split -1 --temporal 3 --preprocess 1")

# ranking corr
# os.system("python {} --content_path /home/xianglin/projects/DVI_data/resnet18_cifar10 --epoch_start 40 --epoch_end 200 --epoch_period 1 --resolution 100 --embedding_dim 512 --cuda True -a 0.6 -t 0.3 --num_class 10 --split -1 --temporal 3 --preprocess 1".format(RANKINGS_CORR))
# os.system("python {} --content_path /home/xianglin/projects/DVI_data/resnet18_mnist --epoch_start 1 --epoch_end 20 --epoch_period 1 --resolution 100 --embedding_dim 512 --cuda True -a 0.5 -t 0.02 --num_class 10 --split -1 --temporal 3 --preprocess 1".format(RANKINGS_CORR))
# os.system("python {} --content_path /home/xianglin/projects/DVI_data/resnet18_fmnist --epoch_start 1 --epoch_end 50 --epoch_period 1 --resolution 100 --embedding_dim 512 --cuda True -a 0.5 -t 0.1 --num_class 10 --split -1 --temporal 3 --preprocess 1".format(RANKINGS_CORR))

# baseline
# attention, temporal, complex construction
# os.system("python run.py --content_path E:\\DVI_exp_data\\resnet18_cifar10 --epoch_start 40 --epoch_end 200 --epoch_period 40 --resolution 100 --embedding_dim 512 --cuda True -a 0.6 -t 0.3 --num_class 10 --split -1 --preprocess 1 --parametricUmap 1 --temporal 2 --attention 0")
# os.system("python run.py --content_path E:\\DVI_exp_data\\resnet18_cifar10 --epoch_start 40 --epoch_end 200 --epoch_period 40 --resolution 100 --embedding_dim 512 --cuda True -a 0.6 -t 0.7 --num_class 10 --split -1 --preprocess 1 --parametricUmap 1 --temporal 2 --attention 1")
# os.system("python run.py --content_path E:\\DVI_exp_data\\resnet18_cifar10 --epoch_start 40 --epoch_end 200 --epoch_period 40 --resolution 100 --embedding_dim 512 --cuda True -a 0.6 -t 0.3 --num_class 10 --split -1 --preprocess 1 --parametricUmap 1 --temporal 3 --attention 0")
# os.system("python run.py --content_path E:\\DVI_exp_data\\resnet18_cifar10 --epoch_start 40 --epoch_end 200 --epoch_period 40 --resolution 100 --embedding_dim 512 --cuda True -a 0.6 -t 0.3 --num_class 10 --split -1 --preprocess 1 --parametricUmap 0 --temporal 2 --attention 0")

# os.system("python run.py --content_path E:\\DVI_exp_data\\resnet18_mnist --epoch_start 4 --epoch_end 20 --epoch_period 4 --resolution 100 --embedding_dim 512 --cuda True -a 0.5 -t 0.02 --num_class 10 --split -1 --preprocess 1 --parametricUmap 1 --temporal 2 --attention 0")
# os.system("python run.py --content_path E:\\DVI_exp_data\\resnet18_mnist --epoch_start 4 --epoch_end 20 --epoch_period 4 --resolution 100 --embedding_dim 512 --cuda True -a 0.5 -t 0.02 --num_class 10 --split -1 --preprocess 1 --parametricUmap 1 --temporal 2 --attention 1")
# os.system("python run.py --content_path E:\\DVI_exp_data\\resnet18_mnist --epoch_start 4 --epoch_end 20 --epoch_period 4 --resolution 100 --embedding_dim 512 --cuda True -a 0.5 -t 0.02 --num_class 10 --split -1 --preprocess 1 --parametricUmap 1 --temporal 3 --attention 0")
# os.system("python run.py --content_path E:\\DVI_exp_data\\resnet18_mnist --epoch_start 4 --epoch_end 20 --epoch_period 4 --resolution 100 --embedding_dim 512 --cuda True -a 0.5 -t 0.02 --num_class 10 --split -1 --preprocess 1 --parametricUmap 0 --temporal 2 --attention 0")
#
# os.system("python run.py --content_path E:\\DVI_exp_data\\resnet18_fmnist --epoch_start 10 --epoch_end 50 --epoch_period 10 --resolution 100 --embedding_dim 512 --cuda True -a 0.5 -t 0.1 --num_class 10 --split -1 --preprocess 1 --parametricUmap 1 --temporal 2 --attention 0")
# os.system("python run.py --content_path E:\\DVI_exp_data\\resnet18_fmnist --epoch_start 10 --epoch_end 50 --epoch_period 10 --resolution 100 --embedding_dim 512 --cuda True -a 0.5 -t 0.1 --num_class 10 --split -1 --preprocess 1 --parametricUmap 1 --temporal 2 --attention 1")
# os.system("python run.py --content_path E:\\DVI_exp_data\\resnet18_fmnist --epoch_start 10 --epoch_end 50 --epoch_period 10 --resolution 100 --embedding_dim 512 --cuda True -a 0.5 -t 0.1 --num_class 10 --split -1 --preprocess 1 --parametricUmap 1 --temporal 3 --attention 0")
# os.system("python run.py --content_path E:\\DVI_exp_data\\resnet18_fmnist --epoch_start 10 --epoch_end 50 --epoch_period 10 --resolution 100 --embedding_dim 512 --cuda True -a 0.5 -t 0.1 --num_class 10 --split -1 --preprocess 1 --parametricUmap 0 --temporal 2 --attention 0")

# os.system("python {} --content_path /home/xianglin/projects/DVI_data/resnet18_mnist --epoch_start 1 --epoch_end 20 --epoch_period 1 --resolution 100 --embedding_dim 512 --cuda True -a 0.5 -t 0.02 --num_class 10 --split -1 --temporal 3 --parametricUmap 1 --preprocess 0 --stage 3".format(RANKINGS_CORR))
# os.system("python {} --content_path /home/xianglin/projects/DVI_data/resnet18_fmnist --epoch_start 1 --epoch_end 50 --epoch_period 1 --resolution 100 --embedding_dim 512 --cuda True -a 0.5 -t 0.1 --num_class 10 --split -1 --temporal 3 --parametricUmap 1 --preprocess 0 --stage 3".format(RANKINGS_CORR))
# os.system("python {} --content_path /home/xianglin/projects/DVI_data/resnet18_cifar10 --epoch_start 1 --epoch_end 200 --epoch_period 1 --resolution 100 --embedding_dim 512 --cuda True -a 0.6 -t 0.3 --num_class 10 --split -1 --temporal 3 --parametricUmap 1 --preprocess 0 --stage 3".format(RANKINGS_CORR))

# os.system("python {} --content_path /home/xianglin/projects/DVI_data/resnet18_cifar10 --epoch_start 1 --epoch_end 200 --epoch_period 99 --resolution 100 --embedding_dim 512 --cuda True -a 0.6 -t 0.3 --num_class 10 --split -1 --temporal 1 --parametricUmap 1 --preprocess 0 --attention 0".format(RUN))
# os.system("python {} --content_path /home/xianglin/projects/DVI_data/resnet18_mnist --epoch_start 1 --epoch_end 20 --epoch_period 1 --resolution 100 --embedding_dim 512 --cuda True -a 0.5 -t 0.02 --num_class 10 --split -1 --temporal 3 --parametricUmap 1 --preprocess 0 --attention 0".format(RUN))
# os.system("python {} --content_path /home/xianglin/projects/DVI_data/resnet18_cifar10 --epoch_start 1 --epoch_end 200 --epoch_period 1 --resolution 100 --embedding_dim 512 --cuda True -a 0.6 -t 0.3 --num_class 10 --split -1 --temporal 3 --parametricUmap 1 --preprocess 0 --attention 0".format(RUN))
# os.system("python {} --content_path /home/xianglin/projects/DVI_data/resnet18_fmnist --epoch_start 1 --epoch_end 50 --epoch_period 1 --resolution 100 --embedding_dim 512 --cuda True -a 0.5 -t 0.1 --num_class 10 --split -1 --temporal 3 --parametricUmap 1 --preprocess 0 --attention 0".format(RUN))


# os.system("python {} --content_path /home/xianglin/projects/DVI_data/vgg19_bn_speechcomment --num_classes 12 --model vgg19_bn --epoch_start 1 --epoch_end 50 --epoch_period 1 --resolution 200 --embedding_dim 512 --cuda True -a 0.5 --num_class 12 --split -1 --temporal 3 --parametricUmap 1 --preprocess 1 --attention 0".format(RUN))

# DVI on noise dataset
# os.system("python {} --content_path /home/xianglin/projects/DVI_data/noisy/symmetric/cifar10/20 --num_classes 10 --model resnet18 --epoch_start 1 --epoch_end 200 --epoch_period 1 --resolution 200 --embedding_dim 512 --cuda True -a 0.5  --temporal 3 --parametricUmap 1 --preprocess 1 --attention 0".format(RUN))
# os.system("python {} --content_path /home/xianglin/projects/DVI_data/noisy/symmetric/cifar10/10 --num_classes 10 --model resnet18 --epoch_start 1 --epoch_end 200 --epoch_period 1 --resolution 200 --embedding_dim 512 --cuda True -a 0.5  --temporal 3 --parametricUmap 1 --preprocess 1 --attention 0".format(RUN))
# os.system("python {} --content_path /home/xianglin/projects/DVI_data/noisy/symmetric/cifar10/5 --num_classes 10 --model resnet18 --epoch_start 1 --epoch_end 200 --epoch_period 1 --resolution 200 --embedding_dim 512 --cuda True -a 0.5  --temporal 3 --parametricUmap 1 --preprocess 1 --attention 0".format(RUN))

# os.system("python {} --content_path /home/xianglin/projects/DVI_data/noisy/symmetric/mnist/20 --num_classes 10 --model resnet18 --epoch_start 1 --epoch_end 15 --epoch_period 1 --resolution 200 --embedding_dim 512 --cuda True -a 0.5  --temporal 3 --parametricUmap 1 --preprocess 1 --attention 0".format(RUN))
# os.system("python {} --content_path /home/xianglin/projects/DVI_data/noisy/symmetric/mnist/10 --num_classes 10 --model resnet18 --epoch_start 1 --epoch_end 15 --epoch_period 1 --resolution 200 --embedding_dim 512 --cuda True -a 0.5  --temporal 3 --parametricUmap 1 --preprocess 1 --attention 0".format(RUN))
# os.system("python {} --content_path /home/xianglin/projects/DVI_data/noisy/symmetric/mnist/5 --num_classes 10 --model resnet18 --epoch_start 1 --epoch_end 15 --epoch_period 1 --resolution 200 --embedding_dim 512 --cuda True -a 0.5  --temporal 3 --parametricUmap 1 --preprocess 1 --attention 0".format(RUN))

# os.system("python {} --content_path /home/xianglin/projects/DVI_data/noisy/symmetric/fmnist/20 --num_classes 10 --model resnet18 --epoch_start 1 --epoch_end 50 --epoch_period 1 --resolution 200 --embedding_dim 512 --cuda True -a 0.5  --temporal 3 --parametricUmap 1 --preprocess 1 --attention 0".format(RUN))
# os.system("python {} --content_path /home/xianglin/projects/DVI_data/noisy/symmetric/fmnist/10 --num_classes 10 --model resnet18 --epoch_start 1 --epoch_end 50 --epoch_period 1 --resolution 200 --embedding_dim 512 --cuda True -a 0.5  --temporal 3 --parametricUmap 1 --preprocess 1 --attention 0".format(RUN))
# os.system("python {} --content_path /home/xianglin/projects/DVI_data/noisy/symmetric/fmnist/5 --num_classes 10 --model resnet18 --epoch_start 1 --epoch_end 50 --epoch_period 1 --resolution 200 --embedding_dim 512 --cuda True -a 0.5  --temporal 3 --parametricUmap 1 --preprocess 1 --attention 0".format(RUN))

# # DVI on active learning dataset
# os.system("python {} --content_path /home/xianglin/projects/DVI_data/active_learning/random/resnet18/CIFAR10/10 --num_classes 10 --model resnet18 --epoch_start 1 --epoch_end 200 --epoch_period 1 --resolution 200 --embedding_dim 512 --cuda True -a 0.5 --temporal 3 --parametricUmap 1 --preprocess 1 --attention 0".format(RUN))
# os.system("python {} --content_path /home/xianglin/projects/DVI_data/active_learning/random/resnet18/CIFAR10/20 --num_classes 10 --model resnet18 --epoch_start 1 --epoch_end 200 --epoch_period 1 --resolution 200 --embedding_dim 512 --cuda True -a 0.5 --temporal 3 --parametricUmap 1 --preprocess 1 --attention 0".format(RUN))
# os.system("python {} --content_path /home/xianglin/projects/DVI_data/active_learning/random/resnet18/CIFAR10/30 --num_classes 10 --model resnet18 --epoch_start 1 --epoch_end 200 --epoch_period 1 --resolution 200 --embedding_dim 512 --cuda True -a 0.5 --temporal 3 --parametricUmap 1 --preprocess 1 --attention 0".format(RUN))

# os.system("python {} --content_path /home/xianglin/projects/DVI_data/active_learning/random/resnet18/MNIST/10 --num_classes 10 --model resnet18 --epoch_start 1 --epoch_end 15 --epoch_period 1 --resolution 200 --embedding_dim 512 --cuda True -a 0.5 --temporal 3 --parametricUmap 1 --preprocess 1 --attention 0".format(RUN))
# os.system("python {} --content_path /home/xianglin/projects/DVI_data/active_learning/random/resnet18/MNIST/20 --num_classes 10 --model resnet18 --epoch_start 1 --epoch_end 15 --epoch_period 1 --resolution 200 --embedding_dim 512 --cuda True -a 0.5 --temporal 3 --parametricUmap 1 --preprocess 1 --attention 0".format(RUN))
# os.system("python {} --content_path /home/xianglin/projects/DVI_data/active_learning/random/resnet18/MNIST/30 --num_classes 10 --model resnet18 --epoch_start 1 --epoch_end 15 --epoch_period 1 --resolution 200 --embedding_dim 512 --cuda True -a 0.5 --temporal 3 --parametricUmap 1 --preprocess 1 --attention 0".format(RUN))

# os.system("python {} --content_path /home/xianglin/projects/DVI_data/active_learning/random/resnet18/FMNIST/10 --num_classes 10 --model resnet18 --epoch_start 1 --epoch_end 50 --epoch_period 1 --resolution 200 --embedding_dim 512 --cuda True -a 0.5 --temporal 3 --parametricUmap 1 --preprocess 1 --attention 0".format(RUN))
# os.system("python {} --content_path /home/xianglin/projects/DVI_data/active_learning/random/resnet18/FMNIST/20 --num_classes 10 --model resnet18 --epoch_start 1 --epoch_end 50 --epoch_period 1 --resolution 200 --embedding_dim 512 --cuda True -a 0.5 --temporal 3 --parametricUmap 1 --preprocess 1 --attention 0".format(RUN))
# os.system("python {} --content_path /home/xianglin/projects/DVI_data/active_learning/random/resnet18/FMNIST/30 --num_classes 10 --model resnet18 --epoch_start 1 --epoch_end 50 --epoch_period 1 --resolution 200 --embedding_dim 512 --cuda True -a 0.5 --temporal 3 --parametricUmap 1 --preprocess 1 --attention 0".format(RUN))


os.system("python {} --content_path /home/xianglin/data/convnet_mnist --num_classes 10 --model convnet --epoch_start 1 --epoch_end 15 --epoch_period 1 --resolution 200 --embedding_dim 512 --cuda True -a 0.5  --temporal 3 --parametricUmap 1 --preprocess 0 --attention 0 --n_neighbors 15".format(RUN))