from simple_websocket_server import WebSocketServer, WebSocket
import  json
# from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket


def remove_dict_from_list(list_of_dict :list, key):
    for item in list_of_dict:
        if key in item.keys():
            list_of_dict.remove(item)

    return  list_of_dict
class Chatserver(WebSocket):
    clients =[]
    users = []
    def connected(self):
        print(self.address, 'connected')
        self.__class__.users.append(self)

    def handle_close(self):
        message= f"--->{self.username} has been disconnected\n"
        print(self.address, 'closed')
        self.__class__.clients = remove_dict_from_list(self.__class__.clients, self)
        self.__class__.users.remove(self)
        for user in self.__class__.users:
                user.send_message(json.dumps({"message":message}))





    def handle(self):
        msg = self.prepare_message(self.data)
        print(msg)
        for user in self.__class__.users:
            if user !=self:
                user.send_message(msg)
                print(f"--- message sent to client {user}")


    def prepare_message(self, message):
        data = json.loads(message)
        print(data)
        if 'login' in data:
            self.__class__.clients.append({self: data['username']})
            self.username = data['username']
            message_to_send = f"--->{data['username']} has been connected\n"
        else:
            message_to_send = f"{data['username']}:{data['message']}\n"

        message_to_send = json.dumps({"message":message_to_send})
        return  message_to_send



if __name__=='__main__':
    print("--- server started ")
    server = WebSocketServer('localhost', 8000, Chatserver)
    server.serve_forever()
    print("Welcome to chat server")



