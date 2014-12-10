function [] = mace_test( input_path1, input_path2 )
%UNTITLED3 Summary of this function goes here
%   Detailed explanation goes here

img1 = imread(input_path1);
img1 = double(rgb2gray(img1));
img1 = imresize(img1, 0.33);

img2 = imread(input_path2);
img2 = double(rgb2gray(img2));
img2 = imresize(img2, 0.33);

[r, c] = size(img2);

H = MACE(img1(:), [1]);
        
resp_2 = fft2(img2(:)) .* conj(H);

resp_reshape_2 = reshape(ifft2(resp_2), [r,c]);

surf(real(resp_reshape_2));


sorted_m = sort(real(ifft2(resp_2)), 'descend');

shortlist = sorted_m(1:500);

m1 = shortlist(1);
m2 = mean(shortlist(2:100));

m1
m2



end

