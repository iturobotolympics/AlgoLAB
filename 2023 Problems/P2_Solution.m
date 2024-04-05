% INPUTS///////////////////////////////////////////////////////////////////
CC = "AE";
% /////////////////////////////////////////////////////////////////////////

% SOLUTION/////////////////////////////////////////////////////////////////
if CC == "AE"
    CC_num = [3, 4, randi([0, 9], [1, 13])];
    control_array = ceil(mod(flip(CC_num(1 : end - 1)) .* repmat([2, 1], [1, 7]), 9.1));
else
    if CC == "MC"
        CC_num = [5, 2, randi([0, 9], [1, 14])];
    else
        CC_num = [4, randi([0, 9], [1, 15])];
    end
    control_array = ceil(mod(flip(CC_num(1 : end - 1)) .* [repmat([2, 1], [1, 7]), 2], 9.1));
end
CC_num(end) = mod(sum(control_array), 10);
% /////////////////////////////////////////////////////////////////////////