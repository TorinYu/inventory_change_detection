function [ H ] = MACE( class1, u )
%UNTITLED3 Summary of this function goes here
%   Detailed explanation goes here
    [d, n] = size(class1);
    X = zeros(d,n);
    D = zeros(d,d);
    for i = 1 : n
        X(:,i) = fft2(class1(:,i));
        D = D + diag(X(:, i) .* conj(X(:, i)));
    end
    D = D./n;
    H = D\X/(X'/D * X) * u; 

end

