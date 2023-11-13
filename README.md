# ReadMe

this is a game developed with pygame.


## Peoject description
在游戏《外星人入侵》中，玩家控制一艘最初出现在屏幕底部中央的飞船。玩家可以使用箭头左右移动飞船，还可使用空格键设计。游戏开始时，一群外星人出现在天空中，并向屏幕下方移动。玩家的任务是射杀这些外星人。玩家将在所有外星人都消灭干净后，将出现一群新的外星人，其移动速度更快。只要有外星人撞到玩家的飞船或者到达屏幕底部，玩家就损失一艘飞船。玩家损失三艘飞船后。游戏结束。

## System requirement
- pygame

## Sprint Plan
#### Sprint1
- Day0 项目规划
编写项目描述
- Day1
game base
- Day2
move ship

#### Sprint 2
sprint2 backlog：
- [x] 1.回顾当前代码
- [x] 2.添加一个外星人
- [x] 3.创建多排外星人
    - [x] 3.1 一行外星人, 计算行的容量
    - [x] 3.2 多行外星人，计算列的容量
    - [x] 3.3 外星人群移动；
        - [x] 向右
        - [x] 检测边缘
        - [x] 向下
    - [x] 撞到飞船或者抵达底部停止
    - [x] 销毁飞船并重新创建外星人
- [x] 外星人击落
    - [x] 子弹与外星人碰撞
    - [x] 刷新所有外星人
- [x] 限制飞船数量，结束游戏
- Day4
add aliens
- Day5
add collisions
end game

### Sprint 3: 计分
<h5>sprint 3 backlog:</h5>

- [x] play button
    - [ ] create button
    - [ ] draw button
    - [ ] start game
    - [ ] reset game
    - [ ] hide play button
    - [ ] hide cursor
- [x] higher level
    - [ ] change game speed
    - [ ] reset game speed
- [ ] tally
    - [x] display score
    - [x] create tally board
    - [x] update score
    - [x] reset score
    - [x] count every aliens
    - [x] increase score
    - [x] round score
    - [x] highest score
    - [x] show levels
    - [x] display number of remaining ships
- Day6
1.complete play button; 2.complete higher level; 3.complete tally board except (1)score history and (2)display other game information.
- Day7
1.complete high score 2.display remaining ships 3.add bgm

**<h4>Summary:</h4>**

<p>
<b>开发tips</b>

要做项目管理和规划，写好任务清单，先思考明白开发思路，和程序结构框架再开发

先完成可以运行的代码，再去重构，出现效率问题再去优化

**pygame：**

surface对象，事件列表，外接矩形，导入图片，绘制图片和矩形，编组，编组绘画，编组使用（如 遍历），计算空间参数，碰撞检测，边缘检测，编组的碰撞检测，渲染文本，文本转化成图像，再转化成外接矩形，检测鼠标事件，碰撞字典，文字排版，保存信息为文件</p>