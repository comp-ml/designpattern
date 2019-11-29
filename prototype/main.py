import prototype

teach = prototype.Teacher()
papers = teach.createManyCrystal()

[print(i,':',paper.draw ,paper.cut, paper) for i, paper in enumerate(papers)]
