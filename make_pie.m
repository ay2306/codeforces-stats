warning off;
hold on;
data = load('data.csv');
labels = {"Accepted","Wrong Answer","Compilation Error","Time Limit Exceeded","Memory Limit Exceeded","Others"};
pie(data);
legend(labels);
print -djpg image.jpg
