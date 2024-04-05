% INPUTS///////////////////////////////////////////////////////////////////
time_sequence = [1, 4, 6, 8, 10]; % error_index = 1 (first element)
% time_sequence = [3, 12, 11, 15, 19, 23]; % error_index = 2 (second_element)
% time_sequence = [3, 7, 17, 15, 19, 23]; % error_index = 3 (mid-element)
% time_sequence = [4, 10, 16, 22, 28, 34, 42, 46]; % error_index = 7 (first to the last element)
% time_sequence = [4, 10, 16, 22, 28, 34, 40, 78]; % error_index = 8 (last element)
% time_sequence = [8, 15, 22, 29]; % no error
% /////////////////////////////////////////////////////////////////////////

% SOLUTION/////////////////////////////////////////////////////////////////
[counts, elements] = groupcounts(diff(time_sequence).');
diff_val = elements(counts == max(counts));
new_sequence = time_sequence(1) : diff_val : time_sequence(1) + diff_val * (length(time_sequence) - 1);
[counts, elements] = groupcounts(abs(time_sequence - new_sequence).');
correct_sequence = new_sequence + elements(counts == max(counts));
error_index = find(correct_sequence ~= time_sequence);
if isempty(error_index)
    fprintf("Time sequence is correct.");
end
% /////////////////////////////////////////////////////////////////////////