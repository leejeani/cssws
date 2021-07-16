class Sql:
    make_userdb = ''' CREATE  TABLE  IF NOT EXISTS USERDB (
        ID  TEXT  PRIMARY KEY,
        PWD  TEXT,
        NAME TEXT
    ) ''';
    insert_userdb = ''' INSERT  INTO  USERDB VALUES (?,?,?) ''';
    update_userdb = ''' UPDATE  USERDB  SET  PWD=?,  NAME=?  WHERE  ID=? ''';
    delete_userdb = ''' DELETE  FROM  USERDB  WHERE  ID=? ''';
    select_userdb = ''' SELECT  *  FROM  USERDB  WHERE ID=? ''';
    selectall_userdb = ''' SELECT  * FROM USERDB ''';

    make_itemdb = '''  
         CREATE  TABLE  IF  NOT  EXISTS  ITEMDB (
           ID INTEGER  PRIMARY KEY  AUTOINCREMENT,
           NAME  TEXT,
           PRICE  REAL,
           REGDATE  DATE DEFAULT (DATETIME('now','localtime'))
         ) 
     ''';
    insert_itemdb = '''  
         INSERT  INTO  ITEMDB (NAME,PRICE) VALUES  (?,?) 
     ''';
    update_itemdb = '''  
         UPDATE  ITEMDB  SET  NAME=?,  PRICE=?  WHERE ID=? 
     ''';
    delete_itemdb = '''  
         DELETE   FROM  ITEMDB  WHERE  ID = ? 
     ''';
    select_itemdb = '''   
         SELECT  *  FROM  ITEMDB  WHERE  ID = ?
     ''';
    selectall_itemdb = '''   
         SELECT  * FROM  ITEMDB
     ''';
