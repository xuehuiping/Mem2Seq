
date: 2020/4/19 3:06 下午 
https://github.com/HLTCHKUST/Mem2Seq
Mem2Seq: Effectively Incorporating Knowledge Bases into End-to-End Task-Oriented Dialog Systems (ACL 2018).

Mem2Seq有效结合KB与端到端任务型对话系统

针对RNN存在长时间遗忘的问题，基于MemNN,本文提出了Mem2Seq模型

当前较为流行的端到端任务型对话系统


主要贡献：

1）Mem2Seq是第一个将多跳注意力机制与指针网络结合起来的模型，并允许我们有效地结合知识库信息。

2）Mem2Seq学习了如何动态生成查询去控制Memory的访问，可以可视化memory控制器和attention的跳跃之间的模型动态。

3）Mem2Seq可以更快地进行训练，并在几个任务型对话数据集中实现最先进的结果。



本仓库实现：
- Mem2Seq: Memory to Sequence (Our model)
- Seq2Seq: Vanilla seq2seq model with no attention (enc_vanilla)
- +Attn: Luong attention attention model
- Ptr-Unk: combination between Bahdanau attention and Pointer Networks (Point to UNK words)


## 运行demo
```
2020-04-19 14:52:15 可以运行，关掉当前，放到后台运行

nohup python3 main_train.py -lr=0.001 -layer=1 \
-hdd=128 -dr=0.2 -dec=Mem2Seq -bsz=8 -ds=babi -t=1  > log.4.19.txt &
```

```
模型文件命名规则： directory = 'save/mem2seq-'+name_data+str(self.task)+
'HDD'+str(self.hidden_size)+'BSZ'+str(args'batch')+'DR'+str(self.dropout)+'L'+str(self.n_layers)+'lr'+str(self.lr)+str(dec_type)
```
```
(env) xuehp@haomeiya002:~/git/Mem2Seq$ ll save/mem2seq-BABI/
total 32
drwxrwxr-x 8 xuehp xuehp 4096 Apr 19 15:03 .
drwxrwxr-x 4 xuehp xuehp 4096 Apr 19 14:51 ..
drwxrwxr-x 2 xuehp xuehp 4096 Apr 19 14:55 1HDD128BSZ8DR0.2L1lr0.001Mem2Seq0.6407437310030395
drwxrwxr-x 2 xuehp xuehp 4096 Apr 19 14:51 1HDD128BSZ8DR0.2L1lr0.001Mem2Seq0.7792315729483283
drwxrwxr-x 2 xuehp xuehp 4096 Apr 19 14:56 1HDD128BSZ8DR0.2L1lr0.001Mem2Seq0.8792980623100305
drwxrwxr-x 2 xuehp xuehp 4096 Apr 19 14:59 1HDD128BSZ8DR0.2L1lr0.001Mem2Seq0.8816251899696049
drwxrwxr-x 2 xuehp xuehp 4096 Apr 19 15:01 1HDD128BSZ8DR0.2L1lr0.001Mem2Seq0.946286094224924
drwxrwxr-x 2 xuehp xuehp 4096 Apr 19 15:03 1HDD128BSZ8DR0.2L1lr0.001Mem2Seq0.9477821048632219

其中，dec_type=
str(self.name)+str(bleu_score)
或者
str(self.name)+str(acc_avg)
```


## 分析一下数据集
上面实验用的是babi数据集。
该数据集包含6个任务，测试端到端的系统，在餐馆领域。
babi是Bordes & Weston的论文《学习端到端面向目标的对话框》(http://arxiv.org/abs/1605.07683)中描述的数据集。
每个任务测试对话的一个独特方面。
任务的设计是为了补充已经发布的20个bAbI任务的故事理解，Weston等人的论文《Towards AI Complete Question Answering: A Set of Prerequisite Toy Tasks》(http://arxiv.org/abs/1502.05698)

每个任务中，都有1000个对话用于训练，1000个用于验证，1000个用于测试。

对于任务1-5，还有第二个测试集，后缀是-OOV.txt，包含的对话中的实体并没有在训练集和开发集中出现。

文件的格式是：
ID user_utterance [tab] bot_utterances


task6的数据集有些特殊，因为它来自于DSTC2。我们对其进行了修改，将其转换为与其他任务相同的格式。没有与此任务相关的OOV测试集，知识库也不完善。此任务有自己的候选文件dialog-babi-task6-dstc2-candidates.txt。

关于数据集的更多细节和baselilnes，参考《Learning End-to-End Goal-Oriented Dialog》，by Antoine Bordes and Jason Weston (http://arxiv.org/abs/1605.07683). 

## 分析实验结果
```
!python3 main_test.py -dec=Mem2Seq \
-path=save/mem2seq-BABI/1HDD128BSZ8DR0.2L1lr0.001Mem2Seq1.0 -bsz=8 -ds=babi -t=1
```

模型文件mem2seq-BABI/1HDD128BSZ8DR0.2L1lr0.001Mem2Seq1.0
实验结果最好的是：
训练集：Dialog Accuracy:	1.0； BLEU SCORE:100.0
测试集：Dialog Accuracy:	0.439；BLEU SCORE:94.31

acc_test = 0.894

---
python3 main_test.py -dec=Mem2Seq \
-path=save/mem2seq-BABI/6HDD128BSZ8DR0.2L1lr0.001Mem2Seq0.5316620879120879 -bsz=8 -ds=babi -t=6 > log.4.22.txt

04-22 08:30 Dialog Accuracy:	0.0008952551477170994
04-22 08:30 F1 SCORE:	0.7040530544521351
04-22 08:30 BLEU SCORE:53.81
acc_test = 0.4103024911032029

[](log_Mem2Seq_babi_1/2020-04-20-12-11-47.png)

## 原始论文
/Users/huihui/KPI-研读论文/1605.07683.任务型.端到端对话.pdf

数据集http://fb.ai/babi，即https://research.fb.com/downloads/babi/
https://github.com/facebookarchive/bAbI-tasks




[](log_Mem2Seq_babi_1/2020-04-20-12-11-47.png)


https://zhuanlan.zhihu.com/p/44110616

https://zhuanlan.zhihu.com/p/108095526
