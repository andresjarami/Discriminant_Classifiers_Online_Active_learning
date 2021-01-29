%Normalize each data vector to have L2-norm equal to 1  
clear all
load YaleB_32x32.mat
fea = NormalizeFea(fea);

a=randperm(size(gnd,1));
trainIdx=a(1,1:500);
testIdx=a(1,1:500);
a=randperm(size(trainIdx,2));
LabelIdx=a(1,1:200);

feaTrain = fea(trainIdx, :);  
gndTrain = gnd(trainIdx);  
 
options = [];  
options.Metric = 'Cosine';  
options.NeighborMode = 'KNN';  
options.WeightMode = 'Cosine';  
options.k = 2;  
options.bSelfConnected = 0;  
W = constructW(feaTrain,options);  
 
options = [];  
options.W = W;  
options.ReguBeta = 1; 
options.ReguAlpha = 0.1; 
 
semisplit = false(size(trainIdx));  
semisplit(LabelIdx) = true;  
 
[eigvector, eigvalue] = SDA(gndTrain, feaTrain, semisplit, options); 
newfea = fea*eigvector; 