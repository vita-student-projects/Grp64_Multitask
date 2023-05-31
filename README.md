# 2D KeyPoints Pose Estimation for humans, animals and vehicles - Group64
Multitasking project : 2D KeyPoints Pose Estimation for animals, humans and vehicles 


# Introduction

The primary objective of this project was to perform 2D keypoints pose estimation for humans, animals and vehicles, which is usually called multitasking (or 
multidomain application). By estimating the pose, we can extract valuable information about the posture, orientation, and movement of these objects. The input is then an
image containing humans, animals or a vehicles and the the output would be the very same picture with 2D keypoints annotations on it. 2D keypoints pose estimation is a computer vision technique that involves identifying and localizing specific points on an object's body or structure. 
These keypoints represent anatomical landmarks such as joints, facial features, or other distinctive parts. By accurately detecting and tracking these keypoints, we can reconstruct and understand the pose or configuration of the object in 2D space. 
In the context of autonomous vehicles, 2D keypoints pose estimation plays a crucial role. By accurately estimating the poses of pedestrians, animals, and other vehicles, autonomous vehicles can better understand their surroundings and make informed decisions. This information enables them to predict and anticipate the movements of different objects, enhancing safety and efficiency on the road.
Our work is based on the existing openpifpaf architecture, a well-established framework for multi-person pose estimation.
To enhance the existing architecture, we aimed to incorporate dynamic weight average (DWA), a generic multitasking method known for improving performance in complex tasks. Additionally, we implemented a new backbone called HRFormer, which we compared to the current backbones (such as ResNets and ShuffleNets) to evaluate its performance.


# Dataset

As stated in the introduction, the model for this project should be able to differentiate among
different classes (or domains): humans, animals and vehicles. Three datasets, labelled with the
2D keypoints, are necessary for each classes. The openpifpaf library is already trained and
tested on each of those classes independently, and the datasets are provided in the library’s
guide.

## For humans : COCO dataset

It is necessary to download the COCO dataset at the following address : https://cocodataset.org//#download. The annotation format is taken as a basis for the other datasets. In other words, anotations from other datasets were converted to the COCO annotation format.

## For animals : Animalpose dataset 

It uses annotations from PASCAL dataset : 
http://host.robots.ox.ac.uk/pascal/VOC/ 
and others created by the authors of Animalpose dataset : 
https://sites.google.com/view/animal-pose/.

The guidelines to download the dataset are on the Openpifpaf library guide :

https://vita-epfl.github.io/openpifpaf/plugins_animalpose.html 

The data are pre-processed with the "voc\_to\_coco" script.

## For vehicles : ApolloCar3D dataset

The dataset is download from :
https://github.com/ApolloScapeAuto/dataset-api/tree/master/car_instance

It can be preprocessed with the script "apollo\_to\_coco" from the Openpifpaf library guide that can be accessed at the following address:

https://vita-epfl.github.io/openpifpaf/plugins_apollocar3d.html

# Our contribution :

As mentioned in the introduction, we decided to implement Dynamic Weight Average (DWA) in the existing OpenPifPaf architecture. It is a method thanks to which wecan adapt the model loss
during training by taking into account the rate of change of each of the haed losses. Weights are indeed computed from the following formula :

![Screenshot 2023-05-31 121635](https://github.com/vita-student-projects/Grp64_Multitask/assets/53184051/48a19673-f9bb-40a1-83a8-e9155933292e)

Where the weights on the right hand side of the formula correspond to the ratio between the head loss k at time t-1 and the head loss at time t-2.
The final loss is then computed as the weighted sum of each of those head losses.

HRFormer backbone was implemented as well to see if it oculd improve the performances of the backbones already available on OpenPifPaf, but since it didn't give much better results,
we decided to rather focus on the implementation of DWA which is a multitasking-specific method. 

# Experimental setup :

## Single Dataset :

The first implementation is done on a single dataset: AnimalPose. There are 6 heads during the training, and DWA is applied to all of them.

The training is continued from a checkpoint trained with Shufflenetv2k30 for 350 epochs on AnimalPose. The results are compared between a classic training and the training with DWA

The metrics are the ones from a classic evaluation on Openpifpaf: AP, AP 0.5, AP 0.75, APM, APL, AR, AR 0.5, AR 0.75, ARL, ARM.

We then wanted to compare the performancesof the model that includes DWA with those of the classical one.

## Multiple Dataset : 

DWA is implemented in the training of three datasets simultaneously: AnimalPose, ApolloCar3D
and Coco. There are 18 heads and DWA is applied to all of them.
The training is continued from a checkpoint trained with Shufflenetv2k30 for 45 epochs on
the three datasets. The results are compared between a classic training and the training with
DWA.
The metrics are once again the ones from a classic evaluation on Openpifpaf: AP, AP 0.5, AP 0.75,
APM, APL, AR, AR 0.5, AR 0.75, ARL, ARM.

## Backbone and number of epochs :

We also need to specify that we decided to train with a Shufflenetv2k30 backbone and not an HRFormer as it was originally planned. We indeed knew Shufflenetv2k30 was performing well,
unlike HRFormer, and we therefore wanted to compare its performance with and without DWA incorporated in the decoder part of the network.

We only managed to train the network up to 45 epochs on SCITAS EPFL clusters, despite a training time of three days. We then trained it for 7 more epochs both with and without DWA tand then compared the performances obtained.

# Results :

## Signle dataset :

A significant improvement is seen on metrics AR and ARL. This can be interpreted as an
improvement of a specific head and therefore on a specific feature, but not of the overall model, which can for instance be interpreted from the ARM metric that didn't really change compared to the classical openpifpaf performance.

![Screenshot 2023-05-31 122429](https://github.com/vita-student-projects/Grp64_Multitask/assets/53184051/4a2f8417-3b3c-4fe7-b17e-d046d89f3a80)

## Multiple datasets : 

The most significant changes are observed on the AnimalPose evaluation. It is the dataset
with the lowest overall scores, around 0.35, and it should be the one changing the most with
the DWA method. However, it is the smallest dataset and this might cause a slight overfit ?
The score of the ApolloCar3D dataset are decreasing, from the baseline to further training.
This might be due to the number of keypoints which is greater in the ApolloCar3D dataset
than in the two other datasets, hence having more feedback and a stronger impact on a low
number of epochs.

![Screenshot 2023-05-31 000004](https://github.com/vita-student-projects/Grp64_Multitask/assets/53184051/b484da57-57da-4dff-a41c-96592eab964d)

# Conclusion :

Our implementation of the Dynamic Weight Average method does not seem to improve the training of a multi-task neural network significantly.

We unfortunately didn't have enough training time to train our models to reach state of the art values, or at least to see if the current method could be improved or not.

