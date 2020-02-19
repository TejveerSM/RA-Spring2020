# Segmentation and Masking
 
- The original image is loaded using the PIL's Image library
- Torchvision transforms are used to resize, convert, and normalize the image
- The transformed image is passed through the network to get the segmentation map (of 21 classes)
- The class of interest is people; so, the input image is masked on the predicted pixels of people
- This gives output image with only people on a black background

Useful resources:
- Semantic segmentation Pytorch implementation https://github.com/CSAILVision/semantic-segmentation-pytorch
- Mask R-CNN paper https://arxiv.org/pdf/1703.06870.pdf
- Mask R-CNN implementation https://towardsdatascience.com/computer-vision-instance-segmentation-with-mask-r-cnn-7983502fcad1
- Implementation of Mask R-CNN for Object Detection and Instance Segmentation with applications to OpenStreetMap images and Satellite Imagery https://github.com/matterport/Mask_RCNN
- Images to OpenStreetMap https://github.com/jremillard/images-to-osm
- Mask R-CNN for GRASS GIS https://github.com/ctu-geoforall-lab/i.ann.maskrcnn
- Crowd AI Mapping https://github.com/crowdAI/crowdai-mapping-challenge-mask-rcnn

Pytorch pre-trained models for image segmentation: https://pytorch.org/docs/stable/_modules/torchvision/models/segmentation/segmentation.html
Models: FCN and DeepLabV3