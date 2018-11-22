clear all;
clc;
close all;

% T = readtable('Crimes_-_2001_to_present.csv');
pruned_data = readtable('new_csv.csv');


% Important features
% temp = T(1:20000, {'Date', 'LocationDescription','Beat','District', 'Ward', 'CommunityArea', 'PrimaryType'});


