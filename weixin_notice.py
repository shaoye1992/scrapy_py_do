import itchat

itchat.auto_login(enableCmdQR= -1)

accounts = itchat.get_friends()
name_find = '失足'
b = itchat.search_friends(nickname = name_find)
user_num = b[0]['User']

