import tensorflow as tf
import matplotlib.pyplot as plt
 
#�������� ����
graph = tf.get_default_graph()
 
#�������� ������� ��������
input_value = tf.constant(1.0)
 
#�������� ����������
weight = tf.Variable(0.8)
 
#������� �������� ��������
output_value = weight * input_value
 
#������� ������
sess = tf.Session()
 
#������� ������������
desired_output_value = tf.constant(2.0)
loss = (output_value - desired_output_value)**2 #������� ������
optim = tf.train.GradientDescentOptimizer(learning_rate=0.025) #�����������
grads_and_vars = optim.compute_gradients(loss)
 
#�������������� ����������
init=tf.global_variables_initializer()
sess.run(init)
 
#������ ��������� �������
x=[]
y=[]
 
 
#�������
train_step = tf.train.GradientDescentOptimizer(0.025).minimize(loss)
for i in range(100):
    sess.run(train_step)
    x.append(i)
    y.append(sess.run(loss))
 
print(sess.run(output_value))
 
#������ ������
fig = plt.figure()
plt.plot(x, y)
 
#���������� ��������� � ������� ����
plt.title('������ �������')
plt.ylabel('��� Y')
plt.xlabel('��� X')
plt.grid(True)
plt.show()

'''
import tensorflow as tf
 
#�������� ����
graph = tf.get_default_graph()
 
#�������� ������� ��������
input_value = tf.constant(1.0)
 
#�������� ����������
weight = tf.Variable(0.8)
 
#������� �������� ��������
output_value = weight * input_value
 
#������� ������
sess = tf.Session()
 
#������� ������������
desired_output_value = tf.constant(2.0)
loss = (output_value - desired_output_value)**2 #������� ������
optim = tf.train.GradientDescentOptimizer(learning_rate=0.025) #�����������
grads_and_vars = optim.compute_gradients(loss)
 
#�������������� ����������
init=tf.global_variables_initializer()
sess.run(init)
 
 
#�������
train_step = tf.train.GradientDescentOptimizer(0.025).minimize(loss)
for i in range(100):
    sess.run(train_step)
 
print(sess.run(output_value))
'''