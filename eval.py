import vk_api
token=''
id= 

 vk_session = vk_api.VkApi(token=token)
 vk = vk_session.get_api()
 longpoll = VkLongPoll(vk_session)

 	for event in longpoll.listen():
 		if event.type == VkEventType.MESSAGE_NEW:
 			m_id = event.message_id

 			Peer_id = event.peer_id

 			if event.from_me == True:
 				try:
 					if (str(event.text).split(' ')[0] == '!eval'):
 						x = str(event.text)[6:]
 						x = x.replace("&quot;", "\'")
 						try:
 							send_msg(peer_id=peer_id, text="Input: "+str(x)+"\nOutput: "+str(eval(x)))
 						except Exception as error:
 							send_msg(peer_id=Ev.peer_id, text="Input: "+str(x)+"\nOutput: "+str(error))
