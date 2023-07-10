<template>
    <div>
      <h1 class="chatroom-title">Chatroom</h1>
      <div class="chatroom">
        <div class="chatroom-messages">
          <div v-for="message in messages" :key="message.id" class="message">
            <div class="message-sender">{{ message.sender }}</div>
            <div class="message-content">{{ message.content }}</div>
          </div>
        </div>
  
        <div class="chatroom-input">
          <input
            type="text"
            v-model="newMessage"
            placeholder="Type your message"
            @keydown.enter="sendMessage"
          />
          <button @click="sendMessage">Send</button>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import { ref } from 'vue';
  
  export default {
    data() {
      return {
        messages: [
          { id: 1, sender: 'Alice', content: 'Hello!' },
          { id: 2, sender: 'Bob', content: 'Hi Alice!' },
          { id: 3, sender: 'Alice', content: 'How are you?' },
          { id: 4, sender: 'Bob', content: "I'm doing well. Thanks!" },
        ],
        newMessage: '',
      };
    },
    methods: {
      sendMessage() {
        if (this.newMessage.trim() === '') {
          return; // Prevent sending empty messages
        }
  
        this.messages.push({
          id: this.messages.length + 1,
          sender: 'Alice',
          content: this.newMessage.trim(),
        });
  
        this.newMessage = '';
      },
    },
  };
  </script>
  
  <style>
  .chatroom {
    display: flex;
    flex-direction: column;
    height: 100%;
    padding-top: 50px;
    padding-left: 20px;
    padding-right: 20px;
  }
  
  .chatroom-title {
    text-align: center;
    font-size: 24px;
    padding-top: 20px;
    margin-bottom: 20px;
  }
  
  .chatroom-messages {
    flex-grow: 1;
    overflow-y: scroll;
  }
  
  .message {
    background-color: #f0f0f0;
    border-radius: 10px;
    margin-bottom: 10px;
    padding: 10px;
  }
  
  .message-sender {
    font-weight: bold;
  }
  
  .message-content {
    margin-top: 5px;
  }
  
  .chatroom-input {
    display: flex;
    align-items: center;
    margin-top: 10px;
  }
  
  .chatroom-input input {
    flex-grow: 1;
    padding: 5px;
  }
  
  .chatroom-input button {
    margin-left: 10px;
  }
  </style>
  