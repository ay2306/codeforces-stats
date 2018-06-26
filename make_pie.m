hold on;
data = load('data.csv');
labels = {"Accepted","Wrong Answer","Compilation Error","Time Limit Exceeded","Memory Limit Exceeded","Others"};
pie(data);
legend(labels);
disp(data(1))
print -djpg image.jpg