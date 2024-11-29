
data = readtable('sit_down_4.csv');
b1 = data.Var1;
b2 = data.Var2;
b3 = data.Var3;
b4 = data.Var4;
b5 = data.Var5;
b6 = data.Var6;
b7 = data.Var7;
s1 = data.Var8;
s2 = data.Var9;
s3 = data.Var10;
s4 = data.Var11;
s5 = data.Var12;
s6 = data.Var13;
s7 = data.Var14;
s8 = data.Var15;
D1 = data.Var16;
%%
const = 10;
plot(smoothdata(s1,"gaussian",const));hold on
title('Seat')
plot(smoothdata(s2,"gaussian",const))
plot(smoothdata(s3,"gaussian",const))
plot(smoothdata(s4,"gaussian",const))
plot(smoothdata(s5,"gaussian",const))
plot(smoothdata(s6,"gaussian",const))
plot(smoothdata(s7,"gaussian",const))
plot(smoothdata(s8,"gaussian",const))
plot(D1*800)
hold off
ylim([500,950])
legend('s1','s2','s3','s4','s5','s6','s7','s8','D1')
figure()

plot(smoothdata(b1,"gaussian",const));hold on
title('Back')
plot(smoothdata(b2,"gaussian",const))
plot(smoothdata(b3,"gaussian",const))
plot(smoothdata(b4,"gaussian",const))
plot(smoothdata(b5,"gaussian",const))
plot(smoothdata(b6,"gaussian",const))
plot(smoothdata(b7,"gaussian",const))
plot(D1*800)
hold off
ylim([480,660])
legend('b1','b2','b3','b4','b5','b6','b7','D1')
%%

%plot(smoothdata(b1,"gaussian",const));hold on
%plot(smoothdata(s1,"gaussian",const))
%hold off
