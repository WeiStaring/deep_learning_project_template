# 深度学习项目模板
## 模板由来
深度学习的科研项目存在许多需求，一般的需求包括收集数据，数据处理，模型搭建等等。复杂的需求包括对比实验，消融实验等。这些需求会显著增加代码量。当项目到了后期，项目规模会越发膨胀，维护项目常常让人力不从心。此时一个好的架构能够将项目清楚地划分为多个组件，最大程度地降低项目的复杂度和维护开销。因此，我阅读了多个项目的架构，总结了一套自己的项目架构，供后人使用。
## 架构讲解
本架构是基于机器学习流程和实际科研实践总结出来的。按顺序如下展示
1. data：存放原始数据
2. data_dealer：数据预处理，包括原始数据处理和torch数据处理
3. source：存放中间数据，例如knn图或者整个模型 
4. data_torch_dealer：将data或source中处理好的数据转换为torch可迭代数据
5. config：定义模型超参数和训练超参数
6. model：搭建模型
7. loss：构建损失函数
8. trainer：针对model的训练器
9. tester：针对model的测试器
10. method: trainer和tester之上的更宏观的一层，用来描述整个方法，包括model，loss，trainer和tester。
11. result：存放训练结果和测试结果
12. utils：在上述过程中可以剥离的一般化函数，例如文件读取，可视化。
13. MultiMethodTestFramework: 在method层面进行统一的测试，例如多数据集多方法的对比。
## 架构是如何与ML科研流程对应的
1. 收集数据，存放于data文件夹
2. 查看和清晰数据，在transform文件夹中编写清洗程序，将清洗后的数据存放于source下的data文件夹。
3. 搭建模型，在model中创建模型
4. 编写损失函数，在loss中创建
5. 搭建数据迭代器，在在torch_data_dealer文件夹中编写
6. 搭建训练器，在trainer中创建训练类，使用config中定义的超参数，传入model中的模型,loss中的损失函数和data_torch_dealer中的训练数据迭代器，训练好的模型课存放于source中，训练日志和结果存放于result中
7. 建测试器，在tester中创建测试类，使用config中定义的超参数，传入source中的模型参数和data_torch_dealer中的测试数据迭代器和utils中的指标，测试日志和结果存放于result中
8. 在method中创建继承类，将上述的data，model，loss，trainer和tester进行统筹。
9. 查看训练结果和测试结果。
10. 修改模型架构，在model中创建继承类，在method中创建继承类
11. 修改损失函数，在loss中创建继承类，在method中创建继承类
12. 修改训练方式，在trainer中创建继承类，在method中创建继承类
13. 进行多数据集的对比，编写新的训练器和测试器，在method中定义一组数据迭代器，将这组数据迭代器传入新的训练器和测试器中。
14. 进行多方法的对比，在method中引入其他方法，然后构建新的对应的测试器，在MultiMethodTestFramework中统一的测试我们方法和他人方法，例如提前定义一组数据迭代器，传入method中，然后传入训练器和测试器中。