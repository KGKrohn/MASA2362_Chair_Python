
data = readtable('back.csv');
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

plot(s1);hold on
title('Seat')
plot(s2)
plot(s3)
plot(s4)
plot(s5)
plot(s6)
plot(s7)
plot(s8)
hold off
legend('s1','s2','s3','s4','s5','s6','s7','s8')
figure()

plot(b1);hold on
title('Back')
plot(b2)
plot(b3)
plot(b4)
plot(b5)
plot(b6)
plot(b7)
hold off
legend('b1','b2','b3','b4','b5','b6','b7','b8')
