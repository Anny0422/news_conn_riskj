# news_conn_risk
1、从数据库中读取想要的数据，插入到一个新表中；
只需：
sql_saved = "select appItemId, detail from tFastNews_jrj"
if __name__ == '__main__':
    CR = ConnRisk()
    db = Database()
    db.connect('news_connect_keywords')
    saved_files = CR.conn_db()
    print(len(saved_files))
    contents = CR.get_json(saved_files)
    print(contents[0])
## 关于从一个表中选择指定列插入到另一个表的指定列操作：
# insert into stock.news_conne_risk1 (oldID, Content) select SinaID, content from stock.tFastNews_Sina;



2、将从数据库中读到的数据匹配风险，更新到表stock.news_conn_risk中。
只需：
if __name__ == '__main__':
    CR = ConnRisk()
    db = Database()
    db.connect('news_connect_keywords')
    saved_files = CR.conn_db()
    print(len(saved_files))
    contents = CR.get_json(saved_files)
    
    risk_dict = CR.get_riskdict(CR.csv_risk)
    texts = CR.get_risklabel(contents, risk_dict)
    print("匹配上风险的新闻数量为:", len(texts))
    print("具体情况为:", texts)
    CR.run1(texts)
    ret = myEmail.mail('若运行完成')
    if ret:
        print("邮件发送成功")
    else:
        print("邮件发送失败")

