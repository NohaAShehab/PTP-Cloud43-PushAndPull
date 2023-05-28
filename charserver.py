from simple_websocket_server import WebSocketServer, WebSocket
import  json


def remove_dict_from_list(list_of_dict :list, key):
    for item in list_of_dict:
        if key in item.keys():
            list_of_dict.remove(item)

    return  list_of_dict
class Chatserver(WebSocket):
    ## call some functions --> open connection to server, closing
    clients =[]
    def connected(self):
        # print("==== this function will be called when client connected the server")
        print(self.address, 'connected')
        # print(self.__class__)
        # self.__class__.clients.append(self)

    def handle_close(self):
        # print("--- this function will be called when a client disconnected from the server ")
        print(self.address, 'closed')
        self.__class__.clients = remove_dict_from_list(self.__class__.clients, self)
        print(f"no of connected users till now {len(self.__class__.clients)}")





    def handle(self):
        # echo message back to client
        print("=== this function will be called when the server receives message from the client ")
        # self.send_message(self.data)
        # print(f"message: {self.data}") # string --> hold json object
        data =  json.loads(self.data)
        print(data, type(data))
        if 'login' in data:
            print("---hi")
            self.__class__.clients.append({self:data['username']})
            print(f"no of connected users till now {len(self.__class__.clients)}")



if __name__=='__main__':
    print("--- server started ")
    server = WebSocketServer('localhost', 8000, Chatserver)
    server.serve_forever()
    print("Welcome to chat server")



