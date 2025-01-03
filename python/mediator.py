from abc import ABC, abstractmethod

'''
Example - A Chat Room Mediator
- A chat room where users can communicate with each other.
- The chat room acts as a mediator between users.
- Users can send messages to each other via the chat room.
'''


# Mediator Interface
class ChatRoomMediator(ABC):
    @abstractmethod
    def show_message(self, user, message):
        pass


# Concrete Mediator
class ChatRoom(ChatRoomMediator):
    def show_message(self, user, message):
        print(f"[{user.name}] says: {message}")


# Colleague Class
class User:
    def __init__(self, name, mediator):
        self.name = name
        self.mediator = mediator

    def send_message(self, message):
        self.mediator.show_message(self, message)


# Client Code
if __name__ == "__main__":
    # Create the mediator
    chat_room = ChatRoom()

    # Create colleagues (users)
    user1 = User("Alice", chat_room)
    user2 = User("Bob", chat_room)

    # Communication between users via the mediator
    user1.send_message("Hi Bob!")
    user2.send_message("Hello Alice!")
